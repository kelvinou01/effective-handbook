document.addEventListener("mouseup", function (event) {
	var selection = window.getSelection().toString();

	if (selection !== "") {
		// Check if the selected text is already highlighted
		if (isHighlighted(event.target, selection)) {
			console.log("isHighlighted");
			// Unhighlight if already highlighted
			unhighlightText(event.target, selection);
		} else {
			console.log("!isHighlighted");
			// Highlight if not already highlighted
			highlightText(event.target, selection);
		}
	}
});

function isHighlighted(element, text) {
	var html = element.innerHTML;
	var highlightedHtml = html.replace(new RegExp('<span class="highlighted">(.*?)</span>', "g"), "$1");
	return html !== highlightedHtml;
}

function highlightText(element, text) {
	var html = element.innerHTML;
	var highlightedHtml = html.replace(new RegExp("(" + text + ")", "g"), '<span class="highlighted">$1</span>');
	element.innerHTML = highlightedHtml;
}

function unhighlightText(element, text) {
	var html = element.innerHTML;
	var unhighlightedHtml = html.replace(new RegExp('<span class="highlighted">(.*?)</span>', "g"), "$1");
	element.innerHTML = unhighlightedHtml;
}
