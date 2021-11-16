# Anomaly Detection with HTM

**Anomaly** : Something that deviates from what is standard, normal, or expected.

Most of the parts in this section are covered from paper on [Unsupervised real-time anomaly detection for streaming data](https://www.sciencedirect.com/science/article/pii/S0925231217309864#bib0001).
Numenta’s anomalies detection approach is derived from the understanding of neo-cortex, which is itself a powerful prediction and anomaly detection system. Using their understanding of neo-cortex, they derive state-of-the-art breakthroughs in two dimensions: 1) how they utilize the processes of the brains to model data, and 2) how they detect anomalies based on that model.

Based on known properties of cortical neurons, Hierarchical Temporal Memory (HTM) is a theoretical framework for sequence learning in the cortex. HTM implementations operate in real-time and have been shown to work well for prediction tasks. HTM networks continuously learn and model the spatiotemporal characteristics of their inputs, but they do not directly model anomalies and do not output a usable anomaly score. In this section we describe our technique for applying HTM to anomaly detection.

```{figure} images/anomaly1.png
---
---
Anomaly detection using HTM.
```

Fig. 8 above, shows the overview of the process. At each point in time, the input data $x_{t}$ is fed to a standard HTM network. Two additional cmputations on the output of the HTM is performed. The first compute the measure of prediction error, $S_{t}$. Then, using a probabilistic model of $S_{t}$, we compute $L_{t}$, a likelihood that the system is in the anomalous state. A threshold on this likelihood determines whether an anomaly is detected.

Fig. 9 shows the core algorithm components and representations within a typical HTM system. The current input, $x_{t}$, is fed to an encoder and then sparse spatial pooling process. The resulting vector, $a(x_{t})$, is a asparse binary vector representing the current input. The heart of the system is the sequence memory component. This component models temporal patterns in $a(x_{t})$ and outputs a prediction in the form of another sparse vector $\pi(x_{t})$. $\pi(x_{t})$ is thus the prediction for $a(x_{t}+1)$.

```{figure} images/anomaly2.png
---
---
HTM core algorithm components.
```
