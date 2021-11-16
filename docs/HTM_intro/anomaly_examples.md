# Anomaly Detection Examples

## Anomaly at production datacenters

Consider an example of production datacenter. Software upgrades can occur anytime and may alter the behavior of the system. In such cases models must adapt to a new definition of 'normal' in an unsupervised, automated fashion.

```{figure} images/eg1.png
---
---
CPU utilization (percent) for an Amazon EC2 instance (data from [Numenta Anomaly Benchmark](https://github.com/numenta/NAB).
```
 In Fig. 10, a modification to the software running on the machine caused the CPU usage to change. The initial anomaly represents a changepoint, and the new system behavior that follows is an example of concept drift. Continuous learning is essential for performing anomaly detection on streaming data like this.

## Anomaly with prediction error

```{figure} images/eg2.png
---
---
Data Stream along with prediction error.
```

Fig. 11 above shows the plot of CPU usage on the database server over time. There are two unusual behavior in this stream, the temporary spike upto $75%$ and the sustained shift up to $30%$ usage. It also shows the prediction error while the HTM trains on this stream. Early during training the prediction error is high while the HTM model learns the data. There is a spike in prediction error corresponding to the temporary spikes in CPU usage that quickly drops once usage goes back to normal. Finally, there is an increase in prediction error corresponding to the sustained shift, which drops after the HTM has learned the new behavior.

## Anomaly for very noisy, unpredictable stream

```{figure} images/eg3.png
---
---
A very noisy, unpredictable stream.
```

Fig. 12 shows an example of anomaly likelihood, $L_{t}$, on noisy load balencer data. The figure demonstrates that the anomaly likelihood provides clearer peaks in extremely noisy scenarios compared to pur prediction error. The data shows the latency (in seconds) of a load balancer on a production website. The anomaly (indicated by the dot) is an unusual sustained increase in latencies around April 10. The prediction error from an HTM model on the latency values. The unpredictable nature of the latencies results in frequent spikes in the prediction error that cannot be distinguished from the true positives. The fact that the unpredictable metric values are spikes and the rest of the latencies are close to zero results in the coincidental similarity between the latencies and resulting prediction error. A log-scale plot of the anomaly likelihood computed from the prediction error. Unlike the prediction error plot, there is a clear peak right around the real anomaly.
