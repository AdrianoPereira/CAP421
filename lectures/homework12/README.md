<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/images/cover-homework12.png" style="width: 100%;">

## Overview
<hr />

This notebook contains exercise 12 (RNNs Exercise 1). This exercise was proposed by Thales Sehn Körting in the course CAP421 - Deep Learning offered in the Postgraduate Program in Applied Computing at the National Institute for Space Research.

**RNNs Exercise 1:**
> Create a classification model using the LSTM architecture to deal with the same problem from our previous test (given a GOES time series, with training elements ```time_steps```, *predict* the next element in the time series). When the predicted value is considered different (define a threshold) from the actual value, indicate a candidate disturbance point. <br /> <br />
For *training*, use the entire curve available at https://raw.githubusercontent.com/tkorting/remote-sensing-images/master/id_756_time_series.csv <br />
For *testing*, use the second one, available at https://raw.githubusercontent.com/tkorting/remote-sensing-images/master/id_703_time_series.csv

## Table of content <span id="table_of_content"></span>
<hr />

- [Overview](#overview)
- [Table of content <span id="table_of_content"></span>](#table-of-content-)
  - [History models](#history-models)
  - [Observation vs Prediction](#observation-vs-prediction)
  - [Correlation analysis](#correlation-analysis)
  - [Dynamic time warping (DTW)](#dynamic-time-warping-dtw)
  - [Identifying disturbances in the time series](#identifying-disturbances-in-the-time-series)
  - [References <a href="#table_of_content"> ^</a> <span id="references"></span>](#references---)

**Author:** Adriano P. Almeida <<adriano.almeida@inpe.br>>
<br />
**Full Notebook avaiable at**: [GitHub](#) and [Google Colab](#)
<br />
**Created on:** 18 November, 2021
<br />

<a href="https://colab.research.google.com/drive/1Jwl905xHU47JvBKT52sxGXqew1kHpbV8?usp=sharing">
    <img style="float: left; margin-right: 10px;" src="https://colab.research.google.com/assets/colab-badge.svg" />
</a>

<a href="https://github.com/AdrianoPereira/CAP421/tree/main/lectures/homework12">
    <img style="float: left; margin-right: 10px;" src="https://img.shields.io/badge/GitHub-Open%20Repository-lightgrey?logo=github" />
</a>
<br /><br />

### History models
<hr>

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/boxplot-history.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 1</strong>: Boxplot history of models.
</span>
</p>

<br />
<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/line-history.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 2</strong>: Line plot history of models.
</span>
</p>

### Observation vs Prediction 
<hr />

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/scatter-comp.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 3</strong>: Scatter plot observations and predictions.
</span>
</p>

### Correlation analysis
<hr />

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/bars-correlations.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 4</strong>: Correlations between observations and predictions.
</span>
</p>

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/comparation-models.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 5</strong>: Comparasion beteween observations and predictions of best models.
</span>
</p>

### Dynamic time warping (DTW)
<hr />

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/paths-dtw.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 6</strong>: Dynamic time warping analysis.
</span>
</p>

<br />

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/paths-accumulated-cost-matrix.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 7</strong>: Dynamic time warping analysis metric.
</span>
</p>

### Identifying disturbances in the time series

<p>
<img style="background-color: #fff" width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework12/results/threshold-disturbance.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 8</strong>: Identification of perturbations in the time series.
</span>
</p>

### References <a href="#table_of_content"> ^</a> <span id="references"></span>
<hr />

<li id="goodfellow_deep_2016">
Goodfellow, I., Bengio, Y. and Courville, A., 2016. Deep learning. MIT press.
</li>

<li id="dupond_thorough_2019">
Dupond, S., 2019. A thorough review on the current advance of neural network structures. Annual Reviews in Control, 14, pp.200-230.
</li>

<li id="rumelhart_learning_1986">
Rumelhart, D.E., Hinton, G.E. and Williams, R.J., 1986. Learning representations by back-propagating errors. Nature, 323(6088), pp.533-536.
</li>

<li id="hochreiter_long_1997">
Hochreiter, S. and Schmidhuber, J., 1997. Long short-term memory. Neural computation, 9(8), pp.1735-1780.
</li>

<li id="kawakami_supervised_2008">
Graves, A., 2012. Supervised Sequence Labelling with Recurrent Neural Networks. Studiesin Computational Intelligence.
</li>




