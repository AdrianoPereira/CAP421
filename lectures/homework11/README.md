<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework11/images/cover-homework11.png" style="width: 100%;">

## Overview
<hr />

This notebook contains exercise 11 (optional exercise 02). This exercise was proposed by Professor Valdivino Santiago Júnior in the course CAP421 - Deep Learning offered in the Postgraduate Program in Applied Computing at the National Institute for Space Research.

**Exercise optional 02:**
> Explain why the "new" proposed DenseNet-83 has more trainable parameters and demands more memory (parameters) than the DenseNet-121. Create a simple network with some dense blocks (enventually transition layers), calculate the number os trainable parameters and related memory to solve this exercise.

## Table of content
<hr />

* [1. DenseNet](#densenet)
    * [1.1. Camada de entrada](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#input_layer)
    * [1.2. Blocos densos](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#dense_blocks)
    * [1.3. Camadas de transição](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#transition_layers)
    * [1.4. Camada de saída](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#output_layer)
* [2. Configurando experimentos](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#experiments)
    * [2.1. Importação das bibliotecas e configurações](#import_libraries)
    * [2.2. Carregando dados](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#load_data)
    * [2.3. Implementando a DenseNet](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#densenet_implementation)
    * [2.4. Criando e compilando modelos](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#create_models)
    * [2.5. Treinando e salvando DenseNet-121](#training_densenet121)
    * [2.6. Treinando e salvando DenseNet-83](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#training_densenet83)
    * [2.7. Comparação e avaliação dos modelos](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#evaluate_models)
* [3. Referências](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb#references)

**Author:** Adriano P. Almeida <<adriano.almeida@inpe.br>>
<br />
**Full Notebook avaiable at**: [GitHub](https://github.com/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb) and [Google Colab](https://colab.research.google.com/github/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb)
<br />
**Created on:** 12 November, 2021
<br />

<a href="https://colab.research.google.com/github/AdrianoPereira/CAP421/blob/main/lectures/homework11/DENSENET84_AND_DENSENET121.ipynb">
    <img style="float: left; margin-right: 10px;" src="https://colab.research.google.com/assets/colab-badge.svg" />
</a>

<a href="https://github.com/AdrianoPereira/CAP421/tree/main/lectures/homework11">
    <img style="float: left; margin-right: 10px;" src="https://img.shields.io/badge/GitHub-Open%20Repository-lightgrey?logo=github" />
</a>
<br /><br />

### TRAINING AND VALIDATION HISTORY
<hr />

<p>
<img width="100%" src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework11/results/train_comp-history.png" />
<br />
<span style="display: block; text-align: center;" id="history">
<strong>Figure 1</strong>: Loss and accuracy during the training and validation of models.
</span>
</p>

### Evaluate models
<hr />

| ARCCHITETURE      | TRAIN. PARAMS | NON-TRAIN. PARAMS | TOTAL PARAMS | MEMORY USAGE | EXECUTION TIME | TEST ACCURACY |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| DenseNet-121 | 6964106 | 83648 | 7047754 | 26,885 MB | 8941 s | 77,837% |
| DenseNet-83 | 3718538 | 43832 | 3762370 | 14,352 MB | 4236 s | 75,735% |

<span style="display: block; text-align: center;" id="history">
<strong>Table 1</strong>: Camada de entrada da DenseNet realçada.
</span>


### References
<hr />

<li id="huang_densely_2017">
Huang, G., Liu, Z., Van Der Maaten, L. and Weinberger, K.Q., 2017. Densely connected convolutional networks. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 4700-4708).
</li>

<li id="he_deep_2016">
He, K., Zhang, X., Ren, S. and Sun, J., 2016. Deep residual learning for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 770-778).
</li>
