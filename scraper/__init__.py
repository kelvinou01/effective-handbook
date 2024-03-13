import json
import os
import re
from typing import Dict

import config
import html2text
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def adjust_headings(body_md):
    """
    Adjusts headings of the body text such that h2 is the largest heading.
    e.g. If the body's largest heading is h1, everything will be shrunk by 1.
    If the body's largest heading is h4, everything will be enlargened by 2.
    """
    heading_pattern = re.compile(r"^(#{1,6})\s(.+)$", re.MULTILINE)
    matches = heading_pattern.findall(body_md)

    min_heading_level = min(len(match[0]) for match in matches) if matches else 0
    adjust_amount = 2 - min_heading_level

    adjusted_markdown = body_md
    for match in matches:
        original_heading, heading_text = match
        heading_level = len(original_heading.strip())
        new_heading_level = heading_level + adjust_amount
        adjusted_heading = f"{'#' * new_heading_level} {heading_text}"
        adjusted_markdown = adjusted_markdown.replace(f"{original_heading} {heading_text}", adjusted_heading, 1)

    return adjusted_markdown


def fix_references(markdown_text):
    # Replaces [number] with [^number]
    pattern = r"\[(\d+)\]"
    replacement = r"[^\1]"
    updated_text = re.sub(pattern, replacement, markdown_text)

    return updated_text


def parse_main_content(article_html):
    soup = BeautifulSoup(article_html, "html.parser")

    # Remove any elements with class "footnotes" from the main content
    for footnotes_section in soup.find_all(class_="footnotes"):
        footnotes_section.decompose()

    # Convert references into strings of the format [^1]
    # Some posts use sup, others use span for references
    ref_elements_format_1 = soup.find_all("sup", id=re.compile(r"fnref-\d+"))
    ref_elements_format_2 = soup.find_all("span", class_="footnote-reference")

    if ref_elements_format_1:
        for sup in ref_elements_format_1:
            footnote_number = re.search(r"\d+", sup["id"]).group()
            sup.replace_with(f"[^{footnote_number}]")
    elif ref_elements_format_2:
        for span_element in ref_elements_format_2:
            sup_element = span_element.find("sup")
            a_element = sup_element.find("a")
            footnote_number = a_element.get_text(strip=True)[1:-1]
            span_element.string = f"[^{footnote_number}]"

    # Parse main content with HTML2Text
    converter = html2text.HTML2Text()
    converter.body_width = 0
    main_content = converter.handle(str(soup))

    num_references = len(get_footnote_list_items(article_html))
    if num_references > 0:
        # Convert footnotes: [1] into [^1]
        main_content = fix_references(main_content)
    else:
        # The article doesn't actually have any footnotes at the bottom
        # The footnote references in the article body are just links, not actual references
        # e.g. https://forum.effectivealtruism.org/s/x3KXkiAQ6NH8WLbkW/p/ER4gAtS5LAx2T3Y98
        # Hence, don't convert into [^1] format, which is a pattern used to denote actual references.
        pass

    return main_content


def indent_footnote(footnote):
    lines = footnote.split("\n")
    if len(lines) > 1:
        # Indent subsequent paragraphs with four spaces
        indented_lines = [lines[0]] + ["    " + line if line.strip() else line for line in lines[1:]]
        return "\n".join(indented_lines)
    else:
        return footnote


def get_footnote_list_items(article_html):
    soup = BeautifulSoup(article_html, "html.parser")

    converter = html2text.HTML2Text()
    converter.body_width = 0

    # Extract the footnotes section.
    # Some forum posts have different formats for footnotes.
    footnotes_section_div = soup.find("div", class_="footnotes")
    footnotes_section_section = soup.find("section", class_="footnotes")
    footnotes_section_ol = soup.find("ol", class_="footnotes")

    if footnotes_section_div:
        footnotes_section = footnotes_section_div
    elif footnotes_section_section:
        footnotes_section = footnotes_section_section
    elif footnotes_section_ol:
        footnotes_section = footnotes_section_ol
    else:
        return ""

    # Extract individual footnote items
    return footnotes_section.find_all("li")


def parse_footnotes(article_html):
    converter = html2text.HTML2Text()
    footnotes_items = get_footnote_list_items(article_html)

    # Parse footnotes into the desired format
    footnotes = []
    for num, item in enumerate(footnotes_items, start=1):
        item = "".join(str(tag) for tag in item)
        footnote_text = converter.handle(str(item)).strip()
        footnote_text = footnote_text.replace("↩", "").rstrip()
        if footnote_text.startswith("**^**"):  # some have this, some don't
            footnote_text = footnote_text[6:]
        footnote_text = footnote_text.strip()
        footnote_text = indent_footnote(footnote_text)
        footnotes.append(f"[^{num}]: {footnote_text}")

    return "\n".join(footnotes)


