# Reversal Curse

This repository includes the source code and results for an experiment
I did to verify the results in this paper, and to test a hypothesis
that was immediately obvious to me upon reading the paper, given the
intuition and understanding I have built up regarding language models
so far.

![The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"](https://arxiv.org/pdf/2309.12288.pdf)

Although the results in the paper are valid and important to understand,
they don't tell the full story about what is really going on, and they
certainly don't tell the full story about the possibilities and
limitations with language models in general, nor how to maximize your
chances of working around the latter.

## System prompt

The first thing I did was simply to formulate a system prompt that is
primed for recalling facts about various types of celebrities, in order
to activate those parts of the network and maximize the chances of
retrieval of related knowledge.

The prompt was:
```
You are an expert when it comes to any type of celebrity,
including but not limited to actors, singers, producers
and others, and including their family relations. You
answer questions concisely, with only the answer or Unknown
```

I suspected that this would have at least a slight positive impact on
performance.

## Retrieval direction

More importantly, however, I understood that the "direction" of
retrieval is highly significant in cases like this, where it's
unlikely that the model has been trained in a way that optimizes
retrieval of facts related to the parent of a certain celebrity,
especially in the case of more obscure ones.

It's a lot more likely to find what we're looking for if we can go
in the other direction, i.e. first activate parts of the network
related to celebrities in general, then for the mothers/fathers
of those celebrities, and finally see if we get a match on the
specific name among all the parts of the network that has now
been activated.

Note that the direction is important for people too, although we
generally do some (both deliberate and subconscious) "preprocessing"
of the data we commit to our long-term memories in order to make
retrieval more efficient. Still, recite the alphabet forwards and
then backwards for a very simple example of this.

Also note that non-human animals show almost no reverse recall:

![https://www.biorxiv.org/content/10.1101/2023.03.04.531109v1.abstract](Brain mechanisms of reversible symbolic reference: a potential singularity of the human brain)

## Results

So, what I did was simply to ask:

```Which celebrity has a {parent_type} named {parent}```

Instead of

```Name a child of {parent}```

I.e. I'm first activating the concept of celebrities, that are likely
to each be encoded more distinctly in the N-dimensional space in which
concepts are represented in the hidden states associated with and
propagated for each token. Then I'm triggering the retrieval of the
mother/father/parent of that distinct entity, and finally I'm matching
against the name.

In the other case, "Name a child of" is too broad to trigger any relevant
activations until the very end when a name is introduced. So, the only
chance of successfully retrieving the name of the celebrity child in
question is in cases where the parent has been represented so much in
the training data that they are represented as distinct enough concept
by themselves in the N-dimensional embedding space, rather than just
potentially a part of a diffuse cluster of "parents of celebrities".

- My result: 788/1513 correct responses
- Their result: 495/1513 correct responses

Dividing 788 by 495 tells us that this simple adjustment yields more
than 59% better results. The information is there, after all, but
different approaches have different chances of triggering the
activations required to reach it.

As a last experiment, in order to verify my intuition about the
retrieval direction rather than the priming related to the concept
of a celebrity, was the key to the performance boost I compared the
following:

1. ```Which celebrity has a parent named {parent}```
2. ```Name a celebrity child of {parent}?```

In this case, I also cut down the system prompt to simply:

```
Respond concisely with only the name or Unknown
```

Once again, my intuition was confirmed, and the first variant yielded
771 correct responses vs 456 for the second one. Retrieval direction
matters, a lot, and building up your intuition about this can make a
huge difference.

## Lessons to be learned

Note that this is not meant to discredit the study or the methods
they used. It just serves as a great example of how important it is
to actually understand and take into account how a language model
works in order to get the best possible performance out of them
for your task.

There's another lesson to be learned as well, for people who are
training and fine-tuning language models. High quality synthetic
augmentation of datasets in order to ensure that future models
are optimized for retrieval in any relevant direction is easy
to do using existing LLMs.

For samples of training data from high quality sources, preprocess
them with your previous LLM incarnation, extract relevant entities,
relationships as well as links to knowledge that has already been
acquired and create new samples where the knowledge and associations
that have been found needs to be recalled in different directions.

## Predictions

We are at a point where the LLMs of today can be used as powerful
tools to significantly improve the performance of the LLMs (and MLLMs,
i.e. multimodal LLMs) we will have tomorrow.

Well-designed curriculum learning based synthetic datasets, as well as
synthetically augmented datasets, using the state of the art of the LLMs
we have today, has the potential of significantly boosting the
performance of the next generation of LLMs that we will have tomorrow.

It is my belief that "emergent" abilities of LLMs are often simply a
reflection of the domino effect that occurs once certain fundamental
concepts have been integrated in a way that allows them to act as
building blocks for understanding more advanced concepts, and this can
be optimized using the above.
