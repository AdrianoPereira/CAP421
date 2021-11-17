<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework11/images/cover-homework11.png" style="width: 100%;">

## Overview
<hr />

This notebook contains exercise 11 (optional exercise 02). This exercise was proposed by Professor Valdivino Santiago Júnior in the course CAP421 - Deep Learning offered in the Postgraduate Program in Applied Computing at the National Institute for Space Research.

**Exercise optional 02:**
> Explain why the "new" proposed DenseNet-83 has more trainable parameters and demands more memory (parameters) than the DenseNet-121. Create a simple network with some dense blocks (enventually transition layers), calculate the number os trainable parameters and related memory to solve this exercise.

## Table of content
<hr />

* [1. DenseNet](#densenet)
    * [1.1. Camada de entrada](#input_layer)
    * [1.2. Blocos densos](#dense_blocks)
    * [1.3. Camadas de transição](#transition_layers)
    * [1.4. Camada de saída](#output_layer)
* [2. Configurando experimentos](#experiments)
    * [2.1. Importação das bibliotecas e configurações](#import_libraries)
    * [2.2. Carregando dados](#load_data)
    * [2.3. Implementando a DenseNet](#densenet_implementation)
    * [2.4. Criando e compilando modelos](#create_models)
    * [2.5. Treinando e salvando DenseNet-121](#training_densenet121)
    * [2.6. Treinando e salvando DenseNet-83](#training_densenet83)
    * [2.7. Comparação e avaliação dos modelos](#evaluate_models)
* [3. Referências](#references)

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