def body_contains_h1(body_md):
    lines = body_md.split("\n")
    return any(line.strip().startswith("# ") for line in lines)


def process_into_md(article_title, article_html):
    body_md = parse_main_content(article_html)
    body_md = adjust_headings(body_md)
    body_md = f"# {article_title}\n{body_md}"
    footer_md = parse_footnotes(article_html)

    return body_md, footer_md


def renumber_references(markdown_text, start_number=1):
    reference_pattern = re.compile(r"\[\d+\]")
    unique_references = set(reference_pattern.findall(markdown_text))
    reference_mapping = {old_ref: f"[{start_number + i}]" for i, old_ref in enumerate(unique_references)}

    for old_ref, new_ref in reference_mapping.items():
        markdown_text = markdown_text.replace(old_ref, new_ref)

    return markdown_text


def scrape_raw_article(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        target_div = soup.find("div", class_="PostsPage-postContent")

        if target_div:
            # Extract the inner HTML of the target <div>
            content = str(target_div)
            return content
        else:
            print("Target <div> not found on the webpage.")
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")


def scrape_article_links() -> Dict[str, Dict[str, str]]:
    response = requests.get(config.HANDBOOK_URL)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        sequence_items = soup.find_all("div", class_="LargeSequencesItem-root")
        result_dict = {}

        for sequence_item in sequence_items:
            chapter_element = sequence_item.find("a", class_="LargeSequencesItem-title")
            if chapter_element:
                chapter_title = chapter_element.text.strip()

                articles = {}
                post_link_elements = sequence_item.find_all("div", class_="SequencesSmallPostLink-title")
                for post_link_element in post_link_elements:
                    link_title_element = post_link_element.find("a")
                    if link_title_element:
                        link_title = link_title_element.text.strip()
                        link_url = config.FORUM_URL + link_title_element["href"]
                        articles[link_title] = link_url

                result_dict[chapter_title] = articles

        return result_dict
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")


def increment_body_references(body_md, n):
    def increment(match):
        number = int(match.group(1))
        new_number = number + n
        return "[^" + str(new_number) + "]"

    pattern = re.compile(r"\[\^(\d+)\]")
    return re.sub(pattern, increment, body_md)


def combine_articles(bodies, footnotes):
    new_articles = []
    total_footnote_count = 0

    for body, footer in zip(bodies, footnotes):
        new_body = increment_body_references(body, total_footnote_count)
        new_footnotes = []
        for line in footer.split("\n"):
            if re.search(r"\[\^(\d+)\]", line):  # Identify footnote references
                total_footnote_count += 1
                line = re.sub(r"\[\^(\d+)\]", f"[^{total_footnote_count}]", line)
            new_footnotes.append(line)

        new_footnotes = "\n".join(new_footnotes)
        new_articles.append(new_body + new_footnotes)
    return "\n".join(new_articles)


if __name__ == "__main__":
    chapter_map = scrape_article_links()
    with open(config.LINKS_PATH, "w") as f:
        json.dump(chapter_map, f, indent=4)

    with open(config.LINKS_PATH, "r") as f:
        chapter_map = json.load(f)

    for chapter, title_to_link in tqdm(chapter_map.items()):
        dirname = chapter.lower().replace(" ", "-")
        chapter_dir = os.path.join(config.RESULTS_DIR, dirname)
        os.mkdir(chapter_dir)

        bodies = []
        footers = []

        for title, link in tqdm(title_to_link.items()):
            filename = title.lower().replace(" ", "-")
            article_html = scrape_raw_article(link)
            html_path = os.path.join(chapter_dir, f"{filename}.html")
            with open(html_path, "w") as f:
                f.write(article_html)

            body_md, footer_md = process_into_md(title, article_html)
            bodies.append(body_md)
            footers.append(footer_md)
            md_path = os.path.join(chapter_dir, f"{filename}.md")
            with open(md_path, "w") as f:
                article_md = body_md + footer_md
                f.write(article_md)

        chapter_md = combine_articles(bodies, footers)
        chapter_path = os.path.join(config.RESULTS_DIR, f"{dirname}.md")

        with open(chapter_path, "w") as f:
            f.write(chapter_md)
        break
