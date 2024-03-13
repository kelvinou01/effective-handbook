+++
title = '7. What Do You Think?'
date = 2024-02-03T01:12:26+08:00
draft = false
weight = 70
+++

# What do you think?

> _“It is one of the unfortunate truisms of the human condition that there is hardly a good idea, noble impulse, or sound suggestion that can't be (and isn't eventually) adopted and bastardized by zealots… One iteration of this tendency is in the idea of “effective altruism.”_

\- [_K. Berger & R. M. Penna_](https://ssir.org/articles/entry/the_elitist_philanthropy_of_so_called_effective_altruism#:~:text=By%20contrast%2C%20defective%20altruism%20is,and%20beneficiaries%20against%20one%20another.)

In this chapter, we’ll give you time to reflect on what you think of effective altruism, and of the specific potential priorities you’ve heard about so far.

We are dedicating a section to this because, to whatever extent we are wrong, realizing and correcting our mistakes will allow us to do more good. Honestly reckoning with strong counterarguments (from both within and outside of the EA community) can help us avoid [_confirmation bias_](https://www.lesswrong.com/tag/confirmation-bias#:~:text=Confirmation%20bias%20(also%20known%20as,beliefs%20or%20hypotheses%20%5B1%5D.) and groupthink, and get us a little closer to identifying the most effective ways to do good.

Such critiques have led to important changes in what many EAs do. For example, GiveWell received some criticisms for making moral tradeoffs on behalf of the people they were trying to help. [_In response, they reached out to a sample of people demographically similar to the people affected by their analysis, and asked them how they would make moral tradeoffs._](https://www.vox.com/future-perfect/2019/12/20/21009803/givewell-survey-kenya-ghana-saving-lives-poverty)

A key concept for this session is the importance of **forming independent impressions.** In the long run, you’re likely to gain a deeper understanding of important issues if you think through the arguments for yourself. But (since you can’t reason through everything) it can still sometimes make sense to defer to others when you’re making decisions.

We are also including pieces on Bayes’ rule and general approaches to dealing with evidence in this session because it is another tool that can be utilized for a wide range of difficult decisions. By thinking more clearly about how much we should update our views based on new evidence, we can become more calibrated and thereby better decision-makers.

_This work is licensed under a_[ _Creative Commons Attribution 4.0 International License_](https://creativecommons.org/licenses/by/4.0/) _._

# Bayes' rule: Guide

This is a linkpost for [https://arbital.com/p/bayes_rule/?l=1zq](https://forum-bots.effectivealtruism.org/out?url=https%3A%2F%2Farbital.com%2Fp%2Fbayes_rule%2F%3Fl%3D1zq)

{{< rawhtml >}}

<html>
  <head>
    <script type="module" src="https://js.withorbit.com/orbit-web-component.js"></script>
  </head>
  <body>
    <orbit-reviewarea color="blue">
      <orbit-prompt
        question="What are prior and posterior odds in Bayes rule?"
        answer="
- Suppose we're testing patients for covid-19. 
- **Prior odds** is the proportion of sick to healthy patients, P(sick) / P(healthy). 
- **Posterior odds** is the proportion of sick to healthy patients amongst those with positive test results, P(sick | positive) / P(healthy | positive)"
      ></orbit-prompt>
      <orbit-prompt
        question="What is the relative likelihood in Bayes rule?"
        answer="
- Suppose we're testing patients for covid-19. 
- **Relative likelihood** is how much more likely a sick patient gets a positive test compared to a healthy patient, P(positive | sick) / P(positive | healthy). 
- A **relatively likelihood** of 3:1 means a sick patient is 3 times more likely to get a positive test."
      ></orbit-prompt>
      <orbit-prompt
        question="What is Bayes' rule in odds form?"
        answer="
- Prior odds x relative likelihoods = posterior odds. 
- P(sick)/P(healthy) x P(positive|sick)/P(positive|healthy) = P(sick|positive)/P(healthy|healthy). 
- Note that we're interested in the posterior odds, i.e. how effective is the test at differentiating sick vs healthy patients? "
      ></orbit-prompt>
      <orbit-prompt
        question="If we design a covid-19 test, how do we determine the effectiveness of the test?"
        answer="
- Gather a random sample of people. 
- Gather data on how many of them are sick, and how many tested positive. 
- Measure the prior odds (ratio of sick to healthy) and relative likelihoods (how much more likely a sick patient gets a positive test compared to a healthy patient)
- Apply Bayes' Rule: Prior odds x relative likelihoods = posterior odds, which tells us how many positives are actually sick."
      ></orbit-prompt>
      <orbit-prompt
        cloze="If a hypothesis is a hundred times as likely to be false versus true, and then you see evidence five times more likely if the hypothesis is true versus false, you should update to believing the hypothesis is {twenty times as likely to be false as true}"
      ></orbit-prompt>
    </orbit-reviewarea>
  </body>
</html>

{{< /rawhtml >}}

# Making beliefs pay rent

This is a linkpost for [https://www.lesswrong.com/s/6xgy8XYEisLk3tCjH/p/a7n8GdKiAZRX86T5A](https://forum-bots.effectivealtruism.org/out?url=https%3A%2F%2Fwww.lesswrong.com%2Fs%2F6xgy8XYEisLk3tCjH%2Fp%2Fa7n8GdKiAZRX86T5A)

Thus begins the ancient parable:

_If a tree falls in a forest and no one hears it, does it make a sound? One says, “Yes it does, for it makes vibrations in the air.” Another says, “No it does not, for there is no auditory processing in any brain.”_

If there’s a foundational skill in the martial art of rationality, a mental stance on which all other technique rests, it might be this one: the ability to spot, inside your own head, psychological signs that you have a mental map of something, and signs that you don’t.

Suppose that, after a tree falls, the two arguers walk into the forest together. Will one expect to see the tree fallen to the right, and the other expect to see the tree fallen to the left? Suppose that before the tree falls, the two leave a sound recorder next to the tree. Would one, playing back the recorder, expect to hear something different from the other? Suppose they attach an electroencephalograph to any brain in the world; would one expect to see a different trace than the other?

Though the two argue, one saying “No,” and the other saying “Yes,” they do not anticipate any different experiences. The two think they have different models of the world, but they have no difference with respect to what they expect will _happen to_ them; their maps of the world do not diverge in any sensory detail.

It’s tempting to try to eliminate this mistake class by insisting that the only legitimate kind of belief is an anticipation of sensory experience. But the world does, in fact, contain much that is not sensed directly. We don’t see the atoms underlying the brick, but the atoms are in fact there. There is a floor beneath your feet, but you don’t _experience_ the floor directly; you see the light _reflected_ from the floor, or rather, you see what your retina and visual cortex have processed of that light. To infer the floor from seeing the floor is to step back into the unseen causes of experience. It may seem like a very short and direct step, but it is still a step.

You stand on top of a tall building, next to a grandfather clock with an hour, minute, and ticking second hand. In your hand is a bowling ball, and you drop it off the roof. On which tick of the clock will you hear the crash of the bowling ball hitting the ground?

To answer precisely, you must use beliefs like _Earth’s gravity is 9.8 meters per second per second,_ and _This building is around 120 meters tall._ These beliefs are not wordless anticipations of a sensory experience; they are verbal-ish, propositional. It probably does not exaggerate much to describe these two beliefs as sentences made out of words. But these two beliefs have an inferential _consequence_ that is a direct sensory anticipation—if the clock’s second hand is on the 12 numeral when you drop the ball, you anticipate seeing it on the 1 numeral when you hear the crash five seconds later. To anticipate sensory experiences as precisely as possible, we must process beliefs that are not anticipations of sensory experience.

It is a great strength of _Homo sapiens_ that we can, better than any other species in the world, learn to model the unseen. It is also one of our great weak points. Humans often believe in things that are not only unseen but unreal.

The same brain that builds a network of inferred causes behind sensory experience can also build a network of causes that is not connected to sensory experience, or poorly connected. Alchemists believed that phlogiston caused fire—we could simplistically model their minds by drawing a little node labeled “Phlogiston,” and an arrow from this node to their sensory experience of a crackling campfire—but this belief yielded no advance predictions; the link from phlogiston to experience was always configured after the experience, rather than constraining the experience in advance.

Or suppose your English professor teaches you that the famous writer Wulky Wilkinsen is actually a “retropositional author,” which you can tell because his books exhibit “alienated resublimation.” And perhaps your professor knows all this because their professor told them; but all they're able to say about resublimation is that it's characteristic of retropositional thought, and of retropositionality that it's marked by alienated resublimation. What does this mean you should expect from Wulky Wilkinsen’s books?

Nothing. The belief, if you can call it that, doesn’t connect to sensory experience at all. But you had better remember the propositional assertions that “Wulky Wilkinsen” has the “retropositionality” attribute and also the “alienated resublimation” attribute, so you can regurgitate them on the upcoming quiz. The two beliefs are connected to each other, though still not connected to any anticipated experience.

We can build up whole networks of beliefs that are connected only to each other—call these “floating” beliefs. It is a uniquely human flaw among animal species, a perversion of _Homo sapiens_ ’s ability to build more general and flexible belief networks.

The rationalist virtue of _empiricism_ consists of constantly asking which experiences our beliefs predict—or better yet, prohibit. Do you believe that phlogiston is the cause of fire? Then what do you expect to see happen, because of that? Do you believe that Wulky Wilkinsen is a retropositional author? Then what do you expect to see because of that? No, not “alienated resublimation”; _what experience will happen to you?_ Do you believe that if a tree falls in the forest, and no one hears it, it still makes a sound? Then what experience must therefore befall you?

It is even better to ask: what experience _must not_ happen to you? Do you believe that _Élan vital_ explains the mysterious aliveness of living beings? Then what does this belief _not_ allow to happen—what would definitely falsify this belief? A null answer means that your belief does not _constrain_ experience; it permits _anything_ to happen to you. It floats.

When you argue a seemingly factual question, always keep in mind which difference of anticipation you are arguing about. If you can’t find the difference of anticipation, you’re probably arguing about labels in your belief network—or even worse, floating beliefs, barnacles on your network. If you don’t know what experiences are implied by Wulky Wilkinsens writing being retropositional, you can go on arguing forever.

Above all, don’t ask what to believe—ask what to anticipate. Every question of belief should flow from a question of anticipation, and that question of anticipation should be the center of the inquiry. Every guess of belief should begin by flowing to a specific guess of anticipation, and should continue to pay rent in future anticipations. If a belief turns deadbeat, evict it.

_This work is licensed under a_[ _Creative Commons Attribution 4.0 International License_](https://creativecommons.org/licenses/by/4.0/) _._

{{< rawhtml >}}

<html>
  <head>
    <script type="module" src="https://js.withorbit.com/orbit-web-component.js"></script>
  </head>
  <body>
    <orbit-reviewarea color="blue">
      <orbit-prompt
        question="What does it mean for a belief to pay rent? "
        answer="
- A belief pays rent if it is connected to an anticipated experience. 
- e.g., 'Wulky Wilkinsen is a retropositional author because his books exhibit alienated resublimation.' tells you nothing abut what to expect from Wulky Wilkinsen's books. The belief doesn't pay rent. "
      ></orbit-prompt>
      <orbit-prompt
        cloze="Don’t ask what to believe, ask {what to anticipate}. Beliefs by themselves are useless, and become useful only when {they change your expectation of an external experience}  "
      ></orbit-prompt>
      <orbit-prompt
        question="Why do we have beliefs that don't pay rent? "
        answer="Humans have the unique ability to model that which is unseen. Unfortunately, this also allows us to believe in things that are unreal."
      ></orbit-prompt>
      <orbit-prompt
        question="What are 'floating' beliefs?"
        answer="
-Whole networks of beliefs that are connected only to each other, but doesn't actually connect to anything external, i.e. doesn't affect what we experience. 
-e.g. 'Wulky Wilkinsen is a retropositional author because his books exhibit alienated resublimation.' doesn't tell us about what to expect from Wulky Wilkinsen's writing "
      ></orbit-prompt>
    </orbit-reviewarea>
  </body>
</html>

{{< /rawhtml >}}

# What is evidence?

This is a linkpost for [https://www.lesswrong.com/s/6xgy8XYEisLk3tCjH/p/6s3xABaXKPdFwA3FS](https://forum-bots.effectivealtruism.org/out?url=https%3A%2F%2Fwww.lesswrong.com%2Fs%2F6xgy8XYEisLk3tCjH%2Fp%2F6s3xABaXKPdFwA3FS)

> The sentence “snow is white” is _true_ if and only if snow is white.
>
> —Alfred Tarski

> To say of what is, that it is, or of what is not, that it is not, is _true_.
>
> —Aristotle, _Metaphysics IV_

Walking along the street, your shoelaces come untied. Shortly thereafter, for some odd reason, you start _believing_ your shoelaces are untied. Light leaves the Sun and strikes your shoelaces and bounces off; some photons enter the pupils of your eyes and strike your retina; the energy of the photons triggers neural impulses; the neural impulses are transmitted to the visual-processing areas of the brain; and there the optical information is processed and reconstructed into a 3D model that is recognized as an untied shoelace. There is a sequence of events, a chain of cause and effect, within the world and your brain, by which you end up believing what you believe. The final outcome of the process is a state of _mind_ which mirrors the state of your actual _shoelaces_.

What is _evidence?_ It is an event entangled, by links of cause and effect, with whatever you want to know about. If the target of your inquiry is your shoelaces, for example, then the light entering your pupils is evidence entangled with your shoelaces. This should not be confused with the technical sense of “entanglement” used in physics—here I’m just talking about “entanglement” in the sense of two things that end up in correlated states because of the links of cause and effect between them.

Not every influence creates the kind of “entanglement” required for evidence. It’s no help to have a machine that beeps when you enter winning lottery numbers, if the machine _also_ beeps when you enter _losing_ lottery numbers. The light reflected from your shoes would not be useful evidence about your shoelaces, if the photons ended up in the same physical state whether your shoelaces were tied or untied.

To say it abstractly: For an event to be _evidence about_ a target of inquiry, it has to happen _differently_ in a way that’s entangled with the _different_ possible states of the target. (To say it technically: There has to be Shannon mutual information between the evidential event and the target of inquiry, relative to your current state of uncertainty about both of them.)

Entanglement can be contagious when processed correctly, which is why you need eyes and a brain. If photons reflect off your shoelaces and hit a rock, the rock won’t change much. The rock won’t reflect the shoelaces in any helpful way; it won’t be detectably different depending on whether your shoelaces were tied or untied. This is why rocks are not useful witnesses in court. A photographic film will contract shoelace-entanglement from the incoming photons, so that the photo can itself act as evidence. If your eyes and brain work correctly, _you_ will become tangled up with your own shoelaces.

This is why rationalists put such a heavy premium on the paradoxical-seeming claim that a belief is only really worthwhile if you could, in principle, be persuaded to believe otherwise. If your retina ended up in the same state regardless of what light entered it, you would be blind. Some belief systems, in a rather obvious trick to reinforce themselves, say that certain beliefs are only really worthwhile if you believe them _unconditionally_ —no matter what you see, no matter what you think. Your brain is supposed to end up in the same state regardless. Hence the phrase, “blind faith.” If what you believe doesn’t depend on what you see, you’ve been blinded as effectively as by poking out your eyeballs.

If your eyes and brain work correctly, your beliefs will end up entangled with the facts. _Rational thought produces beliefs which are themselves evidence._

If your tongue speaks truly, your rational beliefs, which are themselves evidence, can act as evidence for someone else. Entanglement can be transmitted through chains of cause and effect—and if you speak, and another hears, that too is cause and effect. When you say “My shoelaces are untied” over a cellphone, you’re sharing your entanglement with your shoelaces with a friend.

Therefore rational beliefs are contagious, among honest folk who believe each other to be honest. And it’s why a claim that your beliefs are _not_ contagious—that you believe for private reasons which are not transmissible—is so suspicious. If your beliefs are entangled with reality, they _should_ be contagious among honest folk.

If your model of reality suggests that the outputs of your thought processes should _not_ be contagious to others, then your model says that your beliefs are not themselves evidence, meaning they are not entangled with reality. You should apply a reflective correction, and stop believing.

Indeed, if you _feel_ , on a _gut_ level, what this all _means_ , you will _automatically_ stop believing. Because “my belief is not entangled with reality” _means_ “my belief is not accurate.” As soon as you stop believing “ ‘snow is white’ is true,” you should (automatically!) stop believing “snow is white,” or something is very wrong.

So try to explain why the kind of thought processes you use systematically produce beliefs that mirror reality. Explain why you think you’re rational. Why you think that, using thought processes like the ones you use, minds will end up believing “snow is white” if and only if snow is white. If you _don’t_ believe that the outputs of your thought processes are entangled with reality, why believe the outputs of your thought processes? It’s the same thing, or it should be.

_This work is licensed under a_[ _Creative Commons Attribution 4.0 International License_](https://creativecommons.org/licenses/by/4.0/) _._

{{< rawhtml >}}

<html>
  <head>
    <script type="module" src="https://js.withorbit.com/orbit-web-component.js"></script>
  </head>
  <body>
    <orbit-reviewarea color="blue">
      <orbit-prompt
        question="A belief is only really worthwhile if you could, in principle, be persuaded to believe otherwise. Why?"
        answer="
- If your retina ended up in the same state regardless of what light entered it, you would be blind. 
- If what you believe in doesn't depend on what you see, you're effectively blind. 
- If your eyes and brain work correctly, your beliefs will end up entangled with the facts. Rational thought produces beliefs which are themselves evidence."
      ></orbit-prompt>
      <orbit-prompt
        question="What does it mean if you have a belief in private, which you think won't be convincing to other people?"
        answer="
- If you speak honestly, your rational beliefs, which are themselves evidence, can act as evidence for someone else. 
- Hence, beliefs which are consistent with reality are contagious among honest folk. 
- This means it's suspicious when you have a belief in private, which you think won't be convincing to other people"
      ></orbit-prompt>
    </orbit-reviewarea>
  </body>
</html>

{{< /rawhtml >}}

# Notes on Effective Altruism

This is a linkpost for [https://michaelnotebook.com/eanotes/](https://forum-bots.effectivealtruism.org/out?url=https%3A%2F%2Fmichaelnotebook.com%2Feanotes%2F)

Michael Nielsen

Initial release: June 2, 2022

This release: June 3, 2022 (minor modifications)

_Long and rough notes on Effective Altruism (EA). Written to help me get to the bottom of several questions: what do I like and think is important about EA? Why do I find the mindset so foreign? Why am I not an EA? And to start me thinking about: what do alternatives to EA look like? The notes are not aimed at effective altruists, though they may perhaps be of interest to EA-adjacent people. Thoughtful, informed comments and corrections welcome (especially detailed, specific corrections!) - see the comment area at the bottom._

_"Using evidence and reason to figure out how to benefit others as much as possible, and taking action on that basis"_ : that's the idea at the foundation of the Effective Altruism (EA) ideology and movement.[^1] Over the past two decades it has gone from being an idea batted about by a few moral philosophers to being a core part of the life philosophy of thousands or tens of thousands of people, including several of the world's most powerful and wealthy individuals. These are my rough working notes on EA. The notes are long and quickly written: disorganized rough thinking, not a polished essay.

I wrote the notes for a few reasons. One is purely social: many of my friends have strong opinions on EA (some pro-, some anti-, others more neutral). Another is a sense that EA is important as a social movement and (perhaps) as a set of ideas. It's significant that so many smart, idealistic teenagers and 20-somethings respond so strongly to EA. Many report radically changing their lives: changing careers; changing their day-to-day behavior; committing to give a large proportion of their income to charities they describe as "effective". EAs[^2] also share a lot of unusual language and ways of seeing the world, much of it adapted from welfare economics and moral philosophy.

It's tempting to dismiss this as all "just" fashion, or as a consequence of the (meteoric) rise in funding to EA. But I don't buy it. Many EAs are extraordinarily sincere, and have found tremendous conviction and meaning in EA. It's doing something very important for them, something well beyond being a niche fashion.

When I first learned about EA, my instinctive and poorly thought through response was fairly negative. I've often half-joked that I'm an ineffective altruist, or a chaotic altruist. I like to describe myself as a mutilitarian, using the Zen Buddhist "mu" as my utility function (i.e., a denial of the idea). And yet upon deeper inspection these are cheap dismissals.

In 2011 an EA friend of mine went under the knife, donating a kidney to a stranger. He explained to me that he:

> came across some stats on how safe it was to donate and it totally changed my picture. I thought, 1/3,000 risk of death in surgery is like sacrificing yourself to save 3,000 people. I want to be the kind of person who'd do that, and you just have to follow these few steps.

I have EA friends who donate a large fraction of their income to charitable causes. In some cases it's _all_ their income above some fairly low (by rich developed world standards) threshold, say $30k. In some cases it seems plausible that their personal donations are responsible for saving dozens of lives, helping lift many people out of poverty, and preventing many debilitating diseases, often in some of the poorest and most underserved parts of the world. Some of those friends have directly helped save many lives. That's a simple sentence, but an extraordinary one, so I'll repeat it: they've directly helped save many lives.

I'm in stunned awe of all this. And feel a little sheepish about my jokes about ineffective altruism, and grateful that EA friends put up with me. I've tried to live a life matching my personal skills and interests to things which are good for the world. I hope I've done some genuine good, while also enjoying my life. But I've never directly saved a life, as far as I know. I do not think I _could_ donate a kidney: it would violate my sense of somatic integrity too much. At a personal level, I love the sincerity and genuine goodness of my EA and near-EA friends. I simply _feel_ more wholesome after spending time with them. I'm often more honest; I'm sometimes kinder or more open-minded. These are all very good things.

What follows, then, is a collection of observations about EA. It's in part an appreciation: to critique EA you must also understand some of what is good about it. And there is a great deal that can be learned from it by other ideologies. But I'll also dig down and try to understand what bothers me about EA, what I think is wrong, and how I think EA might fruitfully be modified.

Something that's missing from the notes: a direct, first-person account of the good that EA does. I have some reflected sense of this from friends, but wish I knew more. It's impossible to genuinely appreciate EA without it. Malaria bed nets, direct cash transfers, de-worming _etc_ aren't abstractions: they are, in fact, an enormous real world event, making a huge difference in the lives of many people. And that's missing here, just due to my ignorance. Try to keep the fact of this in mind as you read; I've tried to do so as I write.

A caution: I make a lot of generalizations about "what EA does". But EA is not monolithic. This makes it difficult to write without inserting lots of qualifiers. I could do it by saying "Most EAs believe", or quoting leading EAs, and so on. I've instead (mostly) opted to use the general language, with the implicit understanding that there are often EAs who disagree with that particular piece. However, I've tried to note when there is widespread disagreement about a point among the EA community.

I began the notes with a widely-used description of EA, taken from philosopher Will MacAskill, one of the founders of EA: "Using evidence and reason to figure out how to benefit others as much as possible, and taking action on that basis". In practice, I've often heard this abbreviated along the lines of: "Using evidence and reason to do the most good possible". I'll usually use the latter as a shorthand for what EA is about, but keeping in mind the longer description. One caveat about both these descriptions: note that they are inherently maximizing, "benefit others _as much_ as possible", "do the _most_ good possible". In fact, many EAs advocate backing away quite a bit from this maximizing frame. As a result, it makes sense to think of different "strengths" of EA, according to how much a person accepts this maximization approach (or not). We'll return to this, as it's a significant issue not settled by the EA community. And when I use "the most good" framing, it's with the implicit caveat that many EAs back off from "most" in practice.

## EA as a source of moral invention[^3]

I mentioned above my friend who donated a kidney in 2011. The moral philosopher Peter Singer, one of the originators of many ideas in EA, describes his amazement[^4] at learning (in 2004) the story of Zell Kravinsky, a wealthy real estate investor who had donated almost his entire fortune of $45 million, living on $60 thousand a year. But there's something even more remarkable. At first sight it will look very similar to my friend's kidney donation story above. But it's different in an important way:

> He still did not think he had done enough to help others, so he arranged with a nearby hospital to donate a kidney to a stranger… Quoting scientific studies that show the risk of dying as a result of making a kidney donation to be only 1 in 4,000, he says that not making the donation would have meant he valued his life at 4,000 times that of a stranger, a valuation he finds totally unjustified.

As extraordinary as my friend's generosity was, there is something further still going on here. Kravinsky's act is one of moral imagination, to even consider donating a kidney, and then of moral conviction, to follow through. This is an astonishing act of moral invention: someone (presumably Kravinsky) was the first to both imagine doing this, and then to actually do it. That moral invention then inspired others to do the same. It actually expanded the range of human moral experience, which others can learn from and then emulate. In this sense a person like Kravinsky can be thought of as a moral pioneer or moral psychonaut[^5], inventing new forms of moral experience.

Of course, such moral pioneers don't only come from EA. Far from it! They are at the foundation of our civilization. Many of my personal heroes are moral pioneers, including the author of the Sermon on the Mount[^6], the abolitionist movement, the suffragettes and feminist movement, Martin Luther King and other leaders in the civil rights movement. All these (and many more) engaged in acts of moral imagination that expanded the range of moral experience available to the rest of us to emulate. We may not always agree with them: I don't know, for instance, that I agree with Peter Singer's views on the rights of animals. Singer may be wrong on that. But it's valuable nonetheless as an act of moral invention expanding our potential range of moral experience.

One of the things that's interesting about EA is that it has encouraged many moral pioneers: people willing to rethink fundamental moral questions, and (sometimes) to expand the range of our moral experience. Questions they've seriously asked (and in some cases, acted on the answers): "What if animal lives truly mattered?" "What if a life on the other side of the world mattered just as much as that of a child drowning before your eyes?" "What if an intelligent machine's 'life' mattered just as much as a human being's?" "How should we value the life of a human being living a million years from now?" By taking these questions seriously they can expand our moral horizons.

There's a dark flipside to moral pioneering, memorably pointed out by the political philosopher Hannah Arendt in _Eichmann in Jerusalem_ , her account of the trial of the Nazi war criminal Adolf Eichmann. In Arendt's account, the Nazi's were (in some sense) also moral pioneers, inventing new kinds of crime, which then expanded the likely range of future crime:

> Nothing is more pernicious to an understanding of these new crimes, or stands more in the way of the emergence of an international penal code that could take care of them, than the common illusion that the crime of murder and the crime of genocide are essentially the same, and that the latter therefore is “no new crime properly speaking.” The point of the latter is that an altogether different order is broken and an altogether different community is violated… It is in the very nature of things human that every act that has once made its appearance and has been recorded in the history of mankind stays with mankind as a potentiality long after its actuality has become a thing of the past. No punishment has ever possessed enough power of deterrence to prevent the commission of crimes. On the contrary, whatever the punishment, once a specific crime has appeared for the first time, its reappearance is more likely than its initial emergence could ever have been.

Moral reasoning, if taken seriously and acted upon, is of the utmost concern, in part because there is a danger of terrible mistakes. The Nazi example is overly dramatic: for one thing, I find it hard to believe that the originators of Nazi ideas didn't realize that these were deeply evil acts. But a more everyday example, and one which should give any ideology pause, is overly self-righteous people, acting in what they "know" is a good cause, but in fact doing harm. I'm cautiously enthusiastic about EA's moral pioneering. But it is potentially a minefield, something to also be cautious about.

## EA judo: strong critique of any particular "most good" strategy improves EA, it doesn't discredit it

One of the most common lines of "attack" on EA is to disagree with common EA notions of what it means to do the most good. "Are you an EA?" "Oh, those are the people who think you need to give money for malaria bed nets [or AI safety, or de-worming, /etc etc/], but that's wrong because […]." Or: "Will MacAskill says that EAs should consider earning-to-give, but that's wrong because […]". Or: "Science and social justice and creativity and [etc etc etc] are much harder to measure than things like QALYs, so EAs tend to undervalue or ignore them." Or: "EAs are rather credulous[^7] about the value of RCTs and meta-analysis, you should instead […]". Or: "Look, you can directly increase QALYs all you want, it won't shift you from a low-growth to a high-growth economy. The two are at different levels of causal abstraction".

These statements may or may not be true. Regardless, none of them is a fundamental critique of EA. Rather, they're examples of EA thinking: you're actually participating in the EA project when you make such comments. EAs argue vociferously all the time about what it means to do the most good. What unites them is that they agree they should "use evidence and reason to figure out how to do the most good"; if you disagree with prevailing EA notions of most good, and have evidence to contribute, then you're providing grist for the mill driving improvement in EA understanding of what is good.

In any case, this kind of "critique" accounts for at least half – probably more – of the external criticism of EA I've heard. Most external critics who think they're critiquing EA are critiquing a mirage. In this sense, EA has a huge surface area which can only be improved by critique, not weakened. I think of the pattern as _EA judo_. And you see it often in discussions with "EA critics". A pleasant, informative example is EA Rob Wiblin [interviewing](https://80000hours.org/podcast/episodes/russ-roberts-effective-altruism-empirical-research-utilitarianism/) Russ Roberts, who presents himself as disagreeing with EA. But through (most of) the interview, Roberts tacitly accepts the basic ideas of EA, while disagreeing with particular instantiations. And Wiblin practices EA judo, over and over, turning it into a very typical EA-type debate over how to do the most good. It's very interesting and both participants are very thoughtful, but it's not really a debate about the merits of EA.

This is, to me, one of the most attractive and powerful features of EA. It makes it very different to most ideologies, which are often rather static. EA is, in some sense, an attempt to do for the question "what is the good?" what science has done for the question "how does the world work?". Instead of providing an answer it is developing a community that aims to continually improve the answer.[^8]

Because of this, it's worth separating EA-in-practice (a social movement) from EA-the-intellectual-project. If you wish to get at fundamental issues, you ultimately need to focus on the latter, not just the former. As I said: many critiques of EA-in-practice are just part of the core engine of improvement. This does not mean, however, that it's not worth spending time critiquing the surface area of EA-in-practice. "By their fruits ye shall know them" holds for intellectual principles, not just people. If a set of principles throws off a lot of rotten fruit, it's a sign of something wrong with the principles, a _reductio ad absurdum_. You've probably heard communists and libertarians defend failed communist and free-market experiments by saying: "It wasn't a true communist / free-market experiment". Sometimes they have a point. But if the pattern persists, if the fundamental principles aren't resilient or need a lot of special pleading, it means those principles have something badly wrong with them.

Put another way: when EA judo is practiced too much, it's worth looking for more fundamental problems. The basic form of EA judo is: "Look, disagreement over what is good does nothing directly to touch EA. Indeed, such disagreement is the engine driving improvement in our notion of what is good." This is perhaps true in some God's-eye, omniscient, in-principle philosopher's sense. But EA community and organizations are subject to fashion and power games and shortcomings and biases, just like every other community and organization. Good intentions alone aren't enough to ensure effective decisions about effectiveness.[^9] And the reason many people are bothered by EA is not that they think it's a bad idea to "do good better". But rather that they doubt the ability of EA institutions and community to live up to the aspirations.

These critiques can come from many directions. From people interested in identity politics I've heard: "Look, many of these EA organizations are being run by powerful white men, reproducing existing power structures, biased toward technocratic capitalism and the status quo, and ignoring many of the things which really matter." From libertarians I've heard: "Look, EA is just leftist collective utilitarianism. It centralizes decision-making too much, and ignores both price signals and the immense power that comes from having lots of people working in their own self-interest, albeit inside a system designed so that self-interest (often) helps everyone collectively.[^10][^11] From startup people and inventors I've heard: "Aren't EAs just working on public goods? If you want to do the most good, why not work on a startup instead? We can just invent and scale new technology (or new ideas) to improve the world![^11](https://michaelnotebook.com/eanotes/#fn11)." From people familiar with the pathologies of aging organizations and communities, I've heard: "Look, any movement which grows rapidly will also start to decay. It will become dominated by ambitious careerists and principal agent problems, and lose the sincerity and agility that characterized the pioneers and early adopters[^12][^13]

All these critiques have some truth; they also have significant issues. Without getting into those weeds, the immediate point is that they all look like "merely" practical problems, for which EA judo may be practiced: "If we're not doing that right, we shall improve, we simply need you to provide evidence and a better alternative". But the organizational patterns are so strong that these criticisms seem more in-principle to me. Again: if your social movement "works in principle" but practical implementation has too many problems, then it's not really working in principle, either. The quality "we are able to do this effectively in practice" is an important (implicit) in-principle quality.

## "Bad" EAs, caught in a misery trap

Let's go back to the EA principle: "Using evidence and careful reasoning to do the most good possible". It's a very attractive principle in many ways. It's extremely clear. It's highly orienting and meaning-giving, especially if embedded in a social and organizational context that makes convincing recommendations about how to do the most good. Those recommendations don't need to be perfect: they need merely be better than you expect you could do in most other community contexts.

Part of the attraction of the principle is that it takes away choice. One great achievement of modernity is to give people more and more choice, until they get to choose (seemingly) everything.[^14] But vast choice is also bewildering and challenging. Much of the power of EA (and of many ideologies) is to take away much of that choice, saying: no, you have a duty[^15] to do the most good you can in the world. Furthermore, EA provides institutions and a community which helps guide how you do that good. It thus provides orientation and meaning and a narrative for _why_ you're doing what you're doing.

On Twitter, ex-EA Nick Cammarata made the following [comment](https://twitter.com/nickcammarata/status/1528005615095799808), which I've heard echoed one-on-one with many EAs and ex-EAs:

> my inner voice in early 2016 would automatically convert all money I spent (eg on dinner) to a fractional “death counter” of lives in expectation I could have saved if I’d donated it to good charities. Most EAs I mentioned that to at the time were like ah yeah seems reasonable

Or consider the following [remarkable exchange](https://twitter.com/TheDrewRat/status/1525558537467969536) on Twitter, between a non-EA and an EA:

> "the optimal amount of optimal charity is not 100%"
>
> "But good EAs take this into account"
>
> "Yes but bad EAs get caught in a misery trap"
>
> "True, but that's not a flaw of EA, that's a flaw of those people."

Or consider the following passage in Peter Singer's book "The Most Good You Can Do":

> When [pioneering EA] Julia [Wise] was young she felt so strongly that her choice to donate or not donate meant the difference between someone else living or dying that she decided it would be immoral for her to have children. They would take too much of her time and money. She told her father of her decision, and he replied. “It doesn’t sound like this lifestyle is going to make you happy,” to which she responded, “My happiness is not the point.” Later, when she was with [her husband] Jeff, she realized that her father was right. Her decision not to have a child was making her miserable. She talked to Jeff, and they decided they could afford to raise a child and still give plenty. The fact that Julia could look forward to being a parent renewed her sense of excitement about the future. She suspects that her satisfaction with her life makes her of more use to the world than she would be if she were “a broken-down altruist.”
>
> Everyone has boundaries. If you find yourself doing something that makes you bitter, it is time to reconsider. Is it possible for you to become more positive about it? If not, is it really for the best, all things considered?
>
> …
>
> Julia admits to making mistakes. When shopping, she would constantly ask herself, “Do I need this ice cream as much as a woman living in poverty elsewhere in the world needs to get her child vaccinated?” That made grocery shopping a maddening experience, so she and Jeff made a decision about what they would give away over the next six months and then drew up a budget based on what was left. Within that budget, they regarded the money as theirs, to spend on themselves. Now Julia doesn’t scrimp on ice cream because, as she told the class, “Ice cream is really important to my happiness.”
>
> …
>
> Julia’s and Jeff’s decision to have a child shows that they drew a line beyond which they would not let the goal of maximizing their giving prevent them from having something very important to them. Bernadette Young, Toby Ord’s partner, has described their decision to have a child in a similar way: “I’m happy donating 50 percent of my income over my life, but if I also chose not to have a child simply to raise that amount to 55 percent, then that final 5 percent would cost me more than all the rest. … I’m deciding to meet a major psychological need and to plan a life I can continue to live in the long term.” Neither Julia nor Bernadette is unusual in experiencing the inability to have a child—for whatever reason—as deeply distressing. Having a child undoubtedly takes both money and time, but against this, Bernadette points out, effective altruists can reasonably hope that having a child will benefit the world. Both cognitive abilities and characteristics like empathy have a significant inherited component, and we can also expect that children will be influenced by the values their parents hold and practice in their daily lives. Although there can be no certainty that the children of effective altruists will, over their lifetimes, do more good than harm, there is a reasonable probability that they will, and this helps to offset the extra costs of raising them. We can put it another way: If all those who are concerned to do the most good decide not to have children, while those who do not care about anyone else continue to have children, can we really expect that, a few generations on, the world will be a better place than it would have been if those who care about others had had children?

There is a related attitude toward the arts common in EA. Singer is blunt about this: you can't really justify the arts:

> Can promoting the arts be part of “the most good you can do”?
>
> In a world that had overcome extreme poverty and other major problems that face us now, promoting the arts would be a worthy goal. In the world in which we live, however, for reasons that will be explored in chapter 11, donating to opera houses and museums isn’t likely to be doing the most good you can.

I've heard several EAs say they know multiple EAs who get very down or even depressed because they feel they're not having enough impact on the world. As a purely intellectual project it's fascinating to start from a principle like "use reason and evidence to figure out how do the most good in the world" and try to derive things like "care for children" or "enjoy eating ice cream" or "engage in or support the arts[^16] as special cases of the overarching principle. But while that's intellectually interesting, as a direct guide to living it's a terrible mistake. The reason to care for children ( _etc_ ) isn't because it helps you do the most good. It's because _we're absolutely supposed to care for our children_. The reason art and music and ice cream matter aren't because they help you do the most good. It's because we're human beings – not soulless automatons – who respond in ways we don't entirely understand to things whose impact on our _selves_ we do not and cannot fully apprehend.

Now, the pattern that's been chosen by EA has been to insert escape clauses. Many talk about having a "warm fuzzies" budget for "ineffective" giving that simply makes them feel good. And they carve out _ad hoc_ extension clauses like the one about having children or setting aside an ice cream budget or a dinner budget, and so on.[^17] It all seems to me like special pleading at a frequency which suggests something amiss. You've started from a single overarching principle that seems tremendously attractive. But now you've either got to accept all the consequences, and make yourself miserable. Or you have to start, as an individual, grafting on _ad hoc_ extension clauses. And that turns out to be terribly stressful in its own right. You have thoughtful people like Nick Cammarata in a spin over their dinner. It's not the dinner that's the problem: it's the fact that Cammarata is in a spin. Or Julia Wise, deciding whether to have ice cream – or children.

And it's not surprising: on one side you have a very clear, very powerful principle and superhuman entities (EA organizations + the collective community) sending extremely clear and compelling messages about how to do the most good. But it's an individual level at which people are trying to discover and set boundaries. It's no wonder it's stressful.

This is a really big problem for EA. When you have people taking seriously such an overarching principle, you end up with stressed, nervous people, people anxious that they are living wrongly. The correct critique of this situation isn't the one Singer makes: that it prevents them from doing the most good. The critique is that _it is the wrong way to live_. They need a different foundation for their life. It may be that it includes some variation of that principle, as a _small part_ of a much larger and very well developed life philosophy. But it must be sharply tempered by some other principle or principles; those principles must have the same kind of clarity and force; it must be apparent how all the parts fit together, so the "most good" principle is firmly bounded by the other principles. And it may well be that the balancing needs to be (in part) delegated to superhuman institutions, that it's too much to ask of most individuals without causing them tremendous stress. But if "the most good" is used as the foundation tentpole for a life philosophy, onto which you _ad hoc_ graft additional clauses, that seems to me a recipe for problems.

An alternate solution, and the one that has, I believe, been adopted by many EAs, has been a form of weak-EA. Strong-EA takes "do the most good you can do" extremely seriously as a central aspect of a life philosophy. Weak-EA uses that principle more as guidance. Donate 1% of your income. Donate 10% of your income, provided that doesn't cause you hardship. Be thoughtful about the impact your work has on the world, and consult many different sources. These are all good things to do! The critique of this form is that it's fine and good, but also hard to distinguish from the common pre-existing notion many people have, "live well, and try to do some good in the world". As Amia Srinivasan puts it[^18]:

> But the more uncertain the figures, the less useful the calculation, and the more we end up relying on a commonsense understanding of what’s worth doing. Do we really need a sophisticated model to tell us that we shouldn’t deal in subprime mortgages [/ed: yes/], or that the American prison system needs fixing, or that it might be worthwhile going into electoral politics if you can be confident you aren’t doing it solely out of self-interest? The more complex the problem effective altruism tries to address – that is, the more deeply it engages with the world as a political entity – the less distinctive its contribution becomes. Effective altruists, like everyone else, come up against the fact that the world is messy, and like everyone else who wants to make it better they must do what strikes them as best, without any final sense of what that might be or any guarantee that they’re getting it right.
>
> More worrying than the model’s inability to tell us anything very useful once we move outside the circumscribed realm of controlled intervention is its susceptibility to being used to tell us exactly what we want to hear.
>
> …
>
> Effective altruism takes up the spirit of Singer’s argument but shields us from the full blast of its conclusion… Instead of downgrading our lives to subsistence levels, we are encouraged to start with the traditional tithe of 10 per cent, then do a bit more each year. Thus effective altruism dodges one of the standard objections to utilitarianism: that it asks too much of us. But it isn’t clear how the dodge is supposed to work. MacAskill tells us that effective altruists – like utilitarians – are committed to doing the most good possible, but he also tells us that it’s OK to enjoy a ‘cushy lifestyle’, so long as you’re donating a lot to charity. Either effective altruism, like utilitarianism, demands that we do the most good possible, or it asks merely that we try to make things better. The first thought is genuinely radical, requiring us to overhaul our daily lives in ways unimaginable to most. (Singer repeats his call for precisely such an overhaul in his recent book The Most Good You Can Do, and Larissa MacFarquhar’s Strangers Drowning is a set of portraits of ‘extreme altruists’ who have answered the call.) The second thought – that we try to make things better – is shared by every plausible moral system and every decent person. If effective altruism is simply in the business of getting us to be more effective when we try to help others, then it’s hard to object to it. But in that case it’s also hard to see what it’s offering in the way of fresh moral insight, still less how it could be the last social movement we’ll ever need.

There's much I agree with in that excerpt. But I think there's a pretty good retort to Srinivasan's final comment: "in that case it's also hard to see what [EA is] offering in the way of fresh moral insight, still less how it could be the last social movement we'll ever need." Now, if it were a purely intellectual argument, I'd agree with her. But: the EAs have actually gone and done it: created institutions that are actually _centered_ around the idea. And that's valuable and an innovation.

## Internal criticisms of the EA principle

Let's return again to the EA principle: "Effective altruism means using evidence and reason to do the most good possible in the world." I've discussed some in-practice symptoms of implicit issues with this principle; I've also discussed problems setting boundaries on the principle. Let's shift to directly critique the principle itself.

Many of the issues are just the standard ones people use to attack moral utilitarianism. Unfortunately, I am far from an expert on these arguments. So I'll just very briefly state my own sense: "good" isn't fungible, and so any quantification is an oversimplification. Indeed, not just an oversimplification: it is sometimes downright wrong and badly misleading. Certainly, such quantification is often a practical convenience when making tradeoffs; it may also be useful for making suggestive (but not dispositive) moral arguments. But it has no fundamental status. As a result, notions like "increasing good" or "most good" are useful conveniences, but it's a bad mistake to treat them as fundamental. Furthermore, the notion of a single "the" good is also suspect. There are many plural goods, which are fundamentally immeasurable and incommensurate and cannot be combined.

I find these attacks compelling. As a practical convenience and as a generative tool, utilitarianism is useful. But I'm not a utilitarian as a fundamental fact about the world.

(Tangentially: it is interesting to ponder what truth there is in past UN Secretary-General Dag Hammarskjöld's statement that: "It is more noble to give yourself completely to one individual than to labor diligently for the salvation of the masses." This is, to put it mildly, not an EA point of view. And yet I believe it has some considerable truth to it.)

Less centrally, the part of the principle about "using evidence and reason" is striking. There is ongoing change in what humanity means by "evidence and reason", with occasional sharp jumps. Indeed, many of humanity's greatest achievements have been radical changes in what we mean by evidence and reason. 11th century standards of evidence and reason are very different from today's; I expect 31st century standards will be very different again. Of course, this point can be addressed with some minor patching. It can perhaps be dealt with by changing the principle to: "our best current standards of evidence and reasoning to do the most good possible in the world", to emphasize awareness of the fact that these things do change.

## Miscellanea

These are four subjects I'd like to treat at length, but decided to leave as outside the scope of the current notes. I want to just mention them here, at the risk of confusing the issue with a too-easily-misinterpreted brief account. All four subjects really need a lengthy account:

**Illegibility:** A common argument against EA is that it undervalues illegible activity. The typical EA response is another form of EA judo, the bureaucrat's war cry: let's make it legible![^19] We'll just figure out how much good early-stage science / a children's birthday party / new types of sculpture really do. And yet the more forms of activity we make legible, the more the penumbra of illegibility changes and grows: and much of the deepest creative work and the most transformative life changes are made by people in that penumbra.[^20] In many types of work, when the outcomes you get are the outcomes you want – indeed, when they're outcomes you can even understand – you've missed an enormous opportunity. "Evidence and reason" begin to break down, by definition, in the penumbra of illegibility. I also suspect that as a basic personality trait I am happiest in that illegible penumbra, and this is why I've had so much trouble grokking EA: it feels like a foreign language, where there's some starting assumption I just don't get. Conversely, when talking about illegibility with EAs they often look at me like I've grown an extra head. They view illegibility as something to be conquered and minimized; I view it as a fundamental, immovable fact about the way the world works. Indeed, the more illegibility you conquer, the more illegibility springs up, and the greater the need for such work.

**"EA-is-a-cult / EA-is-a-religion:"** These are common statements, usually used as part of critical attacks. I believe they're often used either thoughtlessly or disingenuously, relying on the perjorative connotations of "cult". It's true, EA-the-movement does have some overlapping features with cults; so does mountaineering, appreciation of the music of Bob Dylan, and many other activities. The substantive part that is worth paying attention to is: as with any strong, attractive, growing movement, EA may attract charismatic scoundrels looking to take advantage of others. That is a genuine issue. And it's well worth guarding against. But I don't think EA is unusually prone to it when compared to any other strong ideology.

**Long-termism / x-risk / AI safety:** This requires a set of notes of its own. I'm broadly positive about work on x-risk in general; I admire, for instance, Toby Ord's recent book about it. I think little of most work being done on AI safety, although there are a few people doing good work, and adjacent work (on fairness, interpretability, explainability, _etc_ ) that is very valuable.

**Vibe and aesthetics:** A friend points out that EA has a very particular and quite unusual vibe, very different from many other cultures. This seems both true and interesting. I'm not sure what to make of it. This is also true of aesthetic: EA tends toward a very instrumental and particular aesthetic. Interesting to consider in the frame of art: historically, primarily instrumental approaches to art nearly always result in bad art. It'd be lovely to see an EA arts movement that sprang from something non-instrumental!

## Summing up

EA is an inspiring meaning-giving life philosophy. It invites people to strongly connect with some notion of a greater good, to contribute to that greater good, and to make it central in their life. EA-in-practice has done a remarkable amount of direct good in the world, making people's lives better. It's excellent to have the conversational frame of "how to do the most good" readily available and presumptively of value. EA-in-practice also provides a strong community and sense of belonging and shared values for many people. As moral pioneers EA is providing a remarkable set of new public goods.

All this makes EA attractive as a life philosophy, providing orientation and meaning and a clear and powerful core, with supporting institutions. Unfortunately, strong-EA is a poor life philosophy, with poor boundaries that may cause great distress to people, and underserves core needs. EA-in-practice is too centralized, too focused on absolute advantage; the market often does a far better job of providing certain kinds of private (or privatizable) good. However, EA-in-practice likely does a better job of providing certain kinds of public good than do many existing institutions. EA relies overmuch on online charisma: flashy but insubstantial discussion of topics like the simulation argument and x-risk and AI safety have a tendency to dominate conversation, rather than more substantial work. (This does not mean there aren't good discussions of such topics.) EA-in-practice is too allied with existing systems of power, and does little to question or change them. Appropriating the term "effective" is clever marketing and movement-building, but intellectually disingenuous. EA views illegibility as a problem to be solved, not as a fundamental condition. Because of this it does poorly on certain kinds of creative and aesthetic work. Moral utilitarianism is a useful but limited practical tool, mistaking quantification that is useful for making tradeoffs with a fundamental fact about the world.

I've strongly criticized EA in these notes. But I haven't provided a clearly and forcefully articulated alternative. It amounts to saying that someone's diet of ice cream and chocolate bars isn't ideal, without providing better food; it may be correct, but isn't immediately actionable. Given the tremendous emotional need people have for a powerful meaning-giving system, I don't expect it to have much impact on those people. It's too easy to arm-wave the issues away, or ignore them as things which can be resolved by grafting some exception clauses on. But writing the notes both helped me better understand why I'm not EA, and also why I think the EA principle would, with very considerable modification, make a valuable part of some larger life philosophy. But I don't yet understand what that life philosophy is.

## Elsewhere

I suggest looking at [criticism of effective altruism](https://forum.effectivealtruism.org/topics/criticism-of-effective-altruism) and these [four categories of EA critiques](https://forum.effectivealtruism.org/posts/HzyYoLK2ERTnDmrjB/four-categories-of-effective-altruism-critiques). After I finished the first draft of these notes, a competition was announced for [critiques of EA](https://forum.effectivealtruism.org/posts/8hvmvrgcxJJ2pYR4X/announcing-a-contest-ea-criticism-and-red-teaming); I'll be curious to see the entries. The design of the competition is, perhaps unfortunately, built around pre-existing EA ideas.

## Acknowledgments

Thanks to many people for conversations that have changed or informed how I think about EA, including: Marc Andreessen, Nadia Asparouhova, Alexander Berger, David Chapman, Patrick Collison, Julia Galef, Anastasia Gamick, Danny Goroff, Katja Grace, Spencer Greenberg, Robin Hanson, David Krakauer, Rob Long, Andy Matuschak, Luke Muehlhauser, Chris Olah, Catherine Olsson, Toby Ord, Kanjun Qiu, and Jacob Trefethen. Any good ideas here are due in large part to them. Of course, they're entirely responsible for all the mistakes :-P! My especial thanks to Alexander Berger, Anastasia Gamick, Katja Grace, Rob Long, Catherine Olsson, and Toby Ord: conversations with whom directly inspired these notes. I expect many of them would, however, disagree strongly with much that is in the notes! And thanks to Nadia Asparouhova and David Chapman for providing feedback on a draft of the notes. Thanks to Keller Scholl for pointing out an error in the initial release of the essay.

## Footnotes

[^1]:
    Helen Toner has a thoughtful
    [rebuttal](https://forum.effectivealtruism.org/posts/FpjQMYQmS3rWewZ83/effective-altruism-is-a-question-not-an-ideology) of the idea that EA is an ideology,
    arguing that most ideologies aim to provide answers, whereas EA is mostly
    about asking a question ("how to do the most good?") The essay is very good,
    but ultimately I'm comfortable using "ideology" to describe EA. There is a
    strong presumption in EA that you _should_ aim to do the most good, using your
    best judgement based upon available information and opportunity. In that
    sense, it _is_ providing an answer. However, as I'll discuss later, one of the
    most attractive features of EA – and one unusual among ideologies – is that a
    large chunk of the answer is changing and constantly being renegotiated.

[^2]:
    I will frequently refer to people who "are" EAs. Of course, the question of
    identity is a tricky one. There's many people – myself included – who are
    adjacent to the EA community, but not quite in it. (I certainly do not think
    of myself as an EA.) One of my favorite jokes about the (also EA-adjacent)
    rationality community is that their membership cry is "I'm not a rationalist,
    but…" It's not quite as true of EAs, but there's some truth there, too.

[^3]: The ideas here are due to conversation with Catherine Olsson and Rob Long.
[^4]: Peter Singer, "The Most Good You Can Do" (2015).
[^5]: "Moral psychonaut" was suggested to me by Catherine Olsson.
[^6]:
    In these and other examples it's unclear who the original moral pioneer was.
    Certainly, the author of the Sermon didn't "discover" the ideas alone, they
    came out of some tradition, some act of collective discovery. It's also true
    that just because someone is a moral pioneer doesn't make them a good person
    in an unqualified way! In that sense the term "hero" is perhaps inappropriate.

[^7]:
    And wow, are they ever. This is a personal bugbear, something where I think
    EAs are way off the reservation. Newton, Darwin, and Einstein didn't arrive at
    their huge breakthroughs using RCTs and meta-analyses. Nor did Picasso learn
    to paint that way. RCTs and meta-analysis are a tiny part of the arsenal of
    science, not the pinnacle. Indeed, _methodology_ in that sense is never the
    pinnacle.

[^8]:
    I like to amuse myself with the notion that it's a Popperian approach to "the
    good". Moral conjectures and refutations, the logic of ethical discovery.
    Incidentally, you might say that "what is the good?" is rightly the purview of
    ethics and moral philosophy. EA arguably adds (imperfect) real-world
    experimental and applied components to those subjects.

[^9]:
    Perhaps we need a Center for Effective Effective Altruism? Or Givewellwell,
    evaluating the effectiveness of effectiveness rating charities.

[^10]:
    A friend noted that some EA organizations had gone through the startup
    accelerator YCombinator. I asked how that had gone. They paused, and then said
    with a laugh that they weren't sure, but it was notable that the organizations
    had become "much more interested in graphs that go up and to the right". (On
    balance, I'd guess this is positive. I'm not sure, but I enjoy the story.)

[^11]:
    It's interesting to conceive of EA principally as a means of providing public
    goods which are undersupplied by the market. A slightly deeper critique here
    is that the market provides a very powerful set of signals which aggregate
    decentralized knowledge, and help people act on their comparative advantage.
    EA, by comparison, is relatively centralized, and focused on absolute
    advantage. That tends to centralize people's actions, and compounds mistakes.
    It's also likely a far weaker resource allocation model, though it does have
    the advantage of focusing on public goods. I've sometimes wondered about a
    kind of "libertarian EA", more market-focused, but systematically correcting
    for well-known failures of the market.

[^12]:
    This seems to be less true of EA than many (though not all) other
    organizations and movements. It is, however, concerning that EA organizations
    (mostly) don't have any expiry date; nor is there much of a competitive model
    ensuring improved organizations will thrive and outgrow less effective ones.
    Incidentally, I've heard it said that the first generation of any successful
    religion is started by a prophet, the second generation is run by a very
    effective bureaucrat. This is perhaps true in other domains as well.

[^13]:
    It's something of a tangent, but: I personally often find many new EAs a
    little self-righteous and overconfident, and sometimes overly evangelical,
    either for EA or for particular cause areas ("why are you wasting your time
    doing that, you should be working on AI safety", said by someone who thinks
    they know about AI, but does not, and has no ideas of any value about AI
    safety). This varies from amusing to mildly annoying to infuriating. This
    pattern is, however, common to many ideological movements, and I doubt it's
    particularly bad with EA. You can find similar issues within environmentalism,
    crypto, libertarianism, most religions, communism, and many other ideologies.

[^14]:
    Except, crucially, participation in the market and subjugation to the
    government. It's rule-by-technocracy. It's perhaps telling that the former
    (participation in the market) is also framed in terms of choice. But it
    introduces some notion of a "natural" set of choices available to you, through
    notions like the labor market and the market for goods and services. There is
    nothing natural about them.

[^15]:
    I'm not sure "duty" is the word usually used. But it captures the emotional
    sense I often get quite well. It's not without joy or elan, but those aren't
    primary, either.

[^16]:
    I suspect no society, ever, has been healthy that didn't invest significant
    time and resources in the arts.

[^17]: An insightful, humane essay in this vein is Julia Wise's [You have more than one goal, and that's fine](https://forum.effectivealtruism.org/posts/zu28unKfTHoxRWpGn/you-have-more-than-one-goal-and-that-s-fine) (2019).
[^18]:
    Amia Srinivasan, [Stop the Robot Apocalypse](https://www.lrb.co.uk/the-paper/v37/n18/amia-srinivasan/stop-the-robot-apocalypse), London Review of
    Books (2015).

[^19]: James Scott, "Seeing Like a State" (1998).
[^20]:
    Cf David Chapman's closely related concept of
    [nebulosity](https://meaningness.com/nebulosity).

# Independent impressions

Your **independent impression** about something is essentially what you'd believe about that thing if you weren't updating your beliefs in light of peer disagreement - i.e., if you weren't taking into account your knowledge about what other people believe and how trustworthy their judgement seems on this topic. Your independent impression can take into account the _reasons_ those people have for their beliefs (inasmuch as you know those reasons), but not the _mere fact_ that they believe what they believe.

Meanwhile, your **all-things-considered belief** can (and probably should!) also take into account peer disagreement.

Armed with this concept, I try to stick to the following epistemic/[ _discussion norms_](https://forum.effectivealtruism.org/tag/discussion-norms), and I think it's good for other people to do so as well:

- I try to **keep track of my own independent impressions** separately from my all-things-considered beliefs
- I try to **feel comfortable reporting my own independent impression** , even when I know it differs from the impressions of people with more expertise in a topic
- I try to **be clear about whether, in a given moment, I'm reporting my independent impression or my all-things-considered belief**

One rationale for that bundle of norms is to avoid [information cascades](https://www.lesswrong.com/tag/information-cascades).

In contrast, when I actually _make decisions_ , **I try to always make them based on my all-things-considered beliefs**.

For example: My independent impression is that it's plausible that an [unrecoverable dystopia](https://forum.effectivealtruism.org/tag/dystopia) is more likely than extinction and that we should prioritise such risks more than we currently do. But this opinion seems relatively uncommon among people who've thought a lot about [existential risks](https://forum.effectivealtruism.org/posts/AJbZ2hHR4bmeZKznG/venn-diagrams-of-existential-global-and-suffering). That observation pushes my all-things-considered belief somewhat away from my independent impression and towards what most of those people seem to think. And this all-things-considered belief is what guides my research and career decisions. But I think it's still useful for me to keep track of my independent impression and report it sometimes, or else communities I'm part of might end up with overly certain and homogenous beliefs.

---

_This term, this concept, and these suggested norms aren't at all original to me - see in particular_[ _Naming beliefs_](https://www.overcomingbias.com/2008/04/naming-beliefs.html) _,_[ _this comment_](https://forum.effectivealtruism.org/posts/WKPd79PESRGZHQ5GY/in-defence-of-epistemic-modesty?commentId=cubpmCn7XJE5FQYEq) _, and several of the posts tagged_[ _Epistemic humility_](https://forum.effectivealtruism.org/tag/epistemic-humility) _(especially_[ _this one_](https://forum.effectivealtruism.org/posts/jhexFncC9KN76Z5ki/ea-concepts-share-impressions-before-credences) _). But I wanted a clear, concise description of this specific set of terms and norms so that I could link to it whenever I say I'm reporting my independent impression, ask someone for theirs, or ask someone whether an opinion they've given is their independent impression or their all-things-considered belief._

_My thanks to Lukas Finnveden for_[ _suggesting I make this a top-level post_](https://forum.effectivealtruism.org/posts/EMKf4Gyee7BsY2RP8/michaela-s-shortform?commentId=w3QwxtDRxeueg3ZEf#w3QwxtDRxeueg3ZEf) _(it was originally a shortform)._

_This work is licensed under a_[ _Creative Commons Attribution 4.0 International License_](https://creativecommons.org/licenses/by/4.0/) _._

{{< rawhtml >}}

<html>
  <head>
    <script type="module" src="https://js.withorbit.com/orbit-web-component.js"></script>
  </head>
  <body>
    <orbit-reviewarea color="blue">
      <orbit-prompt
        question="What are independent impressions?"
        answer="What you’d believe about that thing if you weren’t updating your beliefs in light of peer disagreemen"
      ></orbit-prompt>
      <orbit-prompt
        question="What are all-things-considered beliefs?"
        answer="What you believe about a thing, taking into account peer disagreement."
      ></orbit-prompt>
      <orbit-prompt
        question="During a discussion, you're asked about your view on a topic. Your independent impression differs from the consensus in the EA community. What do you do? "
        answer="
- Be comfortable reporting your own independent impression. 
- However, make it clear if you're reporting your independent impression or your all-things-considered belief."
      ></orbit-prompt>
      <orbit-prompt
        question="When making decision, do you use your independent impressinos or all-things-considered beliefs?"
        answer="Your all-things-considered beliefs"
      ></orbit-prompt>
    </orbit-reviewarea>
  </body>
</html>

{{< /rawhtml >}}

# Big List of Cause Candidates

_Many thanks to Ozzie Gooen for suggesting this project, to Marta Krzeminska for editing help and to Michael Aird and others for various comments. In early 2022,_[ **Leo**](https://forum.effectivealtruism.org/users/ea-wiki-assistant) _updated the list with new candidates suggested before March 2022, in_[ **this**](https://forum.effectivealtruism.org/posts/DBhuERvKRgGpLiK6T/big-list-of-cause-candidates-january-2021-march-2022-update) _post—these have now been incorporated into the main post._

In the last few years, there have been many dozens of posts about potential new EA cause areas, causes and interventions. Searching for new causes seems like a worthy endeavour, but on their own, the submissions can be quite scattered and chaotic. Collecting and categorizing these cause candidates seemed like a clear next step.

At the time we first published this post, we —Ozzie Gooen of the Quantified Uncertainty Research Institute and I—noted that we might later be interested in expanding this work and eventually using it for forecasting —e.g., predicting whether each candidate would still seem promising after much more rigorous research. At the same time, we felt like the original list itself could be useful already. Since then, we haven't carried out forecasting experiments, but we have once updated the list as noted above.

Below is the current list with suggestions up to March 2022. It has a simple categorization, as well as an occasional short summary which paraphrases or quotes key points from the posts linked. See the last appendix for some notes on nomenclature. If there are any entries I missed (and there will be), please say so in the comments and I'll add them.

Initially, I created the[ _"Cause Candidates"_](https://forum.effectivealtruism.org/tag/cause-candidates) tag on the EA Forum and tagged all of the listed posts, and made available a[ _Google Sheet_](https://docs.google.com/spreadsheets/d/1GV-6M4WN1kvYnhplxgLA5cf37OdtGh3zDtOqy2uepJQ/edit#gid=469320850). These are not maintained, but might be upon request.

## **Animal Welfare and Suffering**

_Pointer_ : This cause has its various EA Forum tags ([ _farmed animal welfare_](https://forum.effectivealtruism.org/topics/farmed-animal-welfare),[ _wild animal welfare_](https://forum.effectivealtruism.org/topics/wild-animal-welfare),[ _meat alternatives_](https://forum.effectivealtruism.org/topics/meat-alternatives)), where more cause candidates can be found. Brian Tomasik et al.'s[ _Essays on Reducing Suffering_](https://reducing-suffering.org/) are also a gift that keeps on giving for this and other cause areas.

**1.Wild Animal Suffering Caused by Fires**

_Related categories_ : Politics: System change, targeted change, policy reform.

- [ _Wild animal suffering caused by fires and ways to prevent it: a noncontroversial intervention_](https://forum.effectivealtruism.org/posts/D2L3YjYnKh6XtZZqu/wild-animal-suffering-caused-by-fires-and-ways-to-prevent-it) (@Animal_Ethics)

An Animal Ethics grantee designed a[ _protocol_](https://www.animal-ethics.org/wp-content/uploads/Challenges-fires-wild-animals-how-to-help.pdf) aimed at helping animals during and after fires. The protocol contains specific suggestions, but the path to turning these into policy is unclear.

**2\. Invertebrate Welfare**

- \__[\_Invertebrate Welfare Cause Profile_](https://forum.effectivealtruism.org/posts/EDCwbDEhwRGZjqY6S/invertebrate-welfare-cause-profile) (@Jason Schukraft)
- [ _The scale of direct human impact on invertebrates_](https://forum.effectivealtruism.org/posts/9drbh8sKzzykaX38P/the-scale-of-direct-human-impact-on-invertebrates) (@abrahamrowe)

" _In this post, we apply the standard importance-neglectedness-tractability framework to invertebrate welfare to determine, as best we can, whether this is a cause area that is worth prioritizing. We conclude that it is_."

_Note_ : See also Brian Tomasik's[ _Do Bugs Feel Pain_](https://reducing-suffering.org/do-bugs-feel-pain/) _._

**3\. Humane Pesticides**

- [ _Humane Pesticides as the Most Marginally Effective Cause_](https://forum.effectivealtruism.org/posts/qnGkejbe7S8tpCaBx/humane-pesticides-as-the-most-marginally-effective-cause) (@JeffMJordan)
- [ _Improving Pest Management for Wild Insect Welfare_](https://forum.effectivealtruism.org/posts/puxyrkSSZ9FEYK6Rm/improving-pest-management-for-wild-insect-welfare-1) (@Wild_Animal_Initiative)

The post argues that insects experience consciousness, and that there are a lot of them, so we should give them significant moral weight (comments contain a discussion on this point). The post goes on to recommend subsidization of less-painful pesticides, an idea initially suggested by Brian Tomasik, who " _estimates this intervention to cost one dollar per 250,000 less-painful deaths_." The second post goes into much more depth.

**4\. Diet Change**

- [ _Is promoting veganism neglected and if so what is the most effective way of promoting it?_](https://forum.effectivealtruism.org/posts/CZ2pyJPTAjcMX5Gyt/is-promoting-veganism-neglected-and-if-so-what-is-the-most) (@samuel072)
- [ _Animal Equality showed that advocating for diet change works. But is it cost-effective?_](https://forum.effectivealtruism.org/posts/9ShnvD6Zprhj77zD8/animal-equality-showed-that-advocating-for-diet-change-works) (@Peter_Hurford, @Marcus_A_Davis)
- [ _Cost-effectiveness analysis of a program promoting a vegan diet_](https://forum.effectivealtruism.org/posts/bxqMGCLNaz8Cbq7Yr/cost-effectiveness-analysis-of-a-program-promoting-a-vegan) (@nadavb, @sella, @GidonKadosh, @MorHanany)
- [ _Measuring Change in Diet for Animal Advocacy_](https://forum.effectivealtruism.org/posts/Z6QhwL3MDppdrygQB/measuring-change-in-diet-for-animal-advocacy) (@Jacob_Peacock)

The first post is a stub. The second post looks at a reasonably high-powered study on individual outreach. It concludes that, based on reasonable assumptions, the particular intervention used (showing videos of the daily life of factory-farmed pigs) isn't competitive with other interventions on humans:

“(...) we now think there is sufficient evidence to establish that individual outreach may work to produce positive change for nonhuman animals. However, evidence in this study points to an estimate of $310 per pig year saved (90% interval: $46 to $1100), which is worse than human-focused interventions even from a species neutral perspective. More analysis would be needed to see how individual outreach compares to other interventions in animal advocacy or in other cause areas.

Given that a person can be reached for ~$2 and that they spare ~1 pig week, that works out to $150 per pig saved (90% interval: $23 to $560) and, again assuming that each pig has a ~6 month lifespan, that works out to $310 per pig year saved (90% interval: $47 to $1100). To put this in context, Against Malaria Foundation can avert a year of human suffering from malaria for $39, this does not look very cost-effective.”

Comments point out that the postulated retention rates may be too high (making the intervention even worse). Lastly, the second post was written in 2018, and more work might have been done in the meantime.

The third post is somewhat more recent (Nov 2020), but it reports results in terms of "portions of meat not consumed" rather than “animal-years spared”. This makes a comparison with previous research not be straightforward, because different animals correspond to different intensity and length of suffering per kilogram of meat produced, and the post does not report how big these portions are or to which animals they belong.

The fourth post explores " _current and developing alternatives to self-reporting of dietary data._ "

**5\. Vegan/Vegetarian Recidivism**

- [ _Veg\*n recidivism seems important, tractable, and neglected_](https://forum.effectivealtruism.org/posts/NDhjoWvTA8z4pq8hD/veg-n-recidivism-seems-important-tractable-and-neglected) (@xccf)

"But there's a big problem with vegan/vegetarian advocacy: most people who switch to vegan/vegetarian diets later switch back."

The post suggests paying more attention to the growth rate of the vegan/vegetarian movement. It also suggests some specific measures, like producing resources which make it easier for vegetarians/vegans to get all the nutrients they need in the absence of animal products.

**6\. Plant-Based Seafood**

- [ _Plant-Based Seafood: A Promising Intervention in Food Technology? - Charity Entrepreneurship Approach Report_](https://forum.effectivealtruism.org/posts/FWRqytSMLZXSSQP4N/plant-based-seafood-a-promising-intervention-in-food) (vicky_cox)

This Charity Entrepreneurship report ultimately concludes that: " _...while fish product creation in Asia is the most promising intervention within food technology in terms of impact on animals, it is not the most promising intervention for Charity Entrepreneurship to focus on."_

_Note_ : Charity Entrepreneurship has produced many more reports. But, as they are not tagged on the EA Forum, they were difficult to incorporate in this analysis, given the search method I was using (see Appendix: Method). They are, however, available on their[ _webpage_](https://www.charityentrepreneurship.com/animal-welfare-reports.html).

**7\. Improving plant-based diets**

- [ _The Case for Rare Chinese Tofus_](https://forum.effectivealtruism.org/posts/u76hM793BDvyqfdAH/the-case-for-rare-chinese-tofus-1) (@George Stiffman)

In order to improve vegan alternatives, this post proposes to create new types of plant-based food crossing rare Chinese tofu with traditional western cooking methods. The author analyzes the idea in detail, and answers possible objections.

**8\. Moral Circle Expansion**

- [ _Why I prioritize moral circle expansion over artificial intelligence alignment_](https://forum.effectivealtruism.org/posts/BY8gXSpGijypbGitT/why-i-prioritize-moral-circle-expansion-over-artificial) (@Jacy_Reese)

"This blog post makes the case for focusing on quality risks over population risks. More specifically, though also more tentatively, it makes the case for focusing on reducing quality risk through moral circle expansion (MCE), the strategy of impacting the far future through increasing humanity's concern for sentient beings who currently receive little consideration (i.e. widening our moral circle so it includes them.)"

In particular, the post makes this point by comparing moral circle expansion to AI alignment as a cause area.

**9\. Analgesics for Farm Animals**

_Related categories_ : Politics: System change, targeted change, policy reform.

- [ _Analgesics for farm animals_](https://forum.effectivealtruism.org/posts/LLLFTXiHMEd4MctQ5/analgesics-for-farm-animals) (@Monica)

"There is only one FDA approved drug for farm animal pain in the U.S. (and that drug is not approved for any of the painful body modifications that farm animals are subjected to), FDA approval might meaningfully increase the frequency with which these drugs actually used, and addressing this might be a tractable and effective way to improve farm animal welfare [...] Farm animals in the U.S. almost never get pain medication for acutely painful procedures such as castration, tail docking, beak trimming, fin cutting, abdominal surgery, and dehorning. What I was not aware of until this morning is that there is only one FDA approved medication for ANY farm animal analgesic, and that medication is specifically approved only for foot rot in cattle [...] In contrast, the EU, UK, and Canada have much higher standards for food residues in other domains (hormones, antibiotics, etc.) but have nevertheless approved several pain medication for several procedures in species of farm animals. As a result, these drugs are much more commonly used there."

**10\. Welfare of Specific Animals**

Rethink Priorities has done research on the welfare of specific animals, and possible interventions to improve it. They produced a number of profiles, some of which I include here for illustration purposes, but without any claim to comprehensiveness. Thanks to Saulius for bringing my attention to this point.

- _Honey Bee Welfare_ :[ _Managed Honey Bee Welfare: Problems and Potential Interventions_](https://forum.effectivealtruism.org/posts/XyKJJqLQjSKzL7ykP/managed-honey-bee-welfare-problems-and-potential-1) (@Jason Schukraft)
- _Baitfish_ :[ _Fish used as live bait by recreational fishermen_](https://forum.effectivealtruism.org/posts/gGiiktK69R2YY7FfG/fish-used-as-live-bait-by-recreational-fishermen) (@saulius)
- _Fish Stocking_ :[ _35-150 billion fish are raised in captivity to be released into the wild every year_](https://forum.effectivealtruism.org/posts/4FSANaX3GvKHnTgbw/35-150-billion-fish-are-raised-in-captivity-to-be-released) (@saulius)
- _Wild-caught Fish_ :[ _Worse things happen at sea: The welfare of wild-caught fish_](http://www.fishcount.org.uk/published/standard/fishcountfullrptSR.pdf) (Alison Mood, fishcount.org.uk)
- _Cleaner Fish_ :[ _Cleaner Fish: A Neglected Issue Within A Neglected Issue_](https://forum.effectivealtruism.org/posts/HboFNEyAxa7nzdFhF/cleaner-fish-a-neglected-issue-within-a-neglected-issue) (@Martine Klock Fleten). Despite poor evidence, the use of[ _cleaner fish_](https://en.wikipedia.org/wiki/Cleaner_fish) is common practice among salmon farmers to control sea lice, leading to their suffering and death. The post proposes to improve cleaner fish welfare, or to put an end to this practice.
- _Rodents Fed to Snakes_ :[ _Rodents farmed for pet snake food_](https://forum.effectivealtruism.org/posts/pGwR2xc39PMSPa6qv/rodents-farmed-for-pet-snake-food) (@saulius)
- _Mice and Rats_ : [Question] \__[\_Are mice or rats (as pests) a potential area of animal welfare improvement?_](https://forum.effectivealtruism.org/posts/RgkxGz75YogvTTA9o/are-mice-or-rats-as-pests-a-potential-area-of-animal-welfare) (@Louis_Dixon) This post hints that the suffering of mice and rats in cities might be a possible cause area. The answers give several clues about how to tackle the issue.
- _Insect Farming_ :[ _Insects raised for food and feed — global scale, practices, and policy_](https://forum.effectivealtruism.org/posts/ruFmR5oBgqLgTcp2b/insects-raised-for-food-and-feed-global-scale-practices-and) (@abrahamrowe)
- _Snail Farming_ :[ _Snails used for human consumption: The case of meat and slime_](https://forum.effectivealtruism.org/posts/C8247akhZpyMXkRb3/snails-used-for-human-consumption-the-case-of-meat-and-slime) (@Daniela R. Waldhorn)
- _Cochineals_ :[ _Global cochineal production: scale, welfare concerns, and potential interventions_](https://forum.effectivealtruism.org/posts/tDYtn4DhFsR7pR35i/global-cochineal-production-scale-welfare-concerns-and) (@abrahamrowe)
- _Silkworms_ :[ _Silk production: global scale and animal welfare issues_](https://forum.effectivealtruism.org/posts/mZEuNcwTZxLnXrZR6/silk-production-global-scale-and-animal-welfare-issues) (@abrahamrowe). The post examines if the suffering of silkworms used in silk production could be an area to be prioritized, but concludes that available resources “might be better spent in other areas, such as reducing the painfulness of pesticides, reducing the number of insects farmed for animal feed, and reducing the harms of cochineal farming”.
- _Owned cats outdoors in Canada:_[ _\_\_Would a reduction in the number of owned cats outdoors in Canada and the US increase animal welfare?_](https://forum.effectivealtruism.org/posts/QwPg6C43s6wKZ2tv7/would-a-reduction-in-the-number-of-owned-cats-outdoors-in-1) (@kcudding)
- _Chickens_ : [Question][ _New EA cause area: Breeding really dumb chickens_](https://forum.effectivealtruism.org/posts/ySwJso4F3AzbxHdET/new-ea-cause-area-breeding-really-dumb-chickens) (@Sam Enright). This post poses some questions about the idea of “breeding chickens (and other farm animals) to be less intelligent as a way to reduce the suffering caused by factory farming”.
- _Baboons_ :[ _Urban wildlife in South Africa - Cape baboons_](https://forum.effectivealtruism.org/posts/sadugJrbaa9v2z9zg/urban-wildlife-in-south-africa-cape-baboons) (@ajmfisher). "The aim of this post is to catalogue existing methods for managing the population of Cape chacma baboons living in the Cape peninsula, with a focus on welfare impacts for the baboons."

**11\. Cell-Based Meat R &D**

- [ _The extreme cost-effectiveness of cell-based meat R &D_](https://forum.effectivealtruism.org/posts/cXWAJPipxg5dMxfx8/the-extreme-cost-effectiveness-of-cell-based-meat-r-and-d) (@Stijn)

Based on a Fermi estimate, the author concludes that _"cell-based meat research and development is roughly 10 times more cost-effective than top recommended effective altruist animal charities."_

**12\. Animal-Free Proteins**

- [ _Animal-free proteins: A bright outlook and a to-do list (BCG report)_](https://forum.effectivealtruism.org/posts/AwPtuGn62p6T4yuhD/animal-free-proteins-a-bright-outlook-and-a-to-do-list-bcg) (@FGH)

“The report describes what needs to happen to get to 11%, and further to 22% of meat, seafood, eggs and dairy eaten globally every day. Current technology must be refined and scaled, and in some areas, step changes are needed. For instance, optimized protein crops for human consumption need to be bred, and microorganisms as well as animal cells grown on low-cost feedstocks. Regulatory support, such as carbon taxes on meat or subsidies for farmers who are shifting from animal agriculture to alternative proteins, could further boost growth.”

**13\. Antibiotic Resistance in Farmed Animals**

- [ _Antibiotic resistance: Should animal advocates intervene?_](https://forum.effectivealtruism.org/posts/2qXfME3Rrcd7mdnMr/antibiotic-resistance-should-animal-advocates-intervene) (@Bella_Forristal)

“Reducing antibiotic use in farms is very likely to be net positive for humans. However, it is not clear whether it would be net positive for animals. If farmers stop using antibiotics, animals might suffer from more disease and worse welfare. This effect might be mitigated by the fact that (i) farmers can replace antibiotics with substitutes such as probiotics, prebiotics, and essential oils, which also prevent disease, and (ii) farmers might be motivated to make adaptations to farming practices which prevent disease and also benefit animal welfare, such as lowering stocking density, reducing stress, and monitoring disease more closely. It is not obvious how likely it is that farmers will take these disease-mitigating measures, but since high disease rates increase mortality, decrease carcass profitability, and could cause reputational damage, it is plausible that they will be motivated to do so. Alternatively, animal advocates could take the 'holistic strategy' of promoting welfare measures which also tend to cause reduced antibiotic use. Tentatively, I take the view that eliminating antibiotic use on a farm would not lead to worse lives for those animals.

Eliminating antibiotics might also be expensive for producers, and because of this, it could increase the price of animal products in the short term, which would be good for animals. The literature weakly supports the view that meat prices will increase following an antibiotic ban. However, there is also some support for the view that price will increase differentially for smaller and larger animals, which lands us with the small animal replacement problem. This problem could be avoided by the approach taken to the intervention, e.g. a corporate campaign targeting only small animals.”

**14\. Helping Wild Animals Through Vaccination**

- [ _Helping wild animals through vaccination: could this happen for coronaviruses like SARS-CoV-2?_](https://forum.effectivealtruism.org/posts/AsKaJYQtm6NMHSc26/helping-wild-animals-through-vaccination-could-this-happen) (@Animal_Ethics)

"We will first see some cases of successful vaccination programs in the past, including vaccination against rabies, anthrax, rinderpest, brucellosis, and sylvatic plague, in addition to the proposal to vaccinate great apes against Ebola. Next, we will see how zoonotic epidemics have been the object of growing attention.We will then see some responses to them that are misguided and harmful to animals. We will then see the prospects for eventual wild animal vaccination programs against coronaviruses like SARS-CoV-2. We will see the three main limitations of such hypothetical programs. These are the lack of an effective vaccine, the lack of funding to implement the vaccination program, and the lack of an effective system to administer the vaccine. We’ll consider the extent to which these limitations could be overcome and what clues previous examples of vaccination can provide. As we will see, such programs remain to date merely speculative. They could be feasible at some point as other wild animal vaccination programs show. However, it remains uncertain whether there will be human interest in implementing them, despite the benefits for animals themselves.

Finally, we will see the reasons why, if implemented, programs of this kind could substantially help not just the vaccinated animals, but many others as well. Not only would this prevent zoonotic disease transmission to other animals, but such measures could also help inform other efforts to vaccinate animals living in the wild. Moreover, each successful vaccination program helps to illustrate that helping animals in the wild is not impractical, but realistic. This helps to raise concern for these animals and to inspire action on their behalf.”

**15\. Herbivorizing Predators**

- [ _Should we herbivorize predators?_](https://forum.effectivealtruism.org/posts/t54zASn6ohSbTbrsX/should-we-herbivorize-predators) (@Stijn)

This post puts forth a moral argument with the intention to open discussion about considering herbivorizing predators as a cause area. The author argues that we should start doing scientific research to look for new technologies that would make it possible.

## **Community Building**

**1.Effective Animal Advocacy Movement Building**

_Related categories_ : Animal Welfare and Suffering

- [ _Effective animal advocacy movement building: a neglected opportunity?_](https://forum.effectivealtruism.org/posts/7sdcXbTqjgFwzds2S/effective-animal-advocacy-movement-building-a-neglected) (@Jamie_Harris)

The post argues that EAA-specific movement-building might be particularly neglected within EA.

**2\. Non-Western EA**

- [ _Neglected EA Regions_](https://forum.effectivealtruism.org/posts/thydMM6FCuZFpRTS7/neglected-ea-regions) (@DavidNash)

The post asks about expanding EA beyond the USA and Europe. It gets some pushback in the comments, particularly because of the difficulty of transmitting ideas with high fidelity.

**3\. Understanding and/or reducing value drift.**

_Pointer: This cause has its own_[ **EA Forum tag**](https://forum.effectivealtruism.org/topics/value-drift) _._

- [ _A Qualitative Analysis of Value Drift in EA_](https://forum.effectivealtruism.org/posts/jG8pptGksBpzyTxYg/a-qualitative-analysis-of-value-drift-in-ea-1) (@MarisaJurczyk)

**4\. High School Outreach**

- [ _EA outreach to high school competitors_](https://forum.effectivealtruism.org/posts/DgygoJLDxBjFuq7p4/ea-outreach-to-high-school-competitors) (@Nikola)

“Specifically targeting STEM, logic, debate, and philosophy competitors with short outreach could increase high school outreach effectiveness as it would select for high-performing students who are more likely to engage with EA ideas. This would give these individuals more time to think about career choice and enable them to start building flexible career capital early and might make them more open to engaging with EA in the future.”

**5\. Idea Inoculation**

- [ _Effective outreach: evaluating "Idea innoculation"_](https://forum.effectivealtruism.org/posts/TkwAWgcYsF4DQ3T58/effective-outreach-evaluating-idea-innoculation) (@rsturrock)

This post proposes an experiment to serve as the basis of a psychology paper about EA ‘idea inoculation’, in order to discover better ways of conveying EA-related information.

**6\. Values Spreading**

- [ _Values Spreading is Often More Important than Extinction Risk_](https://reducing-suffering.org/values-spreading-often-important-extinction-risk/) (Brian Tomasik)
- [ _On Values Spreading_](https://forum.effectivealtruism.org/posts/BpuTtsz6J6GBycYvJ/on-values-spreading) (@MichaelDickens)
- [ _Against moral advocacy_](https://rationalaltruist.com/2013/06/13/against-moral-advocacy/) (Paul Christiano)
- [ _Effective Altruism and Free Riding_](https://forum.effectivealtruism.org/posts/54Cdt4BR84vDcki6i/effective-altruism-and-free-riding) (@sbehmer)
- [ _High-Leverage Values Spreading_](https://forum.effectivealtruism.org/posts/wtNCs2TgtDpu3W7Ke/charities-i-would-like-to-see#High_Leverage_Values_Spreading) (@MichaelDickens)
- [ _Promoting Simple Altruism_](https://forum.effectivealtruism.org/posts/Ekbs2zkPmxJYZxgwv/promoting-simple-altruism) (@LiaH)

Values spreading refers to improving other people's values. The idea has met with some skepticisim, but perhaps variants of it, like highly targetted or high-leverage values spreading, could still be promising.

## **Transhumanism**

_Related categories_ : Global Health and Development, States of Consciousness

**1.Cryonics**

- [ _Is there a hedonistic utilitarian case for Cryonics? (Discuss)_](https://forum.effectivealtruism.org/posts/jd4ycHq8aqFgJGvkY/is-there-a-hedonistic-utilitarian-case-for-cryonics-discuss) (@OzzieGooen)

Cryonics will probably get cheaper if more people sign up. It might also divert money from wealthy people who would otherwise spend it on more selfish things. Further, cryonics might help people take long-term risks more seriously.

_"_ One advantage of life extension is that it might prompt people to think in a more long-term-focused way, which might be nice for solving coordination problems and x-risks."

One could also argue _"that cryonics doesn't create many additional QALYs because by revival time we've probably hit Malthusian limits. So any revived cryonics patients would be traded off against other future lives."_

- [ _Brain preservation to prevent involuntary death: a possible cause area_](https://forum.effectivealtruism.org/posts/sRXQbZpCLDnBLXHAH/brain-preservation-to-prevent-involuntary-death-a-possible) (@AndyMcKenzie)

The author argues that brain preservation is “one of the best areas for people interested in helping others to work in” and “a great place for people who are interested in helping others to donate money”.

**2\. Ageing**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/life-extension). For illustration purposes:

- [ _How to evaluate neglectedness and tractability of ageing research_](https://forum.effectivealtruism.org/posts/zQDakLnNumoejXZuX/how-to-evaluate-neglectedness-and-tractability-of-aging) (@Emanuele_Ascani)
- [ _Project Proposal: Gears and Aging_](https://forum.effectivealtruism.org/posts/96QqhL5cJftYAp2ez/project-proposal-gears-and-aging) (@johnswentworth)
- [ _[Draft] Fighting Aging as an Effective Altruism Cause_](https://forum.effectivealtruism.org/posts/y3pkt43XsiGmg4Mje/draft-fighting-aging-as-an-effective-altruism-cause) (@turchin)
- [ _Cost-Effectiveness of Aging Research_](https://forum.effectivealtruism.org/posts/JsL2kPWJYRxn9rCWR/cost-effectiveness-of-aging-research) (@SarahC)
- [ _A general framework for evaluating ageing research_](https://forum.effectivealtruism.org/posts/jYMdWskbrTWFXG6dH/a-general-framework-for-evaluating-aging-research-part-1) (@Emanuele_Ascani)
- [ _RP Work Trial Output: How to Prioritize Anti-Aging Prioritization - A Light Investigation_](https://forum.effectivealtruism.org/posts/55YvXmp693t5XaRyR/rp-work-trial-output-how-to-prioritize-anti-aging) (@Linch)

**3\. Genetic Enhancement**

- [ _Genetic Enhancement as a Cause Area_](https://forum.effectivealtruism.org/posts/T8eKL6xdfL4yA2kvg/genetic-enhancement-as-a-cause-area) (@Galton)

The post makes the argument both from a short and long-term perspective. I was particularly intrigued by the suggestion to select for empathy; the comments also suggest selecting against malevolent traits.

**4\. Mind Enhancement**

- [ _Mind Enhancement: A High Impact, High Neglect Cause Area?_](https://forum.effectivealtruism.org/posts/FvZmZdqHNofJyw4Xv/mind-enhancement-a-high-impact-high-neglect-cause-area) (@timfarkas)

“This post aims to raise awareness, provide a rough framework for classification and list the most important theoretical arguments and considerations regarding the impact/desirability of mind enhancement.”

- [ _Cause profile: Cognitive Enhancement Research_](https://forum.effectivealtruism.org/posts/MojiqNw5MN6WMXETc/cause-profile-cognitive-enhancement-research-1) (@George Altman)

“This post is a first attempt at analysing cognitive enhancement research using the ITN framework and cost-effectiveness estimates. Several interventions enhance cognitive functions such as intelligence and decision making. If we identify effective, cheap and scalable cognitive enhancement interventions, they may be competitive with GiveWell charities.”

**5\. Finding Extraterrestrial Life**

- [ _Cosmic EA: How Cost Effective Is Informing ET?_](https://forum.effectivealtruism.org/posts/ga5qCreTmruCkoL4F/cosmic-ea-how-cost-effective-is-informing-et) (@TruePath)

## **Politics**

### **Politics: Ideological Politics**

**1\. Local Political Causes**

- [ _Should local EA groups support political causes?_](https://forum.effectivealtruism.org/posts/kfw94gsrCwo8MuL8h/should-local-ea-groups-support-political-causes) (@lukasberglund)
- [ _Recommendations for prioritizing political engagement in the 2020 US elections_](https://forum.effectivealtruism.org/posts/bpeWM6uwPaMP3kJsC/recommendations-for-prioritizing-political-engagement-in-the) (@IanDavidMoss)
- [ _New Top EA Cause: Politics_](https://forum.effectivealtruism.org/posts/SwADGj8f5sxAmXyLx/new-top-ea-cause-politics) (@Davidmanheim). _Note_ : Satirical.
- [ _Georgia on my Mind: Effectively Flipping the Senate_](https://forum.effectivealtruism.org/posts/vzH8g7GtoJLQHzNLS/georgia-on-my-mind-effectively-flipping-the-senate) (@deluks917)
- [ _What Are Effective Alternatives to Party Politics for Effective Public Policy Advocacy?_](https://forum.effectivealtruism.org/posts/TJPedCHGoHJiySuTn/what-are-effective-alternatives-to-party-politics-for) (@Evan_Gaensbauer)
- [ _What is the increase in expected value of effective altruist Wayne Hsiung being mayor of Berkeley instead of its current incumbent?_](https://forum.effectivealtruism.org/posts/Rcys5RkBzZ5vacBYY/what-is-the-increase-in-expected-value-of-effective-altruist) (@DonyChristie)
- [ _Why are party politics not an EA priority?_](https://forum.effectivealtruism.org/posts/Tju9XKJJhKbKo2CC7/why-are-party-politics-not-an-ea-priority) (@Chantal)

**2\. Fighting Harmful Ideologies**

- [ _Ineffective Altruism: Are there ideologies which generally cause their adherents to have worse impacts?_](https://forum.effectivealtruism.org/posts/t2TMwuDirnFz6PA5p/ineffective-altruism-are-there-ideologies-which-generally) (@Nathan Young)

_Note_ : Post is a stub.

### **Politics: Global politics**

Pointer: See also the EA Forum tag for[ _Global Governance_](https://forum.effectivealtruism.org/topics/global-governance).

**1\. Democracy Promotion**

- [ _Democracy Promotion as an EA Cause Area_](https://forum.effectivealtruism.org/posts/dTconqCtsmHQsNwo9/democracy-promotion-as-an-ea-cause-area-1) (@bryanschonfeld)

The author estimates the benefits of democracy. They then suggest concrete actions to take: " _a review essay on the efficacy of tools of external democracy promotion finds that non-coercive tools like foreign aid that is conditioned on democratic reforms and election monitoring are effective, while coercive tools like sanctions and military intervention are ineffective... One tool EA organizations can fund is election monitoring. Research suggests that election monitoring can play a causal role in decreasing fraud and manipulation._ " Some forum comments suggest that the area is too costly, and not that neglected.

- [ _Decreasing populism and improving democracy, evidence-based policy, and rationality_](https://forum.effectivealtruism.org/posts/8cr7godn8qN9wjQYj/decreasing-populism-and-improving-democracy-evidence-based) (@Hauke Hillebrandt)

This post explores several funding opportunities in this area. The author lists the following causes:

- **Increasing rationality:** Rationality could be increased by funding books as Galef’s _The Scout Mindset_ , or projects as the Winton Centre for Risk and Evidence.
- **General education spending** : “[E]ducation can often predict populism better than income. Thus one funding idea might be to try to increase education budgets globally.”
- **Civic education** : “[C]ivic education can strengthen democratic beliefs and explain the relevance of pluralism, which can play an important role in preventing populist attitudes.”
- **Journalism** : Funding ideas include payments for online news content, the provision of local and investigative journalism, and investigative fact-check websites in general.
- **Information spreading** : “One way to reduce populism is to give activists the tools to expose and debunk populist 'common sense' arguments”, tools like Our World in Data.
- **Research on populism** : “Funding opportunity: Fund an academic researcher working on populism.”
- **English language education** : “Fostering English language learning improves access to more content. This might improve international relations.” But the author notes that learning English doesn’t seem neglected.
- **Elections and voting** : Funding opportunities include switching back to paper ballots to increase trust (Verified Voting Foundation), voting system reform, and the uses of statistical techniques to test election results, among others.
- **Combatting computational propaganda** : Several funding opportunities and ideas are proposed here to counterbalance current AI techniques spreading misleading information.
- **Fostering more independent commissions and monitoring** : Following the example of the Independent Commission for Aid Impact, which scrutinises UK aid spending, institutional decision making could be improved by setting up independent commissions for every major department in government.
- **Aggregating expert consensus** : “Aggregating expert consensus might decrease populism by reducing the faith put in common sense approaches.”
- **Prediction markets** : “Furthering the use of prediction market might help increase the accuracy of forecasts for important policy issues.”
- **Doing more fundamental research** : Funding could foster fundamental research, which is useful to find new techniques to improve institutional decision making.

**2\. Promotion of Parliamentarism**

- [ _The effective altruist case for parliamentarism_](https://forum.effectivealtruism.org/posts/ZKzjaAGhddTF3iCQ9/the-effective-altruist-case-for-parliamentarism) (@Tiago Santos)

The author applies the ITN framework to promotion of parliamentarism and concludes that it is a valuable cause for EAs to focus on.

**3\. Promotion of Self-Determination**

- [ _A framework for self-determination_](https://forum.effectivealtruism.org/posts/DBhuERvKRgGpLiK6T/A%20framework%20for%20self-determination) (@kbog)

This post discusses the advantages of promoting more recognition of a right to self-determination. It develops a set of criteria to be met and applies them to the particular cases of Artsakh, Taiwan, and Crimea. Finally it shows some possible ways to reinforce the idea of self-determination.

**4\. Human Rights in North Korea**

- [ _Cause Area: Human Rights in North Korea_](https://forum.effectivealtruism.org/posts/werW78GfeAgBRbvF3/cause-area-human-rights-in-north-korea) (@Denis Drescher)

The scale of suffering seems vast, and marginal interventions (e.g., smuggling North Koreans out of China) might be cost-effective. The post also suggests capacity building in this area might be a promising intervention.

**5\. Improving Local Governance in Fragile States**

- [ _Improving local governance in fragile states - practical lessons from the field_](https://forum.effectivealtruism.org/posts/ynEh6An8PGpGmnCMM/improving-local-governance-in-fragile-states-practical)(@Timothy_Liptrot)

### **Politics: System Change, Targeted Change, and Policy Reform.**

_Note_ : These categories are grouped together because in practice the distinction between broad system change from outside a political system and targeted change or policy reform within a system is often not quite clear.

_Pointer_ : This cause candidate has a related EA Forum tag:[ _Policy Change_](https://forum.effectivealtruism.org/topics/policy-change).

**1\. Better Political Systems and Policy-Making**

Pointer: The related Institutional Decision-Making has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/institutional-decision-making); more cause candidates can be found there.

- [ _Cause: Better political systems and policy making_](https://forum.effectivealtruism.org/posts/qyX2YG2LCKCsMc2oX/cause-better-political-systems-and-policy-making) (@weeatquince)
- [ _Some personal thoughts on EA and systemic change_](https://forum.effectivealtruism.org/posts/QYH9yJ4WfHRs3ftJD/some-personal-thoughts-on-ea-and-systemic-change) (@Carl_Shulman)
- [ _Deliberation May Improve Decision-Making_](https://forum.effectivealtruism.org/posts/kCkd9Mia2EmbZ3A9c/deliberation-may-improve-decision-making) (@Neil_Dullaghan)
- [ _Answer to “Short List of Cause Areas?”_](https://forum.effectivealtruism.org/posts/NxM7JENRyreE5BbjQ/short-list-of-cause-areas?commentId=7hwTnJz5uc2g7HPeC) (@Jack Cunningham)

**2\. Getting Money Out of Politics and Into Charity**

- [ _Getting money out of politics and into charity_](https://forum.effectivealtruism.org/posts/poQebofmZCdXye8h6/getting-money-out-of-politics-and-into-charity) (@UnexpectedValues)

Donors from two opposing parties could be matched to send their money to their favourite charities instead than to zero-sum political contests.

**3\. Vote Pairing**

- [ _Vote Pairing is a Cost-Effective Political Intervention_](https://forum.effectivealtruism.org/posts/2QhtwLnxLa2DoBx2Z/vote-pairing-is-a-cost-effective-political-intervention) (@Ben_West)

The post makes the case that vote pairing —where one or more voters for a mainstream candidate in a safe US state vote for a third-party candidate in exchange for a vote from a third candidate supporter in a contested state— is much more effective than other traditional interventions.

**4\. Electoral Reform**

_Pointer_ : This cause has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/electoral-reform). I’m adding one post for illustration purposes:

- [ _Why You Should Invest In Upgrading Democracy And Give To The Center For Election Science_](https://forum.effectivealtruism.org/posts/jSjBHmgu3ZGcrW4t2/why-you-should-invest-in-upgrading-democracy-and-give-to-the) (@aaronhamlin)

_Note_ : Included here for completeness. This isn't, strictly speaking, a new cause area because the Center For Election Science is working on it.

**5\. Tax Justice**

- [ _Tax Havens and the case for Tax Justice_](https://forum.effectivealtruism.org/posts/LMN6kLhdre9szBv5o/tax-havens-and-the-case-for-tax-justice) (@--alex--)

The post gives an overview of current efforts to make tax evasion or tax flight harder, and why this should be thought of as positive. A commenter, Larks, makes the[ _opposite case_](https://forum.effectivealtruism.org/posts/LMN6kLhdre9szBv5o/tax-havens-and-the-case-for-tax-justice?commentId=tNzkYuaRPwmYQJNa8).

**6\. Effective Informational Lobbying**

- [ _Informational Lobbying: Theory and Effectiveness_](https://forum.effectivealtruism.org/posts/K638s9L2wCEW78DEF/informational-lobbying-theory-and-effectiveness) (@Matt_Lerner)
- [ _Effective Lobbying Discussion Group_](https://forum.effectivealtruism.org/posts/FqNbt76MLofRiFfKp/effective-lobbying-discussion-group) (@Noah Wescombe)

The first post starts with a literature review and concludes by proposing " _something along the lines of ‘effective lobbying’: a rigorous approach to institutional-level change, starting with the legislature, that would take a portfolio approach to policy advocacy,_ " and outlines how that would broadly look.

The second post is a " _call to all interested in lobbying as both a career and an EA methods topic._ " Having a discussion group on this topic seems like a great idea, so I gave the post a strong upvote. However, it seems like it didn't get picked up when it was posted in mid-December 2020.

**7\. Ballot Initiatives**

- [ _Intervention Profile: Ballot Initiatives_](https://forum.effectivealtruism.org/posts/2LdswNsEZAgDfJDzo/intervention-profile-ballot-initiatives) (@Jason Schukraft)

"The goal of this post is to bring ballot initiatives to the collective attention of the EA community to help promote future research into the effectiveness of ballot initiative campaigns for EA-aligned policies and movement-building." The post gives examples of what might be accomplished with ballot initiatives and covers their advantages and disadvantages.

**8\. Increasing Development Aid**

_Related categories_ : Global Health and Development.

- [ _Funding Proposal: Supporting a Campaign to Increase Canadian Official Development Assistance_](https://forum.effectivealtruism.org/posts/9cLAqwGgtyGTkx28k/funding-proposal-supporting-a-campaign-to-increase-canadian) (@jonathancourtney)
- [ _EAF's ballot initiative doubled Zurich's development aid_](https://forum.effectivealtruism.org/posts/dTdSnbBB2g65b2Fb9/eaf-s-ballot-initiative-doubled-zurich-s-development-aid) (@Jonas Vollmer)
- [ _£4bn for the global poor: the UK's 0.7%_](https://forum.effectivealtruism.org/posts/a5qSgWBLRsicYFRFm/gbp4bn-for-the-global-poor-the-uk-s-0-7) (@Sanjay)

**9\. Institutions for Future Generations**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/institutions-for-future-generations). For illustration purposes:

- [ _Institutions for Future Generations_](https://forum.effectivealtruism.org/posts/op93xvHkJ5KvCrKaj/institutions-for-future-generations) _(@tylermjohn)_

**10\. Decline or Collapse of the US.**

- [ _EA and the Possible Decline of the US: Very Rough Thoughts_](https://forum.effectivealtruism.org/posts/MjWHupe8d8mMGJqKP/ea-and-the-possible-decline-of-the-us-very-rough-thoughts) (@Cullen_OKeefe)

There are reasons to believe that the probability of regime collapse of the US in the next 50 years is higher than 0.5%. The dis-utility from Collapse could be extreme in certain scenarios.

### **Politics: Armed Conflict**

This cause has two related EA Forum tags:[ _Armed conflict_](https://forum.effectivealtruism.org/posts/MsJvzmYLMpsdJBb6C/which-nuclear-wars-should-worry-us-most) and[ _Nuclear Weapons_](https://forum.effectivealtruism.org/topics/nuclear-weapons) which may contain more cause candidates.

**1\. Preventing or Reducing The Severity of Nuclear War**

- [ _Which nuclear wars should worry us most?_](https://forum.effectivealtruism.org/posts/MsJvzmYLMpsdJBb6C/which-nuclear-wars-should-worry-us-most) (@Luisa_Rodriguez)

_Note_ :[ _Luisa Rodríguez_](https://forum.effectivealtruism.org/users/luisa_rodriguez) has more content in this cause.

**2\. Ukraine Conflict**

- [ _Ukraine giving - short term high leverage_](https://forum.effectivealtruism.org/posts/9A8rfagaSvow6pCsN/ukraine-giving-short-term-high-leverage) (@Timothy_Liptrot)

This post proposes supporting Ukraine as a cause area, arguing that if Russia is not strongly punished, other states could follow similar policies. The author goes on to propose buying satellites for improving Ukraine’s military system.

## **Global Health and Development**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/global-health-and-development).

**1\. Reducing the Efficiency of Genocides**

_Related categories_ : Politics

- [ _A brief look at reducing the efficiency of genocides_](https://forum.effectivealtruism.org/posts/Du7BzmTEoDZ44AbN7/a-brief-look-at-reducing-the-efficiency-of-genocides) (@NLHeath)

The post makes the case that at least some genocides (the Rwandan, Myanmar, and possibly the Somalian genocides) could have been stopped with better oversight and targeted use of resources.

**2\. Malnutrition**

- [ _Might targeting malnutrition (not undernourishment!) be an important cause area?_](https://forum.effectivealtruism.org/posts/3YEnCxrbFzmFDNfx5/might-targeting-malnutrition-not-undernourishment-be-an) (@peter_janicki)

The author asks about the impact of malnutrition, i.e., "eating the wrong things as a voluntary choice despite having alternatives." This would mostly be a problem for middle and high-income countries.

**3\. Diet Change**

- [ _Dietary habits – Another potential Cause Area?_](https://forum.effectivealtruism.org/posts/k7qL3GsHqioyauHQw/dietary-habits-another-potential-cause-area) (@peter_janicki)

Unhealthy food choices result in poor diets that reduce expected lifespan and life quality. The author of this post collects a considerable amount of evidence and argues that this a neglected area, given the number of people affected by those choices.

**4\. Raising IQ**

_Related categories_ : [_Transhumanism_](https://forum.effectivealtruism.org/topics/transhumanism)

- [ _Consider raising IQ to do good_](https://forum.effectivealtruism.org/posts/oGBdBsPc45ZrRPkwZ/consider-raising-iq-to-do-good) (@Lila_Rieber)

"Interventions to raise IQ could do a lot of good because of potentially significant flow-through effects of intelligence. IQ also has the benefit of being easily quantifiable, which would make it simpler to compare interventions."

_Note_ : In practice, the raising-IQ framing is unpalatable for some people, as are some charities in an adjacent space, like[ _Project Prevention_](http://projectprevention.org). However, because one of the most effective ways of raising IQ is reducing malnourishment or undernourishment, and in particular, iodine deficiency, one could focus on these causes instead. Note that mal/undernourishment in kids leads to lower wages in adulthood. Although one might suspect IQ is the mediating factor, it's not necessary to emphasize the connection.

**5\. Physical Goods**

- [ _The EA movement is neglecting physical goods_](https://forum.effectivealtruism.org/posts/XwchM4mDT6hocqj2h/the-ea-movement-is-neglecting-physical-goods) (@ruthgrace)

"Seven out of eight of the Givewell top charities deal with physical goods—anti-malaria nets, deworming medication, and vitamins. But otherwise, there's not much discussion/active work in EA on how to improve/spin up the physical manufacture and distribution of physical goods beyond donating money to existing organisations."

**6\. Fighting Diarrhoea**

- [ _How does fighting diarrhoea stack up to malaria in effectiveness?_](https://forum.effectivealtruism.org/posts/6u7RdvDqHKLcFjueq/how-does-fighting-diarrhoea-stack-up-to-malaria-in) (@MichaelDello)

Diarrhoea seems like a large problem because more people die of it per year (or did so in 2015). The remedy is apparently "oral rehydration therapy: a large pinch of salt and a fistful of sugar dissolved in a jug of clean water."

_Note_ : GiveWell has moved slowly and cautiously on this topic, but Evidence Action's Dispensers for Safe Water program is now a GiveWell Standout charity.

**7\. Fighting Fistulae**

- [Question][ _Can it be more cost-effective to prevent than to treat obstetric fistulas?_](https://forum.effectivealtruism.org/posts/mRHH8TECAnaEkXmRK/can-it-be-more-cost-effective-to-prevent-than-to-treat-2) (@brb243)

The author suggests a way of preventing fistulas which may be much cheaper than surgery: “targeting midwives to share information on when to seek specialized care and identify at-risk patients, training doctors at government (free of charge) clinics, providing equipment, and potentially offering travel stipend to extremely poor households”.

**8\. International Supply Chain Accountability**

_Related categories_ : Politics: System change, targeted change, policy reform.

- [ _New Cause Area Proposal: International Supply Chain Accountability_](https://forum.effectivealtruism.org/posts/ME4zE34KBSYnt6hGp/new-top-ea-cause-international-supply-chain-accountability) (@NunoSempere)

Workers' organizations can lobby international companies to adopt better labour conditions across their supply chain, and to get the original companies to pay for these efforts. A particularly promising strategy is to apply pressure in the countries these companies originate from (Spain, Germany, the US), rather than in the countries where the products are made. This seems to be working for the case of Inditex (Zara, and various other textile brands). It is unclear how, and if, EA might get organizations working in this area to accept external funds, but they could in principle absorb a lot of them.

_Note_ : I'm the author of this post.

**9\. Chloramphenicol for Heart Attacks**

- [ _Chloramphenicol as intervention in heart attacks_](https://forum.effectivealtruism.org/posts/KuZ7mwrmS9ZAmqtnM/chloramphenicol-as-intervention-in-heart-attacks) (@G Gordon Worley III)

The article linked suggests approving Chloramphenicol as a coronary treatment, which is claimed to be a fixed cost of "$25 million spent once to save 400,000 lives per year in the U.S. alone." Comments point out that the estimate "seems to be based on one study of 21 pigs."

**10\. COVID-19**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/coronavirus), which contains more cause candidates. Here are some examples included for illustration purposes:

- [ _Is rapid diagnostic testing (RDT), such as for coronavirus, a neglected area in Global Health?_](https://forum.effectivealtruism.org/posts/Rwbd772QcugNv4e5x/is-rapid-diagnostic-testing-rdt-such-as-for-coronavirus-a) (@Ramiro)
- [ _Customized COVID-19 risk analysis as a high value area_](https://forum.effectivealtruism.org/posts/q3v8CpAiuNhZzJ7Gt/customized-covid-19-risk-analysis-as-a-high-value-area) (@Askell)
- [ _Responding to COVID-19 in India_](https://forum.effectivealtruism.org/posts/juwNwpvHcHcH2dRzB/responding-to-covid-19-in-india) (@Suvita)
- [ _Coronavirus Research Ideas for EAs_](https://forum.effectivealtruism.org/posts/AcksHPwQupvPRKcZm/coronavirus-research-ideas-for-eas) (@Peter_Hurford)
- [ _Coronavirus and long term policy [UK focus]_](https://forum.effectivealtruism.org/posts/ZvfG9BDg8GowCcacR/coronavirus-and-long-term-policy-uk-focus) (@weeatquince)

**11\. Vaccines**

- [ _EA Should Spend Its “Funding Overhang” on Curing Infectious Diseases_](https://forum.effectivealtruism.org/posts/maWneZjzQpigAFKPZ/ea-should-spend-its-funding-overhang-on-curing-infectious) (@joshcmorrison)

The author argues that “funding overhang” should be spent developing vaccines against infectious diseases:

“If EA’s investing $10 billion in vaccination over the next ten years could save the equivalent of 3-5 years of disease burden of a disease like tuberculosis, it would represent a cost per disability-adjusted-life-year (DALY) saved of roughly $50-$85 (on par with GiveWell top charities).”

**12\. Clean Cookstoves**

- [ _Clean cookstoves may be competitive with GiveWell-recommended charities_](https://forum.effectivealtruism.org/posts/cz85mufYwiiukpowD/clean-cookstoves-may-be-competitive-with-givewell) (@Suvita)

This is a very quick, rough model of the cost-effectiveness of promoting clean cookstoves in the developing world. It suggests that:

"If a clean cookstove intervention is successful, it may have roughly the same ballpark of cost-effectiveness as a GiveWell-recommended charity.

Circa 90% of the impact comes from directly saving lives, based on a model which estimated both the number of lives saved and the impact on climate change."

**13\. Agricultural R &D**

- [ _Agricultural research and development_](https://forum.effectivealtruism.org/posts/3a3viueN5DA2jwxCu/agricultural-research-and-development) (@David_Goll)

“In combination, the difficulties with estimating the effects of R&D and the potential barriers to adoption suggest that the estimated benefit-cost ratios reported earlier are likely to be upwardly biased. The benefit-cost ratios estimated are also lower than those associated with Giving What We Can’s currently recommended charities. For instance, the $304 per QALY estimate based on the Copenhagen Consensus benefit-cost ratio, which appears to be at the higher end of the literature, compares unfavourably to GiveWell’s baseline estimate of $45 to $115 per DALY for insecticide treated bednets (GiveWell, 2013). The benefit-cost ratios also appear to be lower than those associated with micronutrient supplements, as discussed earlier. While there are significant benefits that remain unquantified within agricultural R&D, the same is also true for interventions based on bednet distribution, deworming and micronutrient supplements. As a result, while this area could yield individual high impact opportunities, the literature as it stands does not seem to support the claim that agricultural R&D is likely to be more effective than the best other interventions.”

**14\. Golden Rice**

- [ _Should GMOs (e.g. golden rice) be a cause area?_](https://forum.effectivealtruism.org/posts/AF8hvNXFqhZsDmrTc/should-gmos-e-g-golden-rice-be-a-cause-area) (@mariushobbhahn)

“In this post, I want to very roughly ​​evaluate whether golden rice should be of interest to EAs and whether genetically modified organisms (GMOs) in general are worth investigating deeper.”

The author concludes that this cause is valuable, though acknowledges that golden rice wouldn't allow to reach levels of efficiency comparable to GiveWell top charities.

**15\. Agricultural Land Redistribution**

- [ _Intervention report: Agricultural land redistribution_](https://forum.effectivealtruism.org/posts/LempBhdJe6HzwtDxd/intervention-report-agricultural-land-redistribution) (@David Rhys Bernard & @Jason Schukraft)

The authors conclude that advocating for agricultural land redistribution is neither tractable nor cost-effective.

**16\. Ventilation**

- [ _Cost-Effectiveness of Air Purifiers against Pollution_](https://forum.effectivealtruism.org/posts/umzu3RGBBhA3fefhw/cost-effectiveness-of-air-purifiers-against-pollution) (@Lukas Trötzmüller)

"The goal for this post is to give an introduction into the human health effects of air pollution, encourage further discussion, and evaluate an intervention: The use of air purifiers in homes. These air purifiers are inexpensive, standalone devices not requiring any special installation procedure. A first analysis suggests that the cost-effectiveness of this intervention is two orders of magnitude worse than the best EA interventions. However, it is still good enough to qualify as an ’effective’ or even ‘highly effective’ health intervention according to WHO criteria."

- [ _How a ventilation revolution could help mitigate the impacts of air pollution and airborne pathogens_](https://forum.effectivealtruism.org/posts/PQK52rfMyLFGkHmrt/how-a-ventilation-revolution-could-help-mitigate-the-impacts) (@Mike Cassidy)

Indoor air pollution can be worse than outdoor pollution, yet it is neglected. Installing ventilation and filtration systems in our buildings would reduce economic losses arising from air pollution and respiratory viruses.

**17\. Stubble Burning in India**

- [ _Stubble Burning in India_](https://forum.effectivealtruism.org/posts/s82X4ta6ucaPYRf9S/notes-stubble-burning-in-india) (@Jason Schukraft)

Stubble burning in north India is a major contributor to seasonal decreases in ambient air quality [...] Stubble burning releases carbon dioxide, carbon monoxide, nitrogen oxides, sulfur oxides, and methane as well as particulate matters (PM10and PM2.5) ([ _Abdurrahman, Chaki, & Saini 2020_](https://doi.org/10.1016/j.envadv.2020.100011)). These pollutants affect the immediate area and also drift southeast to Delhi, smothering the city of ~22 million in thick haze. At their peak, these fires are responsible for ~58% of Delhi air pollution ([ _Beig et al. 2020_](https://doi.org/10.1016/j.scitotenv.2019.136126)). The consequences of this air pollution include skin and eye irritation, respiratory problems (dry cough, wheezing, breathlessness, chest discomfort, asthma), and hypertension ([ _Rizwan, Nongkynrih, & Gupta 2013_](https://dx.doi.org/10.4103%2F0970-0218.106617)). Air pollution is estimated to be responsible for at least 48,000 premature deaths in Delhi alone in 2020 ([ _Greenpeace, n.d._](https://www.greenpeace.org/international/campaign/tracking-cost-air-pollution/)).[ _[5]_](https://forum.effectivealtruism.org/posts/s82X4ta6ucaPYRf9S/notes-stubble-burning-in-india#fn-25nfjvHiNoZfr6u49-5) Nationwide, the open burning of agricultural residue is estimated to be responsible for more than 66,000 premature deaths in India ([ _GBD MAPS Working Group 2018_](https://www.healtheffects.org/system/files/GBD-MAPS-SpecRep21-India-revised_0.pdf)).[ _[6]_](https://forum.effectivealtruism.org/posts/s82X4ta6ucaPYRf9S/notes-stubble-burning-in-india#fn-25nfjvHiNoZfr6u49-6)

**18\. Starvation in Afghanistan**

- [Linkpost][ _Millions face starvation in Afghanistan_](https://forum.effectivealtruism.org/posts/ysZRpArx5sg5c4kN5/linkpost-millions-face-starvation-in-afghanistan) (@aogara)

Since the Taliban seized power, US sanctions and the sudden suspension of foreign aid worsened the situation in Afghanistan to the extent that millions of people are at risk of starvation and death.

**19\. Water, Sanitation and Hygiene Interventions**

- [ _If you (mostly) believe in worms, what should you think about WASH?_](https://forum.effectivealtruism.org/posts/FAA22RbfgC68fRnRs/if-you-mostly-believe-in-worms-what-should-you-think-about) (@alexrjl)

According to GiveWell's research, the overwhelming majority of the value of mass deworming interventions (DW) comes from expected long-term economic effects rather than short-term effects on health. The mechanism by which these long-term effects occur is unclear, especially as the health effects are so small.

The best WASH interventions (in particular, Dispensers for Safe Water, but possibly also Development Media International) have larger health effects than DW.

If the long-term effects of deworming are related to the health effects of worms, it is likely that the long-term economic effects of WASH interventions are at least as good. If the effects are somehow specific to worms, given that a significant part of the benefit of WASH is in preventing parasitic worm infestation, there should still be significant long-term effects of WASH interventions.

**20\. Research on Inbreeding**

- [ _Inbreeding and global health & development_](https://forum.effectivealtruism.org/posts/kBXcwroun6xv46DBa/inbreeding-and-global-health-and-development) (@pafnuty)

“Inbreeding (also known as consanguinity) is associated with an increased risk of adverse prenatal outcomes including stillbirths, low birth weight, preterm delivery, abortion, infant and child mortality, congenital birth defects, cognitive impairments, malformations and many other complex disorders. . . . [R]esearch on this issue in the context of global health and development is scarce, and additional research might generate ample information value about potentially impactful interventions.”

**21\. Stopping Miscarriages**

- [ _Might stopping miscarriages be a very important cause area?_](https://forum.effectivealtruism.org/posts/F4CfKz9cfhLn9jPuu/might-stopping-miscarriages-be-a-very-important-cause-area) (@SaraAzubuike)

The author implies that stopping miscarriages could be important (if there’s some probability that embryos are human), given that miscarriages occur in 20% of pregnancies.

**22\. Advocacy for Legalizing Abortion**

- [Question][ _Developing countries and adolescent pregnancy: how effective could advocacy for legalizing abortion be?_](https://forum.effectivealtruism.org/posts/uvw7M7c7fEfatRwxg/developing-countries-and-adolescent-pregnancy-how-effective-4) (@Ramiro)

Adolescent pregnancy is associated with high rates of child mortality. The author advances that advocacy for legalizing abortion may be an effective way to prevent this tragedy in developing countries.

**23\. Drug Legalisation**

- [ _Ending The War on Drugs - A New Cause For Effective Altruists?_](https://forum.effectivealtruism.org/posts/7WLasmb9R2DQgDorm/ending-the-war-on-drugs-a-new-cause-for-effective-altruists) (@MichaelPlant)

Moving from drug prohibition to legalisation would be beneficial to drug users (decriminalisation) and drug-producing and trafficking countries (less violence). The author raises the question of whether this could be an area to be prioritized.

**24\. Patent Policy**

- [ _Global Health Innovation Incentives, Patent Trolls, and Evergreening: Discussion of Subtopics within US Patent Policy_](https://forum.effectivealtruism.org/posts/ZFpZgy8jEZ55qieY7/global-health-innovation-incentives-patent-trolls-and) (@schethik)

This post covers three candidates within patent policy: The first is **global health innovation incentives** :

“Alternative innovation finance mechanisms—such as advanced market commitments and the Health Impact Fund—can help incentivize firms to invest in R&D aimed at helping developing countries’ poorest people. The present patent system, on the other hand, provides limited incentive to create innovations for these people.”

The second candidate is **patent trolling** : Some firms' merely buy patents and sue others for infringing on their rights, without really producing anything themselves. These patent trolls cost money to other firms, which therefore turn hesitant to use technology, and unwilling to innovate.

“However, many legislative and judicial steps have been taken since 2013 to address patent trolling in the US, making the issue—in our view—presently low in scale, neglectedness, and tractability.”

The third is **evergreening** , which doesn't seem to be a high priority either:

“It does not appear that companies unfairly extend (i.e., evergreen) their patent terms using statutory strategies. However, there is reason to believe companies use other means such as the 30-month stay provision to extend effective market monopolies.”

The author also recommends further research into this area.

**25\. Training Economists**

- [ _Hits-based development: funding developing-country economists_](https://forum.effectivealtruism.org/posts/geDd86p6C6a2pkZXr/hits-based-development-funding-developing-country-economists) (@Michael_Wiebe)

“One specific mechanism [for promoting growth] is to train developing-country economists, who then work in government and influence policy in a pro-growth direction, ultimately increasing the probability of a growth episode.”

**26\. Improving Welfare Algorithms**

- [Link][ _Improving the lives of millions of Latin Americans through better welfare targeting algorithms_](https://forum.effectivealtruism.org/posts/25PdnAsMPaepRAh5o/improving-the-lives-of-millions-of-latin-americans-through) (@NORIEGA)

“More than 50 million people in Latin America are impacted by the decision of very simple linear algorithms which determine how much welfare they receive from social programs. Simple changes to the algorithm lead to hundreds of thousands of people being added or removed to major welfare programs.”

The author holds that improving these algorithms would allocate billions of dollars more effectively.

**27\. Low Back Pain**

- [ _Preventing low back pain with exercise_](https://forum.effectivealtruism.org/posts/swwgCnaxbzSupv6vZ/preventing-low-back-pain-with-exercise) (@Ryan Kidd)

This post argues that exercise seems to be the most effective treatment to prevent low back pain, which is a symptom experienced by people of all ages and socioeconomic circumstances. A comment by[ _Aaron_](https://forum.effectivealtruism.org/users/aaron-gertler) suggests that this might be a solid cause area in the developing world.

**28\. Chronic Pain**

- [ _Should Chronic Pain be a cause area?_](https://forum.effectivealtruism.org/posts/qFgCg94gGBqrXni7N/should-chronic-pain-be-a-cause-area) (@mariushobbhahn)

This post gives an overview of what chronic pain is, and its relation with demographic and environmental factors. It finally discusses whether it could be a worthy cause area, reaching no conclusion.

**29\. Intactivism**

- [ _Intactivism as a potential Effective Altruist cause area?_](https://forum.effectivealtruism.org/posts/jtG75XvwajobTT7qB/intactivism-as-a-potential-effective-altruist-cause-area) (@Question Mark)

The author argues against the practice of circumcision and proposes its abolition.

**30\. Delaying Aging**

- [ _Work Test for Charity Entrepreneurship: Delaying Aging_](https://forum.effectivealtruism.org/posts/kiYxCuqMWCz2j8KxS/work-test-for-charity-entrepreneurship-delaying-aging) (@Heye Groß)

This post argues that aging is the most common cause of death and human suffering. There are already known effective interventions (exercise, fighting smoking) against accelerated aging. For this reason, research confirming that aging itself is responsible for aging-related diseases could yield many cost-effective programs.

**31\. Health in Younger Generations**

- [ _The health of millennials_](https://forum.effectivealtruism.org/posts/BGKeAiTZPFvYT5kRd/the-health-of-millennials) (@Michael_2358)

Inspired by a study on the health of the millennials, the author advances that mental and physical health might be deteriorating in younger generations. This idea is only proposed as a subject for future research.

**32\. Charter Cities**

- [ _Intervention Report: Charter Cities_](https://forum.effectivealtruism.org/posts/EpaSZWQkAy9apupoD/intervention-report-charter-cities) (@David Rhys Bernard & @Jason Schukraft)

A comprehensive report on the subject. Conclusions are pessimistic, given the uncertainties involved, but the authors state that further research could be valuable at a modest cost.

- [ _Further thoughts on charter cities and effective altruism_](https://forum.effectivealtruism.org/posts/9oyHip2JCyjdLPhEs/further-thoughts-on-charter-cities-and-effective-altruism) (@marklutter)

This is a defense of charter cities and a reply to the foregoing report.

**33\. Alleviating Price Risk**

- [ _Want to alleviate developing world poverty? Alleviate price risk.​ (2018)_](https://forum.effectivealtruism.org/posts/cDRtP5TxbrpuQBmZ8/want-to-alleviate-developing-world-poverty-alleviate-price) (@RomeoStevens)

This post is an excerpt from[ _this piece_](https://medium.com/greyswandigital/want-to-alleviate-developing-world-poverty-alleviate-price-risk-39958aad8359) by Peter Harrigan. It calls attention to the idea that price risk is one of the more overlooked sources of poverty. Third world farmers face constant risk from price volatility, which reduces their profits and leads them to bankruptcy.

**34\. Fighting Corruption**

- [ _Fighting corruption in aid-embezzling_](https://forum.effectivealtruism.org/posts/xmsEgHazbRPD7LhB4/fighting-corruption-in-aid-embezzling) (@MarcSerna)

This post estimates that aid-embezzling in developing countries could cut “from 10% to 50% of donations received by charitable organizations in humanitarian and development settings”. It proposes the creation of an organization dedicated to do audits of development and humanitarian projects in such countries.

**35\. Lead Exposure**

- [ _Global lead exposure report_](https://forum.effectivealtruism.org/posts/naTwu3xD3WFWu5fbp/global-lead-exposure-report) (@David Rhys Bernard & @Jason Schukraft)

This is a comprehensive report on the problem of lead exposure. The authors conclude that it is neglected and deserves more attention among effective altruists leaning towards neartermist interventions.

**36\. Fungal Diseases**

- [ _Antifungal Resistance - The Neglected Cousin of Antibiotic Resistance_](https://forum.effectivealtruism.org/posts/NHJRmX9tqYo7HiDdp/antifungal-resistance-the-neglected-cousin-of-antibiotic) (@Madhav Malhotra)

This post links to an interview with Marcio Rodrigues, an expert in the field, about the importance and neglectedness of fungal diseases.

### **Global Health and Development: Mental Health**

_Related categories_ : States of consciousness.

_Pointer_ : This cause candidate has two related EA Forum tags:[ _Mental Health (Cause Area)_](https://forum.effectivealtruism.org/topics/mental-health-cause-area) and[ _Subjective Well-Being_](https://forum.effectivealtruism.org/topics/subjective-well-being). For illustration purposes:

- [ _Cause profile: mental health_](https://forum.effectivealtruism.org/posts/XWSTBBH8gSjiaNiy7/cause-profile-mental-health) (@MichaelPlant)

"Not only does mental illness seem to cause as much, if not more, total worldwide unhappiness than global poverty, it also seems far more neglected. Effective mental health interventions exist currently. These have been improving over time and we can expect further improvements. I estimate the cost-effectiveness of a particular mental health organisation, StrongMinds, and claim it is (at least)four times more effective per dollar than GiveDirectly, a GiveWell recommended top charity. This assumes we understand cost-effectiveness in terms of happiness, as measured by self-reported life satisfaction [...] Even if mental health is a large-scale, neglected problem, we shouldn't consider it a possible moral priority if there aren't effective treatments. Fortunately, there are."

- [ _HLI's Mental Health Programme Evaluation Project - Update on the First Round of Evaluation_](https://forum.effectivealtruism.org/posts/uzLRw7cjpKnsuM7c3/hli-s-mental-health-programme-evaluation-project-update-on) (@Jasper Synowski)

The project, which seems to be ongoing, tries to systematically assess a long list of mental health interventions.

Initially, various EAs proposed varied experimental mental health interventions. There are a number of posts asking if "mental health issue X" should fall within Effective Altruism's purview. Of these, mental health apps represent probably the most well-argued intervention and stand on a class of their own. In particular, they are scalable.

- [ _"Fixing Adolescence" as a Cause Area?_](https://forum.effectivealtruism.org/posts/WJzxnrxRFZPypZezq/fixing-adolescence-as-a-cause-area) (@kirchner.jan)

Adolescence comes frequently with substantial suffering. After analyzing abundant data, and pointing out the lack of strategies to tackle this problem, the author suggests that more research is desirable to establish this as a cause area.

- [Link][ _Preprint is out! 100,000 lumens to treat seasonal affective disorder_](https://forum.effectivealtruism.org/posts/bwhDhZQvbEcG4FEb8/preprint-is-out-100-000-lumens-to-treat-seasonal-affective) (@Fabienne)

“Seasonal affective disorder (SAD) is common and debilitating. The standard of care includes light therapy provided by a light box; however, this treatment is restrictive and only moderately effective. Advances in LED technology enable lighting solutions that emit vastly more light than traditional light boxes. Here, we assess the feasibility of BROAD (Bright, whole-ROom, All-Day) light therapy and get a first estimate for its potential effectiveness.”

- [ _Sex work as part of mental health and wellbeing services_](https://forum.effectivealtruism.org/posts/HX8Nh8daXQdXn57x7/sex-work-as-part-of-mental-health-and-wellbeing-services) (@Mary)

This post argues that instead of trying to discourage sex workers, there is a number of reasons for which “it is worth considering integrating this profession more into society”:

“Sex workers satisfy a very essential need, providing not only sexual intercourse but also company, a listening ear, a safe space where is no judgment. Otherwise dangerous paraphilias can be safely practiced, believed to be shameful wants can be satisfied, never said fantasies can be discussed. Victims of sexual abuse, people with mental health conditions, couples with sexual problems can not only talk or discuss their problems, as it would be possible in a clinical setting but can also receive practical help too. All of these attributes make sex work a potentially valuable addition to mental health and wellbeing services.”

- Mental health apps:[ **_Mind Ease: a promising new mental health intervention_**](https://forum.effectivealtruism.org/posts/kuZz3aB6Z7tciEhG5/mind-ease-a-promising-new-mental-health-intervention) (@PeterBrietbart)
  - See also:[ \__\*\*\_Ineffective entrepreneurship: post-mortem of Hippo, the happiness app that never quite was_\*\*](https://forum.effectivealtruism.org/posts/KhwiyLpJmW6fcAuuo/ineffective-entrepreneurship-post-mortem-of-hippo-the) (@MichaelPlant)
- Preventing/Curing Trauma:[ **_Is trauma a potential EA cause area?_**](https://forum.effectivealtruism.org/posts/4Xb7mLRCh6GExtW6w/is-trauma-a-potential-ea-cause-area) (@nonzerosum)
- Preventing Child Abuse:[ **_Is preventing child abuse a plausible Cause X?_**](https://forum.effectivealtruism.org/posts/C5diBK7sJmoYWdrCs/is-preventing-child-abuse-a-plausible-cause-x) (@Milan_Griffes)
- Anti-tribalism:[ **_Anti-tribalism and positive mental health as high-value cause areas_**](https://forum.effectivealtruism.org/posts/Qgq4zJPzR9TCJ89wj/anti-tribalism-and-positive-mental-health-as-high-value) (@Kaj_Sotala)
- Insomnia:[ **_Insomnia: a promising cure_**](https://forum.effectivealtruism.org/posts/q8g2MXQCmKoYhEjsT/insomnia-a-promising-cure) (@Halstead)
- Sleep loss:[ **_Should we consider the sleep loss epidemic an urgent global issue?_**](https://forum.effectivealtruism.org/posts/G6aZMjXBke326WJLp/should-we-consider-the-sleep-loss-epidemic-an-urgent-global) (@orenmn)
- Mindfulness Based Stress Reduction:[ **_Cost Effectiveness of Mindfulness Based Stress Reduction_**](https://forum.effectivealtruism.org/posts/gkbpbSzEaEteF8FSm/cost-effectiveness-of-mindfulness-based-stress-reduction) (@Elizabeth)

## **States of Consciousness.**

**1\. Psychedelics**

_Related categories_ : Global Health and Development: Mental Health.

- [ _Cash prizes for the best arguments against psychedelics being an EA cause area_](https://forum.effectivealtruism.org/posts/zwno3Gxb8p6DmfadP/cash-prizes-for-the-best-arguments-against-psychedelics) (@Milan_Griffes)

The post makes the case from an EA perspective and offers a cash prize for counter-arguments.

**2\. Fundamental Consciousness Research**

- [ _Principia Qualia: blueprint for a new cause area, consciousness research with an eye toward ethics and x-risk_](https://forum.effectivealtruism.org/posts/kxHRn7Lye6FdQ3tEE/principia-qualia-blueprint-for-a-new-cause-area) (@MikeJohnson)

"...if your goal is to reduce suffering, it's important to know what suffering is."

**3\. Increasing Access to Pain Relief (Opioids) in Developing Countries**

_Related categories_ : Global Health and Development. Politics: System change, targeted change, policy reform.

- [ _Increasing Access to Pain Relief in Developing Countries - An EA Perspective_](https://forum.effectivealtruism.org/posts/nsCFsRjfW6b72gJuB/increasing-access-to-pain-relief-in-developing-countries-an) (@Lee_Sharkey)

Access to opioids is unduly restricted, such that the pain of some deaths can amount to "torture by omission". The author suggests, as a tentative donation target, the Pain and Policy Studies Group of the University of Wisconsin-Madison which "runs 'International Pain Policy Fellowships', which train national champions of the cause to identify and overcome barriers to the use of opioids in their countries. The programme has had numerous in-country successes." However, the program seems to now be defunct. One organization that I personally perceive as promising, which is working in this space, is[ _The Organisation for the Prevention of Intense Suffering_](https://www.preventsuffering.org/#about-opis).

**4\. Cluster Headaches**

- [ _OPIS initiative on access to psilocybin for cluster headaches_](https://forum.effectivealtruism.org/posts/wfXrMmKcD6eLEbS6R/opis-initiative-on-access-to-psilocybin-for-cluster) (@jonleighton)

"Cluster headaches are considered one of the most excruciating conditions known to medicine..."; "there is [...] evidence that psilocybin mushrooms can prevent and abort entire episodes. Such evidence has been published as survey data and is also widely reported by patients in cluster headache groups. TwoPhase I RCTs are ongoing and should add to the existing evidence for efficacy. Lack of access to psilocybin mushrooms and widespread information about using them are key barriers to effective treatment for many patients."

**5\. Drug Policy Reform**

_Related categories:_ Politics: System change, targeted change, policy reform.

- [ _High Time For Drug Policy Reform_](https://forum.effectivealtruism.org/posts/wu9nEXWtvhEnYQTxG/high-time-for-drug-policy-reform-part-1-4-introduction-and) (@MichaelPlant)

"In the last 4 months, I've come to believe drug policy reform, changing the laws on currently illegal psychoactive substances, may offer a substantial, if not the most substantial, opportunity to increase the happiness of humans alive today."

**6\. Love**

- [ _Love seems like a high priority_](https://forum.effectivealtruism.org/posts/qar8rGhomyNsQC85z/love-seems-like-a-high-priority) (@kbog)

"Making it possible for people to deliberately fall in love seems like a high priority, competitive with good short- and medium-term causes such as malaria prevention and anti-aging. However, there is little serious work on it."

**7\. Universal Euphoria**

- [ _Happy animal farm — Universal euphoria_](https://forum.effectivealtruism.org/posts/wtNCs2TgtDpu3W7Ke/charities-i-would-like-to-see#High_Leverage_Values_Spreading) (@Michael Dickens)
- [ _Hedonium_](https://www.lesswrong.com/tag/orgasmium) (Less Wrong tag page)
- [ _Wireheading_](https://www.lesswrong.com/tag/wireheading) (Less Wrong tag page)
- "Rats on heroin" thought experiment
- [ _The Tails Coming Apart As Metaphor For Life_](https://slatestarcodex.com/2018/09/25/the-tails-coming-apart-as-metaphor-for-life/)

Compressing as much happiness into a unit of matter can be pursued at all levels of technological development. With current technology, we could have animal farms dedicated to making rats, about which we know a fair bit, maximally happy. With future technology, we could have computer simulations of maximal bliss.

The idea is sometimes thought to be morally repugnant or philosophically misguided, and a quick Fermi estimate suggests that current happy animal farms would not be cost effective compared to interventions in the developing world.

## **Space**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/space).

_Related categories_ : Existential risk, Transhumanism, Politics: System change, targeted change, policy reform.

**1\. Space Colonization**

- [ _What analysis has been done of space colonization as a cause area?_](https://forum.effectivealtruism.org/posts/Wwotfu2pz4bLPRNYg/what-analysis-has-been-done-of-space-colonization-as-a-cause) (@reallyeli)
- [ _The Case for Space: A Longtermist Alternative to Existential Threat Reduction_](https://forum.effectivealtruism.org/posts/DKY5qedLxLhSab7XF/the-case-for-space-a-longtermist-alternative-to-existential) (@Giga)
- [ _An Informal Review of Space Exploration_](https://forum.effectivealtruism.org/posts/xxcroGWRieSQjCw2N/an-informal-review-of-space-exploration#comments) (@kbog)

If we had a backup planet, existential risk would be reduced. Further, we'd be able to have more people. However, even with a backup planet, existential risk in both planets would be correlated, and the protection from extinction that the second planet provides would be inversely proportional to the degree of correlation. One might expect this correlation to be particularly high for hostile AI. See[ _here_](https://forum.effectivealtruism.org/posts/GseREh8MEEuLCZayf/nunosempere-s-shortform?commentId=Qk2Scyv2sdgAWP9CD) for some discussion on these points.

User @kbog looked at this issue in[ _more depth_](https://forum.effectivealtruism.org/posts/xxcroGWRieSQjCw2N/an-informal-review-of-space-exploration#comments), and concluded that:

In this post I take a serious and critical look at the value of space travel. Overall, I find that the value of space exploration is dubious at this time, and it is not worth supporting as a cause area, though Effective Altruists may still want to pay attention to the issue. I also produce specific recommendations for how space organizations can rebalance their operations to have a better impact.

**2\. Space Governance**

- [ _Space governance is important, tractable and neglected_](https://forum.effectivealtruism.org/posts/QkRq6aRA84vv4xsu9/space-governance-is-important-tractable-and-neglected) (@Tobias_Baumann)

"I argue that space governance has been overlooked as a potentially promising cause area for longtermist effective altruists. While many uncertainties remain, there is a reasonably strong case that such work is important, time-sensitive, tractable and neglected, and should therefore be part of the longtermist EA portfolio [...] The work I have in mind aims to replace the current state of ambiguity with a coherent framework of (long-term) space governance that ensures good outcomes if and when large-scale space colonisation becomes feasible."

## **Education**

_Related categories_ : Global Health and Development.

**1\. Global Basic Education**

- [ _Global basic education as a missing cause priority_](https://forum.effectivealtruism.org/posts/pe7QHjMpMuxT8YTir/global-basic-education-as-a-missing-cause-priority) (@lucy.ea8)

The post could use some work, but I can imagine both of its points being true: education has intrinsic value (all things being equal, we want to have more education), and extrinsic value (it is somewhat correlated with health outcomes, and economic productivity).

**2\. Philosophy in Schools**

- [ _Are we neglecting education? Philosophy in schools as a longtermist area_](https://forum.effectivealtruism.org/posts/Z64fKxmEP9YjHNAad/are-we-neglecting-education-philosophy-in-schools-as-a) (@jackmalde)

"In this post I consider the possibility that the Effective Altruism (EA) movement has overlooked the potential of using pre-university education as a tool to promote positive values and grow the EA movement. Specifically, I focus on evaluating the potential of promoting the teaching of philosophy in schools."

## **Climate Change**

_Related categories_ : Politics: System change, targeted change, policy reform. Politics: Culture war.

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/climate-change). For illustration purposes:

**1\. General**

- [ _Does climate change deserve more attention within EA?_](https://forum.effectivealtruism.org/posts/BwDAN9pGbmCYZGbgf/does-climate-change-deserve-more-attention-within-ea) (@Louis_Dixon)
- [ _Global development interventions are generally more effective than climate change interventions_](https://forum.effectivealtruism.org/posts/GEM7iJnLeMkTMRAaf/updated-global-development-interventions-are-generally-more) (@HaukeHillebrandt)
- [ _Review of Climate Cost-Effectiveness Analyses_](https://forum.effectivealtruism.org/posts/ynRG6JBvARS2cHu63/review-of-climate-cost-effectiveness-analyses) (@mchr3k)
- [ _Climate Change Is Neglected By EA_](https://forum.effectivealtruism.org/posts/pcDAvaXBxTjRYMdEo/climate-change-is-neglected-by-ea) (@mchr3k)

Most notably, climate change has a long tail of bad outcomes, and it impacts more than just GDP, as previously modelled.

_Note_ : The disagreement about whether EA should give more attention to climate change is probably older than any of these posts.

**2\. Public R &D to Deal With Climate Change**

- [ _Vox article_](https://forum.effectivealtruism.org/posts/j7fuAbkPiPuPCegou/the-climate-change-policy-with-the-most-potential-is-the) (@Henry_Stanley)

**3\. Leveraging the Climate Change Movement**

- [ _Taking advantage of climate change concerns to channel donations to EA-recommended organizations at low marginal cost (proposal and call for more research)_](https://forum.effectivealtruism.org/posts/jdLomLk3F9vH85j6i/taking-advantage-of-climate-change-concerns-to-channel) (@ianps)

"This willingness to act seems to be mostly tied to climate change and cannot be easily directed towards more effective causes. Therefore, I think EAs could influence existing concerns and willingness to act on climate change to direct funds/donations towards cost-effective organizations (i.e., CfRN, CATF)with relatively low investment of time."

**4\. Extinguishing or Preventing Coal Seam Fires**

- [ _Extinguishing or preventing coal seam fires is a potential cause area_](https://forum.effectivealtruism.org/posts/2nrx8GdtobScoAZF8/extinguishing-or-preventing-coal-seam-fires-is-a-potential) (@kbog)

"Much greenhouse gas emissions comes from uncontrolled underground coal fires. I can't find any detailed source on its share of global CO2 emissions; I see estimates for both 0.3% and 3% quoted for coal seam fires just in China, which is perhaps the world's worst offender. Another rudimentary calculation said 2-3% of global CO2 emissions comes from coal fires. They also seem to have pretty bad local health and economic effects, even compared to coal burning in a power plant (it's totally unfiltered, though it's usually diffuse in rural areas). There are some methods available now and on the horizon to try and put the fires out, and some have been practiced - see the Wikipedia article. However, the continued presence of so many of these fires indicates a major problem to be solved with new techniques and/or funding for the use of existing techniques."

**5\. Paris-Compliant Offsets**

- [ _Paris-compliant offsets - a high leverage climate intervention?_](https://forum.effectivealtruism.org/posts/RvCvQqy46iyQkk2mq/paris-compliant-offsets-a-high-leverage-climate-intervention) (@Louis_Dixon)

"We should be rapidly exploring higher quality and more durable offsets. If adopted, these principles could be a scalable and high-leverage way of moving organisations towards net-zero."

**6\. Help coral reefs survive climate change**

- [ _Trying to help coral reefs survive climate change seems incredibly neglected_](https://forum.effectivealtruism.org/posts/YEkyuTvachFyE2mqh/trying-to-help-coral-reefs-survive-climate-change-seems). (@capybaralet)

## **7\. CO2 Sensors**

- [Question][ _Any initiative/zo introduce small and cheap CO2 sensors?_](https://forum.effectivealtruism.org/posts/waWQCL7kHARLcNEdw/any-initiative-zo-introduce-small-and-cheap-co-sensors) (@Martin (Huge) Vlach)

The idea here is to raise awareness about high CO² levels by introducing sensors in smartphones and similar devices.

## **8\. Hurricanes**

- [ _Seeking a Collaboration to Stop Hurricanes?_](https://forum.effectivealtruism.org/posts/Jsz7bMzAZsh3hkSEL/seeking-a-collaboration-to-stop-hurricanes) (@Anthony Repetto)

This post proposes to stop hurricanes as a way to avoid the damages caused by them. As high surface temperatures are a necessary condition for hurricanes, cooling them down would prevent their formation, which might be achieved by regularly provoking water spouts (that is, “30mph 'humidity tornadoes' over hot waters”) with the help of a special device described by the author.

## **Existential and Global Catastrophic Risks**

_Pointer_ : This cause has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/existential-risk). More cause candidates may be found there, or in the related[ _AI Alignment_](https://forum.effectivealtruism.org/topics/ai-alignment),[ _AI Governance_](https://forum.effectivealtruism.org/topics/ai-governance) and[ _Civilizational Collapse & Recovery_](https://forum.effectivealtruism.org/topics/civilizational-collapse-and-recovery) tags.

**1\. Corporate Global Catastrophic Risks**

- [ _Corporate Global Catastrophic Risks (C-GCRs)_](https://forum.effectivealtruism.org/posts/vy2QCTXfWhdiaGWTu/corporate-global-catastrophic-risks-c-gcrs-1) (@HaukeHillebrandt)

"It might be useful to think of corporations as dangerous optimization demons which will cause GCRs if left unchecked by altruism and philanthropy."

Comments present a different perspective.

**2\. Aligning Recommender Systems**

Pointer: See the related[ _Near-Term AI Ethics_](https://forum.effectivealtruism.org/topics/near-term-ai-ethics) tag.

- [ _Aligning Recommender Systems as Cause Area_](https://forum.effectivealtruism.org/posts/xzjQvqDYahigHcwgQ/aligning-recommender-systems-as-cause-area) (@IvanVendrov)

"In this post we argue that improving the alignment of recommender systems with user values is one of the best cause areas available to effective altruists, particularly those with computer science or product design skills."

**3\. Surveillance**

- [ _The case for studying stylometric deanonymisation as surveillance tech_](https://forum.effectivealtruism.org/posts/nm2EczMBm99AZn5JK/the-case-for-studying-stylometric-deanonymisation-as) (@acylhalide)

Given the seriousness of surveillance tech, which can stabilise totalitarian regimes and destabilise democratic ones, this post proposes to fund advanced AI-based stylometrics research to see how far it can be developed and to create awareness about whatever are the results of this research.

**4\. Keeping Calories in the Ocean for a Possible Catastrophe**

- [ _Has anyone done an analysis on the importance, tractability, and neglectedness of keeping human-digestible calories in the ocean in case we need it after some global catastrophe?_](https://forum.effectivealtruism.org/posts/MCFakPtwy2KDCYK3Q/has-anyone-done-an-analysis-on-the-importance-tractability) (@Mati_Roy)

In particular, the post suggests cultivating bacteria. ALLFED's director answers in the comments.

_Note_ : Included here for completeness. This isn't, strictly speaking, a new cause area since ALLFED is now working on it.

**5\. Recovery from an Existential Catastrophe**

- [ _Shortening & enlightening dark ages as a sub-area of catastrophic risk reduction_](https://forum.effectivealtruism.org/posts/o5hYrj5asR4jCBiZh/shortening-and-enlightening-dark-ages-as-a-sub-area-of) (@Jpmos)

This post lists some ideas relating to better recovery of civilization in case that an existential catastrophe takes place, which seems rather neglected as compared to prevention of existential risks.

**6\. Resilience of Industry and the Electric Grid**

- [ _AGI safety and losing electricity/industry resilience cost-effectiveness_](https://forum.effectivealtruism.org/posts/XA8QSCL7wZ973i6vr/agi-safety-and-losing-electricity-industry-resilience-cost) (@Ross_Tieman)

**7\. Foods for Global Catastrophes (ALLFED)**

- [ _Cost-Effectiveness of Foods for Global Catastrophes: Even Better than Before?_](https://forum.effectivealtruism.org/posts/CcNY4MrT5QstNh4r7/cost-effectiveness-of-foods-for-global-catastrophes-even) (@Denkenberger)

_Note_ : Included here for completeness. This isn't, strictly speaking, a new cause area since ALLFED is now working on it.

**8\. Preventing Ideological Engineering and Social Control**

_Related categories_ : Politics

- [ _Ideological engineering and social control: A neglected topic in AI safety research?_](https://forum.effectivealtruism.org/posts/oXzRPoCmYkEySevj8/ideological-engineering-and-social-control-a-neglected-topic) (@geoffreymiller)

"Will enhanced government control of populations' behaviors and ideologies become one of AI's biggest medium-term safety risks?"

**9\. Reducing Long-Term Risks from Malevolent Actors**

- [ _Reducing long-term risks from malevolent actors_](https://forum.effectivealtruism.org/posts/LpkXtFXdsRd4rG8Kb/reducing-long-term-risks-from-malevolent-actors) (@David_Althaus)

The authors make the case that a situation when malevolent actors rise to power has many negative externalities. They propose countermeasures, such as advancing the science of malevolence. This would involve developing better constructs and measures of malevolence, and hard-to-beat detection measures, such as neuroimaging techniques. Comments suggest further concrete measures, such as having elections for parties rather than leaders (which gives less power to individuals).

**10\. Autonomous Weapons**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/autonomous-weapons)

- [ _Why those who care about catastrophic and existential risk should care about autonomous weapons_](https://forum.effectivealtruism.org/posts/oR9tLNRSAep293rr5/why-those-who-care-about-catastrophic-and-existential-risk-2) (@aaguirre)
- [ _On AI Weapons_](https://forum.effectivealtruism.org/posts/vdqBn65Qaw77MpqXz/on-ai-weapons) (@kbog)

**11\. AI Governance**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/ai-governance), and is already being worked on at FHI's[ _Centre for the Governance of AI_](https://www.fhi.ox.ac.uk/govai/), among other places. For illustration purposes:

- [ _AI Governance: Opportunity and Theory of Impact_](https://forum.effectivealtruism.org/posts/42reWndoTEhFqu6T8/ai-governance-opportunity-and-theory-of-impact) (@Allan Dafoe)

**12\. International Cooperation**

- [ _International cooperation as a tool to reduce two existential risks_](https://forum.effectivealtruism.org/posts/fkN9zcqNeZGrXeeMF/international-cooperation-as-a-tool-to-reduce-two) (@johl@umich.edu)

The author argues that international cooperation could especially reduce the risks of unaligned AI and engineered pandemics. That’s why allocating funding in attempts to foster it seems of high importance.

**13\. Improving Disaster Shelters to Increase the Chances of Recovery From a Global Catastrophe**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/civilizational-collapse-and-recovery).

- [ _Improving disaster shelters to increase the chances of recovery from a global catastrophe_](https://forum.effectivealtruism.org/posts/fTDhRL3pLY4PNee67/improving-disaster-shelters-to-increase-the-chances-of) (@Nick_Beckstead)

“What is the problem? Civilization might not recover from some possible global catastrophes. Conceivably, people with access to disaster shelters or other refuges may be more likely to survive and help civilization recover. However, existing disaster shelters (sometimes built to ensure continuity of government operations and sometimes built to protect individuals), people working on submarines, largely uncontacted peoples, and people living in very remote locations may serve this function to some extent.

What are the possible interventions? Other interventions may also increase the chances that humanity would recover from a global catastrophe, but this review focuses on disaster shelters. Proposed methods of improving disaster shelter networks include stocking shelters with appropriately trained people and resources that would enable them to rebuild civilization in case of a near-extinction event, keeping some shelters constantly full of people, increasing food reserves, and building more shelters. A philanthropist could pay to improve existing shelter networks in the above ways, or they could advocate for private shelter builders or governments to make some of the improvements listed above.”

**14\. Discovering Previously Unknown Existential Risks**

- [ _The Importance of Unknown Existential Risks_](https://forum.effectivealtruism.org/posts/CRofnyTEqL4uSNBSi/the-importance-of-unknown-existential-risks) (@MichaelDickens)

The most dangerous existential risks appear to be the ones that we only became aware of recently. As technology advances, new existential risks appear. Extrapolating this trend, there might exist even worse risks that we haven't discovered yet.

**15\. Exploring Using Insights from International Relations Theory to facilitate International Cooperation Against Existential Risks**

- [ _International Cooperation Against Existential Risks: Insights from International Relations Theory_](https://forum.effectivealtruism.org/posts/sqTW3KhbkDirTh8vJ/international-cooperation-against-existential-risks-insights) (@Jenny_Xiao)

Dealing with existential risks requires international cooperation. Naturally, one might expect scholars of international relations (IR) to provide the best answers regarding how states can cooperate to protect humanity’s long-term potential. Yet reading Tody Ord’s new book[ **The Precipice**](https://theprecipice.com/) \_\_ as a PhD student in IR, I am surprised how little attention my field has paid to the existential threats Toby raised in the book, such as global disease, climate change, and risks from artificial intelligence (AI).

_Although mainstream IR often overlooks existential risks, it does offer insight into how to make international cooperation easier._ In particular, IR theory’s emphasis on the importance of national interests offers us a realistic view of international behavior.[ _Isaac Asimov_](https://www.penguinrandomhouse.ca/books/5596/a-choice-of-catastrophes-by-isaac-asimov/9780449900482), a universalist and humanist, once dismissed decisions based on the national interest as “emotional” reactions on “such nineteenth century matters as national security and local pride.” My view is exactly the opposite: _We should work with states as they are, not what we wish them to be._

**16\. Reducing Risks from Whole Brain Emulation**

- [ _The Age of Em_](https://en.wikipedia.org/wiki/The_Age_of_Em) (Robin Hanson)

**17\. Preventing/Avoiding Stable Longterm Totalitarianism**

_Pointer_ : This cause candidate has related EA forum tags:[ _Global dystopia_](https://forum.effectivealtruism.org/topics/global-dystopia) and[ _Totalitarianism_](https://forum.effectivealtruism.org/topics/totalitarianism)

- Chapter[ _"The Totalitarian Threat"_](https://forum.effectivealtruism.org/posts/SCqRu6shoa8ySvRAa/www.gmu.edu/departments/economics/bcaplan/total4.doc), in _Global Catastrophic Risks_ (Bryan Caplan)

**18\. Reducing Risks from Atomically Precise Manufacturing / Molecular Nanotechnology**

- [ _Molecular machinery and manufacturing with applications to computation_](https://dspace.mit.edu/handle/1721.1/27999) (Eric Drexler1991)

**19\. AGI Safety Research Far in Advance**

- [Link][ _A case for AGI safety research far in advance_](https://forum.effectivealtruism.org/posts/W2jh4bELpgzsB5n4d/a-case-for-agi-safety-research-far-in-advance) (@steve2152)

“Among other things, I make a case for misaligned AGI being an existential risk which can and should be mitigated by doing AGI safety research far in advance.”

**20\. Evolutionary AI alignment**

- [ _Can we simulate human evolution to create a somewhat aligned AGI?_](https://forum.effectivealtruism.org/posts/uk39s7wgLcotmFsto/can-we-simulate-human-evolution-to-create-a-somewhat-aligned) \_\_ (@Thomas Kwa)

This post discusses the possibility of simulating human evolution as a new approach to the alignment problem:

“If AI alignment is intractable, but human evolution is robust in producing something close to human values, we could try to simulate/mimic human evolution to create a superintelligent successor AI.”

**21\. Extraterrestrial Intelligence**

- [ _An EA case for interest in UAPs/UFOs and an idea as to what they are_](https://forum.effectivealtruism.org/posts/Y7hX9T6eA7kQQNaH5/an-ea-case-for-interest-in-uaps-ufos-and-an-idea-as-to-what) (@TheNotSoGreatFilter)

Given the current evidence of unidentified aerial phenomena, the probability that they are due to extraterrestrial crafts, and the enormous implications for our world models if this were the case, it may be reasonable to do more research on the subject.

**22\. Fundamental Research**

- [ _Cause area: Fundamental Research_](https://forum.effectivealtruism.org/posts/MGXuaCv3DqZXngAgz/cause-area-fundamental-research) (@amit.chilgunde)

The author claims that “research for the sake of research” is the best way to anticipate unknown future existential risks.

**23\. Universal Basic Income**

- [ _Mortality, existential risk, and universal basic income_](https://forum.effectivealtruism.org/posts/Z8GCPjoy37AscwhTz/mortality-existential-risk-and-universal-basic-income) (@MaxGhenis)

“I argue that poverty alleviation would reduce both mortality and existential risk, and that, among anti-poverty programs, universal basic income has a number of advantages over targeted and in-kind benefits.”

**24\. Short-range Forecasting**

- [ _Why short-range forecasting can be useful for longtermism_](https://forum.effectivealtruism.org/posts/zjMeGcgWpvDcm3CkH/why-short-range-forecasting-can-be-useful-for-longtermism) (@Linch)

The author argues that short-range forecasting can be useful for longtermism, if there is a coordinated effort to respond rapidly to potential crises in their early stages (for example, by creating an EA Early Warning Forecasting Center).

**25\. Risk from Asteroids**

- [ _Risks from Asteroids_](https://forum.effectivealtruism.org/posts/RZf2KqeMFZZEpvBHp/risks-from-asteroids) (@finm)

The author gives an overview of this particular risk and explains why it is not a cause to be prioritized:

“First, the international effort to track near-Earth asteroids is potentially humanity’s most successful effort to date to directly address an existential risk. . . . Second, expanding beyond mere detection to building deflection systems probably shouldn’t be a priority right now — not just because other comparably tractable risks look far more urgent, but because deflection technology could pose risks of its own from malign use.”

**26\. Biosecurity**

- [ _Project Ideas in Biosecurity for EAs_](https://forum.effectivealtruism.org/posts/NzqaiopAJuJ37tpJz/project-ideas-in-biosecurity-for-eas) (@Davidmanheim)

“In conjunction with a group of other EA biosecurity folk, I helped brainstorm a set of projects which seem useful, and which require various backgrounds but which, as far as we know, aren't being done, or could use additional work. Many EAs have expressed interest in doing something substantive related to research in bio, but are unsure where to start - this is intended as one pathway to do so.”

- [ _State of the land: Misinformation and its effects on global catastrophic risks_](https://forum.effectivealtruism.org/posts/jEdrFvwcmTgXTegfL/state-of-the-land-misinformation-and-its-effects-on-global) (@ruthgrace)

Basing on experience from the last pandemic, this post highlights the danger posed by misinformation to future global biological catastrophic risks on the rise, and sketches some possible ways to do something about it.

- [ _Non-pharmaceutical interventions in pandemic preparedness and response_](https://forum.effectivealtruism.org/posts/ydcF5CX7AkpNwMyGh/non-pharmaceutical-interventions-in-pandemic-preparedness#Tractability) (@James Smith)

The author argues that evaluation of non-pharmaceutical interventions (e.g. mask wearing, hand-washing, social distancing, etc.) is neglected and that the scale of its impact could be high.

- [ _Concrete Biosecurity Projects (some of which could be big)_](https://forum.effectivealtruism.org/posts/u5JesqQ3jdLENXBtB/concrete-biosecurity-projects-some-of-which-could-be-big-1) (@ASB & @eca)

This post gives a list of longtermist biosecurity projects. The first is about improving response time to biothreats by early detection. This could happen by setting up an **Early Detection Center** where a small team collects “samples from volunteer travelers around the world and then does a full metagenomic scan”.

The second project points out that most personal protective equipment (PPE)—e.g. masks, suits, etc.—has a number of disadvantages. Materials science and product design could produce **better PPE** than our current options, i.e. “highly effective in extreme cases, easy to use, reliable over long periods of time, and cheap/abundant”.

The third proposes better **medical countermeasures** against biothreats “either by 1) producing targeted countermeasures against particularly concerning threats (or broad-spectrum countermeasures against a class of threats), or by 2) creating rapid response platforms that are reliable even against deliberate adversaries”.

The fourth points out some possible ways of **strengthening the Biological Weapons Convention**. The fifth recommends further investigation on the advantages of **sterilization technologies** “that rely on physical principles (e.g. ionizing radiation) or broadly antiseptic properties (e.g., hydrogen peroxide, bleach) rather than molecular details (e.g. gram-negative antibiotics)”.

The last project is to create pandemic-proof **refuges** :

“Existing bunkers provide a fair amount of protection, but we think there could be room for specially designed refuges that safeguard against catastrophic pandemics (e.g. cycling teams of people in and out with extensive pathogen agnostic testing, adding a ‘civilization-reboot package’, and possibly even having the capability to develop and deploy biological countermeasures from the protected space).”

## **Rationality and Epistemics**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/rationality). It has seen more work on[ _LessWrong_](https://lesswrong.com) _._

**1\. Developing the Rationality Community**

- [ _Rationality as an EA Cause Area_](https://forum.effectivealtruism.org/posts/Z9rLfMjTZ2X376izm/rationality-as-an-ea-cause-area) (@casebash)

**2\. Progress Studies**

- [ _Progress Studies_](https://www.lesswrong.com/tag/progress-studies)

**3\. Epistemic Progress**

- [ _Epistemic Progress_](https://www.lesswrong.com/posts/xF96rk7yZtrjekiqZ/epistemic-progress-1) has also been suggested as a cause area, but this topic has seen more activity outside the EA Forum.

## **Donation timing**

**1\. Counter-Cyclical Donation Timing**

- [ _Increase Impact by Waiting for a Recession to Donate or Invest in a Cause_](https://forum.effectivealtruism.org/posts/NasdMzQfx2yT7AE9r/increase-impact-by-waiting-for-a-recession-to-donate-or) (@maxwell)

**2\. Patient Philanthropy**

_Pointer_ : This cause has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/patient-altruism). For illustration purposes:

- [ _Patience and Philanthropy_](https://philiptrammell.com/static/PatienceAndPhilanthropy.pdf), by Trammell (previously "Discounting for Patient Philanthropists")
- [ _Long-term investment fund at Founders Pledge_](https://forum.effectivealtruism.org/posts/8vfadjWWMDaZsqghq/long-term-investment-fund-at-founders-pledge) (@SjirH)

**3\. Improving our Estimate of the Philanthropic Discount Rate**

- [ _Estimating the Philanthropic Discount Rate_](https://forum.effectivealtruism.org/posts/3QhcSxHTz2F7xxXdY/estimating-the-philanthropic-discount-rate) (@MichaelDickens)

How we should spend our philanthropic resources over time depends on how much we discount the future. A higher discount rate means we should spend more now; a lower discount rate tells us to spend less now and more later.

According to a simple model, improving our estimate of the discount rate might be the top effective altruist priority.

## **Other**

Trivia: See[ _Wastebasket Taxon_](https://en.wikipedia.org/wiki/Wastebasket_taxon).

**1\. Eliminating Email**

- [ _[Link] A Modest Proposal: Eliminate Email_](https://forum.effectivealtruism.org/posts/qCwyhBuAMbjCegjtC/link-a-modest-proposal-eliminate-email) (@arikr)

Civilization could have better workflows around email.

**2\. Software Development in EA**

- [ _What are some software development needs in EA causes?_](https://forum.effectivealtruism.org/posts/ZGDheCSFidyxuWL4f/what-are-some-software-development-needs-in-ea-causes) (@evelynciara)

_Note_ : Post is a stub.

**3\. Tweaking the Algorithms which Feed People Information**

- [ _Short-Term AI Alignment as a Priority Cause_](https://forum.effectivealtruism.org/posts/ptrY5McTdQfDy8o23/short-term-ai-alignment-as-a-priority-cause) (@Lê Nguyên Hoang)

The post is structured in a confusing way, but a core suggestion is to tweak various current AI systems, particularly the Youtube and Facebook algorithms, to better fit EA values. However, the post doesn't give specific suggestions of the sort a Youtube engineer could implement.

**4\. Positively Shaping the Development of Crypto-Assets**

- [ _An Argument To Prioritize Positively Shaping the Development of Crypto-assets_](https://forum.effectivealtruism.org/posts/f4rH64WrjN3gda96L/an-argument-to-prioritize-positively-shaping-the-development) (@rhys_lindmark)

The article tries to analyze the promisingness of influencing the development of crypto assets from an ITN perspective, in 2018. Three of its most notable points are:

1. Effective Altruists should shape the implementation of any high-impact new technology,
2. crypto-assets constitute a new organizational technology which could solve a bunch of coordination problems, and
3. the use of crypto assets could result in beneficial resource redistribution.

- [ _A Democratic Currency_](https://forum.effectivealtruism.org/posts/k333SifAAwk5Fy2Cm/a-democratic-currency) (@MikkW)

The author outlines the creation of a new (digital) currency with a view to tackle poverty:

“[T]he major source of the currency will be in the people as a whole, with a certain fixed percentage of the value represented by the currency (that is, the market cap), being credited, on regular intervals (for example, every day), to every single person known to the currency.”

- [ _The transformative potential of cryptocurrencies_](https://forum.effectivealtruism.org/posts/eRA3DJHRdpkn6iue8/the-transformative-potential-of-cryptocurrencies) (@bejaq)

The author argues that decentralized creation of money (instead of money creation by central banks) could lead to better ways of distributing money.

**5\. Increasing Economic Growth**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/economic-growth). For illustration purposes:

- [ _Growth and the case against randomista development_](https://forum.effectivealtruism.org/posts/bsE5t6qhGC65fEpzN/growth-and-the-case-against-randomista-development) (@HaukeHillebrandt, @Halstead)
- [ _Can we drive development at scale? An interim update on economic growth work_](https://forum.effectivealtruism.org/posts/a84LrFzSf3sGsYfNr/can-we-drive-development-at-scale-an-interim-update-on) (@smclare, @AidanGoth)
- [ _Quantifying the Impact of Economic Growth on Meat Consumption_](https://forum.effectivealtruism.org/posts/YH4zm6JDLELnPyLP9/quantifying-the-impact-of-economic-growth-on-meat) (@kbog)

**6\. For-Profit Companies Serving Emerging Markets**

- [ _Why and how to start a for-profit company serving emerging markets_](https://forum.effectivealtruism.org/posts/M44rw22o5dbrRaA8F/why-and-how-to-start-a-for-profit-company-serving-emerging) (@Ben_Kuhn)

**7\. Land Use Reform**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/land-use-reform). The Land Use Reform tag covers posts that discuss changes to regulations around the use of land (e.g. for housing or business development). These changes could lead to increases in economic growth and welfare in locations around the world.

- [ _Cause Area: UK Housing Policy_](https://forum.effectivealtruism.org/posts/Aof6xs2jqfhEbJSxt/cause-area-uk-housing-policy) (@GMcGowan)

The author gives an overview of the problem and presents the solution advocated by the YIMBI movement in the UK, namely a political reform reducing veto power and giving households on a street the means of allowing development by a majority vote. The concluding section lists a number of reasons for and against EA involvement in this area.

- [ _Vetocracy reduction and other coordination problems as potential cause areas_](https://forum.effectivealtruism.org/posts/o8TfAbYgDGKbeu6Da/vetocracy-reduction-and-other-coordination-problems-as) (@John_Myers)

This post examines the problem posed by veto players when majorities are trying to bring forward development. Improving coordination techniques could be the way to break such deadlock not only here, but also in many other areas:

“With high uncertainty, I think that focusing a small amount of resources on improving broader coordination techniques for reducing such large deadweight losses in various areas could be a highly impactful, tractable and neglected area of research.”

**8\. Markets for Altruism**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/markets-for-altruism). For illustration purposes:

- [ _Certificates of impact_](https://forum.effectivealtruism.org/posts/yNn2o3kEhixZHkRga/certificates-of-impact) (@Paul_Christiano)

**9\. Meta-Science**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/meta-science). For illustration purposes:

- [ _The Intellectual and Moral Decline in Academic Research_](https://forum.effectivealtruism.org/posts/5GjpvnLNBHds9NtAh/the-intellectual-and-moral-decline-in-academic-research) (Edward Archer)
- [ _Prioritization in Science - current view_](https://forum.effectivealtruism.org/posts/Rjtezb4N7fyqGQrk6/prioritization-in-science-current-view) (@EdoArad)
- [ _Eva Vivalt: Forecasting Research Results_](https://forum.effectivealtruism.org/posts/Z7RTJePkiWBH92qqo/eva-vivalt-forecasting-research-results) (Eva Vivalt)

**10\. Scientific Progress**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/scientific-progress). However, it is mostly a stub, as far as EA Forum posts go. For illustration purposes:

- [ _How to estimate the EV of general intellectual progress_](https://forum.effectivealtruism.org/posts/3YeQ9LFuPnCBSu22M/how-to-estimate-the-ev-of-general-intellectual-progress) _(@Ozzie Goen)_
- [ _Science policy as a possible EA cause area: problems and solutions_](https://forum.effectivealtruism.org/posts/7eNxc6wzxWziJ3EGi/science-policy-as-a-possible-ea-cause-area-problems-and) (@PabloAMC)

“Creating the right incentive structures in science could make science more fluid, efficient, and painless. . . . The aim of this post is to suggest science policy as a possible research area for EAs where it might be possible to do progress that results in better science.”

**11\. Improving Information**

- [ _A Case for Better Feeds_](https://forum.effectivealtruism.org/posts/db8SiHtdscdHcK2Mm/a-case-for-better-feeds) (@Nathan Young)

A proposal to adapt information spread on EA databases to other methods of accessing it (email, twitter, RSS readers, etc.). If distribution of information is improved, there should be an increase in general impact.

- [ _Wikipedia editing is important, tractable, and neglected_](https://forum.effectivealtruism.org/posts/FebKgHaAymjiETvXd/wikipedia-editing-is-important-tractable-and-neglected) (@Darius_M)

This post highlights the importance of Wikipedia editing and gives useful suggestions for how this should be done.

**12\. Cause Prioritisation Research**

- [ _The case of the missing cause prioritisation research_](https://forum.effectivealtruism.org/posts/MSYhEatxkEfg46j3D/the-case-of-the-missing-cause-prioritisation-research) \_\_ (@weeatquince)

This post points out that there has been little progress on cause research for several years. Some difficulties relating to it are discussed, but “they are all overcomeable, and they do not make a strong case that such research is intractable”.

**13\. EA Art & Fiction**

_Pointer_ : This cause candidate has its own[ _EA Forum tag_](https://forum.effectivealtruism.org/topics/ea-art-and-fiction). For illustration purposes:

- [ _When can Writing Fiction Change the World?_](https://forum.effectivealtruism.org/posts/Bc8J5P938BmzBuL9Y/when-can-writing-fiction-change-the-world) (@timunderwood)

**14\. Corporate Giving Strategies and Corporate Social Responsibility**

- [ _How we promoted EA at a large tech company_](https://forum.effectivealtruism.org/posts/76mY5Mt6GC62tjnTP/how-we-promoted-ea-at-a-large-tech-company-v2-0) (v2.0) (@jlewars)
- [ _Are there EA-aligned organizations working on improving the effectiveness of corporate social responsibility/corporate giving strategies?_](https://forum.effectivealtruism.org/posts/2j9ZeSNEDbPtGnSZp/are-there-ea-aligned-organizations-working-on-improving-the) (@mss74)
- [ _If I am a US business owner, can I legally donate to an unrelated charity as a business expense to avoid the 37% income tax on that amount?_](https://forum.effectivealtruism.org/posts/uPhWFD5vowWB87giW/if-i-am-a-us-business-owner-can-i-legally-donate-to-an)

Note: This cause area comprises two distinct areas: giving by companies, and giving by employees.

Note: Corporate Social Responsability has the potential to be used by companies to cheaply distract from their pretty terrible working conditions in their supply chains by having ineffective corporate giving strategies which donate to recipients in the developed world. Last time I checked (two years ago). See[ _International Supply Chain Accountability_](https://forum.effectivealtruism.org/posts/ME4zE34KBSYnt6hGp/new-top-ea-cause-international-supply-chain-accountability).

**15\. Biodiversity**

- [Question][ _Neglected biodiversity protection by EA_](https://forum.effectivealtruism.org/posts/ysD5ZYCiohqKjrHEA/neglected-biodiversity-protection-by-ea) (@Danny Forest)

This post claims, without elaborating on it, that biodiversity of life should be considered worth funding. Some of the comments reason why it shouldn’t.

- [ _Answer to “Preserving natural ecosystems?”_](https://forum.effectivealtruism.org/posts/7AwqyiFLbDyNjw8RS/?commentId=qPDGY99anh2KFModP) (@RafaelF)

The author gives a list of ideas for tackling this issue.

**16\. Population Size Reduction**

- [ _Population Size/Growth & Reproductive Choice: Highly effective, synergetic & neglected_](https://forum.effectivealtruism.org/posts/WYmJoDxJZToDcA9Bq/population-size-growth-and-reproductive-choice-highly) (@RafaelF)

The author argues that reduction of population growth should be prioritised, because it would have significant positive effects on several other EA cause areas, such as climate change, animal welfare, etc.

**17\. Metaverse Democratisation**

- [ _Metaverse democratisation as a potential EA cause area_](https://forum.effectivealtruism.org/posts/NtdbQgqbybKtwJFMh/metaverse-democratisation-as-a-potential-ea-cause-area) (@Paul_Lang)

“This post argues that we may now be at a tipping point that decides whether we are steering either towards a utopian or to a dystopian future of hybrid virtual/physical realities. It encourages a discussion on the assessment of the problem and brainstorming of potential solutions.”

**18\. Sleeping Less to Increase Lifespan**

- [ _Theses on Sleep_](https://forum.effectivealtruism.org/posts/LxHHiLpHwtmGywiLb/theses-on-sleep#Conclusion) (@guzey)

The author argues that sleeping under 6 hours is perfectly healthy. If people sleep less, then their lifespan would be increased.

**19\. Combating Ageism**

- [Linkpost][ _Is Combatting Ageism The Most Potentially Impactful Form of Social Activism?_](https://forum.effectivealtruism.org/posts/mftEbZCbmHDihnQoL/is-combatting-ageism-the-most-potentially-impactful-form-of) (@JosephBronski)

The author claims that people between 15 and 17 years are “the most oppressed group in the West”.

**20\. S-risks**

- [ _How can we reduce s-risks?_](https://forum.effectivealtruism.org/posts/NwaqTc8pcfpybcrhs/how-can-we-reduce-s-risks) (@Tobias_Baumann)

“In this post, I’ll give an overview of the priority areas that have been identified in suffering-focused cause prioritisation research to date.”

- [ _The Importance of Artificial Sentience_](https://forum.effectivealtruism.org/posts/cEqBEeNrhKzDp25fH/the-importance-of-artificial-sentience) (@Jamie_Harris)

“Artificial sentient beings could be created in vast numbers in the future. While their future could be bright, there are reasons to be concerned about widespread suffering among such entities. . . . Research may help us assess which actions will most cost-effectively make progress.”

- [ _The problem of artificial suffering_](https://forum.effectivealtruism.org/posts/JCBPexSaGCfLtq3DP/the-problem-of-artificial-suffering) (@Martin Trouilloud)

This post reviews Metzinger's paper, _Artificial Suffering: An Argument for a Global Moratorium on Synthetic Phenomenology._

**21\. EA Meta**

- [ _Why EA meta, and the top 3 charity ideas in the space_](https://forum.effectivealtruism.org/posts/TcefyQHfYpAKvD6jq/why-ea-meta-and-the-top-3-charity-ideas-in-the-space) (@Joey)

“This post goes over why we think Effective Altruism meta could be highly impactful, why CE [Charity Entrepreneurship] is well-positioned to incubate these charities, why 2021 is a good time, differences in handling EA meta compared to other causes, and potential concerns. We finish by introducing our three top recommendations for new charities in the space: exploratory altruism, earning to give +, and EA training.”

**22\. Prioritization research on slacktivism**

- [ _Effective Slacktivism: why somebody should do prioritization research on slacktivism_](https://forum.effectivealtruism.org/posts/zKicwqprkWfbnsRCA/effective-slacktivism-why-somebody-should-do-prioritization) (@Kat Woods)

There are some tasks that could be done with almost no effort, and yet they could have a lot of impact. This post notes that “[s]ome slacktivism is probably way more effective than other slacktivism, so somebody should do some prioritization research to find the best slacktivism techniques”.

## **Other lists of ideas**

The following posts collect lots of funding ideas, many of which are novel interventions and cause areas:

- [ _E.A. Megaproject Ideas_](https://forum.effectivealtruism.org/posts/Khz5s6hrTWo4cReNL/e-a-megaproject-ideas) (@Tomer_Goloboy)
- [ _Milan Griffes on EA blindspots_](https://forum.effectivealtruism.org/posts/AqpFkoq3oSEvsqker/milan-griffes-on-ea-blindspots) (@Gavin)
- [Question][ _What EA projects could grow to become megaprojects, eventually spending $100m per year?_](https://forum.effectivealtruism.org/posts/ckcoSe3CS2n3BW3aT/what-ea-projects-could-grow-to-become-megaprojects) (@Nathan Young)
- [_Humanities Research Ideas for Longtermists_](https://forum.effectivealtruism.org/posts/oTJ5vMNwdWiHj2iKL/humanities-research-ideas-for-longtermists) (@Lizka)
- [ _EA Projects I'd Like to See_](https://forum.effectivealtruism.org/posts/8ic7KcxyfchhmGP3x/ea-projects-i-d-like-to-see) (@finm)
- [_EA megaprojects continued_](https://forum.effectivealtruism.org/posts/faezoENQwSTyw9iop/ea-megaprojects-continued) (@mariushobbhahn, @slg, @MaxRa, @JasperGeh & @Yannick_Muehlhaeuser)
- [ _The Future Fund's Project Ideas Competition_](https://forum.effectivealtruism.org/posts/KigFfo4TN7jZTcqNH/the-future-fund-s-project-ideas-competition) (@Nick_Beckstead, @ketanrama, @leopold, @William_MacAskill)

---

## **Appendix I: Method**

I queried all forum posts using the following query at the EA forum's GraphQL API:

    {
    posts(input: {
    terms: {
    meta: null  # this seems to get both meta and non-meta posts
    after: "10-1-2000"
    before: "10-11-2020" # or some date in the future
    }
    }) {
    results {
    title
    url
    pageUrl
    postedAt
    }
    }
    }

Then, I copied them over to a document called last5000posts.txt.

The EA forum API returns a maximum of 5000 entries, but this is not a problem because it currently only has 4077 posts.

I then searched for the keywords "cause x", "cause y", "new cause", "cause", "area", "neglected", "promising", "proposal", "intervention", "effectiveness", "cost-effective", using grep, a Unix/Linux tool, taking care to use the case-insensitive option (this is necessary because, although links contain the title in lowercase, links don't always contain the full title). An example of using grep to do this is:

grep -i "cause x" last5000posts.txt >> searchoutputs.txt

which appends the results to the searchoutputs.txt file if the file exists, and otherwise creates that file.

I then looked through the posts with the “Cause-Prioritization” tag and under the most upvoted posts to see if I had missed anything. I then went through all [EA Forum tags](https://forum.effectivealtruism.org/tags/) which had some relation to cause candidates and read through the relevant posts.

When I started tagging the posts I'd found, I found out about the "Less-discussed Causes" tag. I didn't like its categorization scheme, which also included things other than cause candidates, so I continued creating my own tags. The “Less-discussed Causes'' tag had about 5 posts I wouldn't have found. I also found many more posts which were not in the tag.

I imagine a similar method could be used to efficiently populate other tags.

## **Appendix II: A Note on Nomenclature**

Trivia: See [Soviet Nomenklatura](https://en.wikipedia.org/wiki/Nomenklatura#Etymology).

Thanks to Michael Aird for pushing for clarification of the terms I'm using, and for asking exactly what this list was about.

Terms:

- **Cause Area** : A broad category of causes. For example, "animal welfare and suffering" would be a cause area, "factory-farmed animals" and "wild animal welfare" would be slightly less-broad cause areas.
- **Cause** : Something more specific than a cause area. For example, "analgesics for farm animals" would be a cause within the "factory-farmed animals" cause area.
- **Intervention, charity idea** , etc.: Something more specific than a cause. For example, a ballot initiative to provide more space for factory-farmed animals, like [2018 California Proposition 12](https://en.wikipedia.org/wiki/2018_California_Proposition_12) would be an intervention. "Working to bring approval voting to Saint Louis" would be an intervention within the cause "better voting methods", itself within the cause area "better political systems".
- **Meta-intervention** : An intervention that can be applied to different causes. For example, ballot initiatives.

**Question: On what level of specificity am I working in this post?**

In practice, it's often hard to establish whether something is a cause area, a cause, or an intervention. For example, I'd say that "climate change" is a cause area and that "extinguishing or preventing coal seam fires" is a cause, but the [original post](https://forum.effectivealtruism.org/posts/2nrx8GdtobScoAZF8/extinguishing-or-preventing-coal-seam-fires-is-a-potential) refers to it as a cause area.

Column C —"Level of specificity"— [this google sheet](https://docs.google.com/spreadsheets/d/1GV-6M4WN1kvYnhplxgLA5cf37OdtGh3zDtOqy2uepJQ/edit#gid=469320850) contains information about the categorization chosen for each cause candidate (from intervention to cause area).

_This work is licensed under a_[ _Creative Commons Attribution 4.0 International License_](https://creativecommons.org/licenses/by/4.0/) _._

# Exercise for 'What do you think?'

For the exercise in this chapter, we will take some time to reflect on the ideas we’ve engaged with over the past chapters. Our goal is to take stock and to identify our concerns and uncertainties about EA ideas.

## What are your concerns about EA? (15 mins.)

We’ve covered a lot over the last few chapters: the philosophical foundations of effective altruism, how to compare causes and allocate resources, and a look at some top priority causes using the EA framework.

What are your biggest questions, concerns, and criticisms based on what we’ve discussed so far? These can be about the EA framework/community, specific ideas or causes, or anything you’d like!

## Reflecting back (45 mins.)

You’ve covered a lot so far! We hope you found it an interesting and enjoyable experience. There are lots of major considerations to take into account when trying to do the most good you can, and lots of ideas may have been new and unfamiliar to you. In this chapter we’d like you to reflect back on the program with a skeptical and curious mindset.

To recapitulate what we’ve covered:

**Chapter 1: The Effectiveness mindset**

Over the course of Chapters 1 and 2, we aim to introduce you to the core principles of effective altruism. We use global health interventions, which has been a key focus area for effective altruism, to illustrate these principles, partly because we have unusually good data for this cause area.

**Chapter 2: Differences in impact**

In Chapter 2 we continue to explore the core principles of effective altruism, particularly through the lens of global health interventions because they are especially concrete and well-studied. We focus on giving you tools to quantify and evaluate how much good an intervention can achieve; introduce expected value reasoning; and investigate differences in expected cost-effectiveness between interventions.

**Chapter 3: Radical empathy**

The next section focuses on your own values and their practical implications. During Chapter 3 we explore who our moral consideration should include. We focus especially on farmed animals as an important example of this question.

**Chapter 4: Our final century?**

In this chapter we’ll focus on existential risks: risks that threaten the destruction of humanity’s long-term potential. We’ll examine why existential risks might be a moral priority, and explore why existential risks are so neglected by society. We’ll also look into one of the major risks that we might face: a human-made pandemic, worse than COVID-19.

**Chapter 5: What could the future hold? And why care?**

In this chapter we explore what the future might be like, and why it might matter. We’ll explore arguments for “longtermism” - the view that improving the long term future is a key moral priority. This can bolster arguments for working on reducing some of the extinction risks that we covered in the last two weeks. We’ll also explore some views on what our future could look like, and why it might be pretty different from the present.

**Chapter 6: Risks from artificial intelligence**

Transformative artificial intelligence may well be developed this century. If it is, it may begin to make many significant decisions for us, and rapidly accelerate changes like economic growth. Are we set up to deal with this new technology safely?

Now, trying answering the following questions:

_What topics or ideas from the program do you most feel like you don’t understand?_

_What seems most confusing to you about each one? (Go back to that topic/idea and see if there are any further readings you can do that would help you address your uncertainties and explore any concerns. Do those readings. Consider writing notes on your confusion, stream-of-consciousness style.)_

_List one idea from the program that you found surprising at first, and which you now think more or less makes sense and is important? How could this idea be wrong? What’s the strongest case against it?_

_List one idea from the program that you found surprising at first, and think probably isn’t right, or have reservations about. What’s the strongest case **for** this idea? What are your key hesitations about that case?_

# More to explore on 'What do you think?'

[_Effectiveness is a conjunction of multipliers_](https://forum.effectivealtruism.org/posts/GzmJ2uiTx4gYhpcQK/effectiveness-is-a-conjunction-of-multipliers) (5 mins.) - one take on why it matters so much to think carefully and critically about which of the above perspectives is right.

## Types of criticism

- [ _Disagreeing about what’s effective isn’t disagreeing with effective altruism_](https://tinyurl.com/y3b9v8uh) \- _Rob Wiblin differentiates critiques of effective altruism as a concept and critiques of the ways EAs attempt to apply this concept._ (5 mins.)
- [ _Four categories of effective altruism critiques_](https://forum.effectivealtruism.org/posts/HzyYoLK2ERTnDmrjB/four-categories-of-effective-altruism-critiques) (4 mins.)

## Systemic change

- [ _Response to Effective Altruism, Iason Gabriel_](https://bostonreview.net/forum_response/response-iason-gabriel/) (1 min.)
- [ _Effective altruists love systemic change_](https://tinyurl.com/2szjdmy) \- _Robert Wiblin argues why EA does not, in fact, neglect systemic change._ (13 mins.)
- [ _Beware Systemic Change_](https://tinyurl.com/8ambmj6p) (15 mins.)
  - Critique of pursuing systemic change. How hard is it to figure out what systemic changes will make things better?
  - This is partly an expression of disagreement with others in EA who have [_embraced systemic change_](https://tinyurl.com/2szjdmy), which was itself partly a response to criticisms like those in the Boston Review

## Is effective altruism a question or an ideology, or both?

- [ _Effective Altruism is a Question (not an ideology)_](https://forum.effectivealtruism.org/posts/FpjQMYQmS3rWewZ83/effective-altruism-is-a-question-not-an-ideology) (5 mins.)
- [ _Effective Altruism is an Ideology, not (just) a Question_](https://forum.effectivealtruism.org/posts/uxFvTnzSgw8uakNBp/effective-altruism-is-an-ideology-not-just-a-question) (24 mins.)

## General criticisms of effective altruism

- [ _Notes on Effective Altruism_](https://michaelnotebook.com/eanotes/) (20 mins.)
- [ _The Centre for Effective Altruism’s responses to some common objections_](https://tinyurl.com/3feahcj6) (10 mins.)
- [ _Responses to The Logic of Effective Altruism_](https://tinyurl.com/5afpjkxn) (~20 mins., pick a few to read) Note that these critiques are from 2015.
  - Recommended excerpts
    - Daron Acemoglu
    - Angus Deaton
    - Jennifer Rubenstein
    - Iason Gabriel
    - Peter Singer’s response
  - How to view these: click the names under “Responses” at the bottom of the original article
- [ ** _Towards Ineffective Altruism_**](https://reboothq.substack.com/p/ineffective-altruism?s=r) **(15 mins.)**
- [ ** _A critique of effective altruism_**](https://tinyurl.com/598j34mc) **(11 mins.)**
- [ _Another Critique of Effective Altruism_](https://tinyurl.com/77tx8fey) (5 mins.)
- [ _The motivated reasoning critique of effective altruism_](https://forum.effectivealtruism.org/posts/pxALB46SEkwNbfiNS/the-motivated-reasoning-critique-of-effective-altruism) (34 mins.)
- [ _Making decisions under moral uncertainty_](https://tinyurl.com/yjdntm2b) \- _Placing credence in multiple ethical systems leads to questions of moral uncertainty when the two ethical systems disagree. This post summarizes the problem and suggests ways to resolve such issues._ (16 mins.)
- [ _Some blindspots in rationality and effective altruism_](https://tinyurl.com/48wvhfy9) \- _An EA forum blog post that discusses some common pitfalls for rationalists and effective altruists, as well as some meta-considerations_ (12 mins.)
- [ _Free-spending EA might be a big problem for optics and epistemics_](https://forum.effectivealtruism.org/posts/HWaH8tNdsgEwNZu8B/free-spending-ea-might-be-a-big-problem-for-optics-and) (12 mins.) - _EA forum post on risks associated with EA spending trends_
- [ _80,000 hours' anonymous flaws in EA_](https://80000hours.org/2020/03/anonymous-answers-flaws-effective-altruism-community/)
- [ _Critiques of EA that I want to read_](https://forum.effectivealtruism.org/posts/n3WwTz4dbktYwNQ2j/critiques-of-ea-that-i-want-to-read) (16 mins)
- [ _Effective Altruism: Not Effective and Not Altruistic_](https://swarthmorephoenix.com/2022/03/31/effective-altruism-not-effective-and-not-altruistic/) (27 mins.)
- [ _Stop the Robot Apocalypse_](https://drive.google.com/file/d/1KMzfLdXU6-ZGmnrgAoa3jAQWTRRJCFEg/view?usp=sharing) \- Amia Srinivasan - (15 mins.)
- [ _EA and the current funding situation_](https://forum.effectivealtruism.org/posts/cfdnJ3sDbCSkShiSZ/ea-and-the-current-funding-situation) \- _not exactly criticism, but discusses some potential pitfalls of EA’s current funding situation_ (35 mins.)

## Deference and forming inside views

- [ _Some thoughts on deference and inside view models_](https://forum.effectivealtruism.org/posts/53JxkvQ7RKAJ4nHc4/some-thoughts-on-deference-and-inside-view-models) (14 mins.)
- [ _A sketch of good communication_](https://www.lesswrong.com/posts/yeADMcScw8EW9yxpH/a-sketch-of-good-communication) (4 mins.)
- [ _How I formed my own views on AI safety_](https://forum.effectivealtruism.org/posts/xS9dFE3A6jdooiN7M/how-i-formed-my-own-views-about-ai-safety) (21 mins.)
- [ _Deference Culture in EA_](https://forum.effectivealtruism.org/posts/Jx6ncakmergiC74kG/deference-culture-in-ea) (8 mins.)
- [ _Bad Omens in Current Community Building_](https://forum.effectivealtruism.org/posts/xomFCNXwNBeXtLq53/bad-omens-in-current-community-building) (27 mins.)

## Criticism of EA methods

- [ _A philosophical review of Open Philanthropy’s Cause Prioritisation Framework_](https://forum.effectivealtruism.org/posts/bdiDW83SFAsoA4EeB/a-philosophical-review-of-open-philanthropy-s-cause) (42 mins.)
- [ _Evidence, Cluelessness, and the Long Term_](https://www.youtube.com/watch?v=fySZIYi2goY) \- Hilary Greaves - (30 mins.)
- [ _Why we can’t take expected value estimates literally (even when they’re unbiased)_](https://tinyurl.com/375fr395) \- _Holden Karnofsky explains why he takes issue with using expected value estimates of impact._ (35 mins. - skimmable)
- [ _Some blindspots in rationality and effective altruism_](https://tinyurl.com/48wvhfy9) \- _An EA forum blog post that discusses some common pitfalls for rationalists and effective altruists, as well as some meta-considerations_ (12 min)
- [ _Ethical Systems_](http://tinyurl.com/zfm9rmw3) \- _Check out other ethical systems not discussed yet in the program. Which ones resonate most with you?_ (Varies)
- [ _Summary review of ITN critiques_](https://forum.effectivealtruism.org/posts/MtCAsPMftvJqRBYzr/wip-summary-review-of-itn-critiques) (8 mins.)

## Criticism of EA principles

- [ _Pascal’s Mugging_](https://tinyurl.com/5azx42b7) _Critique of the application of expected value theory. How do you deal with very low probability events that would be disastrous if they took place?_ (5 mins.)
- [ _Ethical Systems_](http://tinyurl.com/zfm9rmw3) \- _Check out other ethical systems not discussed yet in the program. Which ones resonate most with you?_ (Varies)
- [ _AI alignment, philosophical pluralism, and the relevance of non-Western philosophy_](https://www.youtube.com/watch?v=dbMp4pFVwnU) \- _Short talk_ (18 mins.)
- [ _The Repugnant Conclusion_](https://tinyurl.com/bjkx2bna) \- _Total utilitarianism (maximizing overall wellbeing) implies that it’s better to have many many beings with infinitesimally positive wellbeing to a smaller number of beings that are all extremely well off. Some people find this counterintuitive, but there’s significant debate on this._ (Video - 6 mins.)
- [ _Utility monster_](https://tinyurl.com/dts35ejh) \- _Another thought experiment suggesting that trying to maximize wellbeing may have counterintuitive implications_ (5 mins.)
- [ _The bullet-swallowers_](https://tinyurl.com/3hwsdusv) \- _Scott Aaronson describes how some theories (like EA) force you to either swallow some tough conclusions or dodge them by contorting the theory._ (2 mins.)

## Funding and Cause prioritization

- [ _The flow of funding in EA movement building_](https://forum.effectivealtruism.org/posts/nnTQaLpBfy2znG5vm/the-flow-of-funding-in-ea-movement-building) (In this piece, data on funding for different cause areas within EA was collected and analyzed. It’s important to note that funding is only one of many ways we could determine what the EA movement currently prioritizes, and other sources (such as the [_EA Survey_](https://forum.effectivealtruism.org/topics/effective-altruism-survey)) might show other results.) (12 mins.)
