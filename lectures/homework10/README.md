<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework10/images/cover-label-smoothing.png" style="width: 100%;">

### OVERVIEW
<hr />

[This notebook](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework10/CROSS_ENTROPY_AND_LABEL_SMOOTHING_EN.ipynb) contains exercise 10 (optional exercise 01) which deals with label smoothing, a kind of regularization of neural networks. This exercise was proposed by Professor Valdivino Santiago Júnior in the course CAP421 - Deep Learning offered in the Postgraduate Program in Applied Computing at the National Institute for Space Research.

**Full Notebook avaiable at**: [https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework10/CROSS_ENTROPY_AND_LABEL_SMOOTHING_EN.ipynb](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework10/CROSS_ENTROPY_AND_LABEL_SMOOTHING_EN.ipynb). 

**Author:** Adriano P. Almeida <<adriano.almeida@inpe.br>>
<br>
**Created on:** 09 November, 2021
<br />
<a href="https://github.com/AdrianoPereira/CAP421/tree/main/lectures/homework10">
    <img style="float: left; margin-right: 10px;" src="https://img.shields.io/badge/GitHub-Open%20Repository-lightgrey?logo=github" />
</a>
<br />

### Training and validation models
<hr />

The performance of each model during its training was evaluated through the set of tests, defined as a proportion of 15% of the training set. Error and accuracy over epochs were evaluated for the training and validation set. The following Figure show this information.

<p id="fig01">
    <img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework10/images/history.png" />
    <span style="display: block; text-align: center; margin-top: 10px;"><strong>Figure 1</strong>: Traning and validation history of all models.</span> 
</p>

### Evaluation models
<hr />

For the skill of the model with the test dataset, some classical metrics in classification tasks, the information from the confusion matrix and the ROC curve, were used. The following Figure show the confusion matrix for each model trained with different label smoothing factors. The ROC curve is also generated for the average of the false positives and true positives rate. 

<p id="fig02">
    <img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework10/images/confusion_matrix.png" />
    <span style="display: block; text-align: center; margin-top: 10px;"><strong>Figure 2</strong>: Confusion matrix of all models and their average ROC curve.</span> 
</p>

The following Figure show the ROC curve of each model for each class was generated, as shown below.

<p id="fig03">
    <img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework10/images/roc_curve.png" />
    <span style="display: block; text-align: center; margin-top: 10px;"><strong>Figure 3</strong>: ROC curve for all models for each class.</span> 
</p>

### References
<hr />

<ul>
    <li id="goodfellow_deep_2016">
        Goodfellow, I., Bengio, Y. and Courville, A., 2016. Deep learning. MIT press.
    </li>
    <li id="shannon_mathematical_1948">
        Shannon, C.E., 1948. A mathematical theory of communication. The Bell system technical journal, 27(3), pp.379-423.
    </li>
    <li id="murphy_machine_2012">
        Murphy, K.P., 2012. Machine learning: a probabilistic perspective. MIT press.
    </li>
    <li id="galstyan_empirical_2007">
        Galstyan, A. and Cohen, P.R., 2007, June. Empirical comparison of “hard” and “soft” label propagation for relational classification. In International Conference on Inductive Logic Programming (pp. 98-111). Springer, Berlin, Heidelberg.
    </li>
    <li id="szegedy_rethinking_2016">
        Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J. and Wojna, Z., 2016. Rethinking the inception architecture for computer vision. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 2818-2826).
    </li>
    <li id="muller_when_2019">
        Müller, R., Kornblith, S. and Hinton, G., 2019. When does label smoothing help?. arXiv preprint arXiv:1906.02629.
    </li>
    <li id="lecun_lenet5_2015">
        LeCun, Y., 2015. LeNet-5, convolutional neural networks. URL: http://yann.lecun.com/exdb/lenet, 20(5), p.14.
    </li>
    <li id="lecun_backpropagation_1998">
            LeCun, Y., Boser, B., Denker, J.S., Henderson, D., Howard, R.E., Hubbard, W. and Jackel, L.D., 1989. Backpropagation applied to handwritten zip code recognition. Neural computation, 1(4), pp.541-551.
    </li>
</ul>