# Performance of HTM compared to other tnomaly detection techniques

[Numenta Anomaly Benchmark](https://github.com/numenta/NAB), an opensourse project, is designed to be an accessible and reliable frame word for all to use. Included witht eh open-source data and code is extensive documentation and examples on how to test algorithms. The repository contains source code for commonly used algorithms for online anomaly detection. 

A number of anomlay detection methods, like, HTM, Twitter's Anomaly Detection, Etsy's Skyline, [Multinomial Relative Entropy](https://ieeexplore.ieee.org/document/5990537), [EXPoSE](https://doi.org/10.1007/s10994-016-5567-7), Bayesian Online Changepoint detection, simple sliding threshold, and so on were considered.

```{figure} images/nab-score.png
---
---
NAB score board.
``` 

NAB scoreboard summarizes the NAB scores for each algorithm across all application profiles. HTM AL denotes the HTM algorithm using prediciton error plus anomaly likelihood. HTM PE denotes the HTM algorithm using prediction error only. Overall we see that the HTM detector using anomaly likelihood gets the best score, followed by CAD-OSE, nab-comportex, KNN-CAD, and the Multinomal Relative Entropy detector. The HTM detector using only prediction error performs moderately well, but using the anomaly likelihood step significantly improves the scores. 

```{figure} images/nab-score1.png
---
---
Comparison of properties of algorithm that is implemented and tested in [NAB](https://github.com/numenta/NAB).
``` 

Fig. 14 shows the comparison of properties for algorithms that is implemented and tested in [NAB](https://github.com/numenta/NAB).Each algorithm is categorized based on its ability to detect spatial and temporal anomalies, handle concept drift, and automatically update parameters; these characteristics are based on published information, which may or may not reflect the actual performance. We also list the measured latency of processing each data point. Several algorithms claim to have all of the listed properties but their actual anomaly detection performance on the benchmark varies significantly. In general there is a rough correlation between the number of properties satisfied and the NAB ranking.

```{figure} images/nab-score2.png
---
---
Comparison of average NAB scores for some algorithms across data from different kinds of sources provide by [NAB](https://github.com/numenta/NAB).
```

A breakdown of the algorithms performance on the benchmark is shown in Fig. 15. Results have been aggregated across data sources ranging from artificially generated streams to real streams from advertisement clicks, server metrics, traffic data and twitter volume. Data streams are characterized by spatial anomalies, temporal anomalies or a combination. Grouping the streams by their anomaly types in Fig. 15 helps us inspect the characteristics of the algorithms identified earlier in Fig. 14 . Results show that both HTM and CAD-OSE yield the best over- all aggregate scores on almost all data sources and anomaly types, with the exceptions of Twitter AdVec on artificial temporal streams and KNN –CAD on miscellaneous known causes. The difference between aggregate scores for HTM and CAD-OSE for the majority of the data streams is less than 0.20. For some stream types, HTM significantly outperforms CAD-OSE such as spatial advertisement streams, temporal server metric streams and spatial/temporal mis- cellaneous streams. In particular, the results show HTM performing well on server metrics and online advertisements data while CAD- OSE performs well on traffic and twitter streams.


