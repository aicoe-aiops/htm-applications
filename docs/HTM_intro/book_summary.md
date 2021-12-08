# `On Intelligence` and `A Thousands Brains` by Jeff Hawkins - Summary

[Numenta](https://numenta.com/), a startup of neuroscientists whose goal is to understand the neo cortex to reproduce the mechanism in learning algorithms. The founder, Jeff Hawkins, wrote a book _On Intelligence_ and _A Thousand Brains_, in which the author gives a history of theories about the brain and intelligence. He explains with anecdotes and experiences how he arrived at his theory.

In the book, _On Intelligence_, Hawking's basic idea is that the brain is a mechanism to predict the future, hierarchical regions of the brain predict their future input sequence. Perhaps not always far from the future, but far enough to be of real use to an organism. As such, the brain is a feed forward hierarchical machine with special properties that enable it to learn. The state machine actually controls the behavior of the organism. Since it is a feed forward state machine, the machine responds to future events predicted from the past data.

The hierarchy is capable of memorizing frequently observed sequences of patterns and developing invariant representations. Higher levels of the cortical hierarchy predict the future on the longer time scale, or over a wider range of sensory inputs. Lower levels interpret and control limited domains of experience, or sensory or effector system. Connections from the higher level states predispose some selected transitions in the lower-level state machines. Hebbian learning is a part of the framework, in which the event of learning physically alters neurons and connections, as learning takes place. Vernon Mountcadtle’s formulation of the cortical column is a basic element in the framework. Hawkings places particular emphasis on the role of interconnections from peer columns  and the activation of columns as a whole. He strongly implies that a column is the cortex’s physical representation of a state in a state machine.

```{figure} images/thousand-brains.png
---
#height: 150px
#name: A Thousand Brains
---
[A Thousand Brains](https://numenta.com/neuroscience-research/research-publications/papers/thousand-brains-theory-of-intelligence-companion-paper/).
```

The Thousand Brains Theory is the core model-based, sensory-motor framework of intelligence putting together the neuroscience research developed over the almost two decades of research at Numenta and the Redwood Neuroscience Institute (founded in 2002 by Jeff Hawkins). While backed by substantial anatomical and functional neurological evidence, it provides a unique interpretation of the high-level computation thought to happen throughout the neocortex and giving rise to intelligent behaviors.

In particular, the framework suggests mechanisms for how the cortex represents object compositionality, object behaviors and even high-level concepts from a basic functional unit tightly replicated across the cortical sheet: a cortical column. It leads to the hypothesis that every cortical column learns complete models of objects. Unlike traditional hierarchical ideas in deep learning, where objects are learned only at the top, the theory proposes that there are many models of each object distributed throughout the neocortex (hence the name of the theory).
