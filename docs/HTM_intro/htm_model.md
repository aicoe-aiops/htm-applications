# HTM Model Structure

[HTM](https://web.archive.org/web/20110721225535/http://blog.mohammadzadeh.info/media/blogs/snf/Resources/HTM/Numenta_HTM_Concepts.pdf?mtime=1296775021) is a multi-layer tree structure. The signal sensed by the perceptron is first input to the bottom node (in the original version, each node is a single cell. In the improved version of the second version, it is changed to a Cortical Column, which contains one The cells of the array), and the output of the node (Beliefs) are then transferred layer by layer to the highest layer. As shown in the figure below.

```{figure} images/htm.png
---
---
[HTM](https://web.archive.org/web/20110721225535/http://blog.mohammadzadeh.info/media/blogs/snf/Resources/HTM/Numenta_HTM_Concepts.pdf?mtime=1296775021) structure!
```
The so-called Belief in the Fig. 2 is the probability array of Cause, as shown in the following Fig. 3.

```{figure} images/htm1.png
---
---
[HTM](https://web.archive.org/web/20110721225535/http://blog.mohammadzadeh.info/media/blogs/snf/Resources/HTM/Numenta_HTM_Concepts.pdf?mtime=1296775021) structure!
```

As mentioned in Thousand Brains Theory, each node (Column) will learn a complete world view. But the nodes at the bottom will only learn the simplest objects, and the nodes on the upper level eill learn the more complex composite objects. This also means that the number of layers required by the HTM is positively related to the complexity of the object to be recognized. 












