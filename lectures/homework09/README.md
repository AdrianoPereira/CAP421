<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework09/images/cover-data-augmentation.png" style="width: 100%;">

## Overview
<hr />
This folder contains the notebook with some data augmentation techniques for machine learning and exercise 9. This exercise was proposed by Professor Thales Körting in the discipline CAP421 - Deep Learning offered in the Graduate Program in Applied Computing at the National Institute for Space Research.

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/13wuRCJSO37zepGvs2nG2IxE0SoGFrtzV/view?usp=sharing)

[![Open Repository](https://img.shields.io/badge/GitHub-Open%20Repository-lightgrey?logo=github)](https://github.com/AdrianoPereira/CAP421/tree/main/lectures/homework09)

## Data augmentation techeniques
<hr />
In this work, some of the main data augmentation techniques were applied:

* Random rotation;
* Random flip;
* Random Zoom;
* Random Contrast;
* Brightness; and
* HUE

### Example using HUE
The Figure [1](#fig01) shows a sample image of the pasture class with some HUE transformations.

<p id="fig01">
<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework09/images/sample_HUE.png" title="Pasture sample image with Random HUE adjust" style="width: 100%;"/>
<span style="display: block; text-align: center;"><strong>Figure 1</strong>: Pasture sample image with Random HUE adjust.</span>
</p> 

Figure [2] (# fig02) shows some information about the attribute space (RGB Channel) of the sample image of the pasture class with some HUE.

<p id="fig02">
<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework09/images/space_attrs_HUE.png" title="Pasture sample image with Random HUE adjust" style="width: 100%;"/>
<span style="display: block; text-align: center;"><strong>Figure 2</strong>: Comparison between the attribute space of the original image and the image with HUE adjustment.</span>
</p> 

## Data augmentation in training a CNN
<hr />
Two experiments were created. In the first experiment, the classification model was trained with the data set without augmentation data. In the second experiment, the data model was used with the data augmentation in the pasture class, according to exercise 1 below:

> Create new X_train and y_train datasets, called X_train_allDA_Pasture and y_train_allDA_Pasture containing all the previously indicated DA techniques:
> 
> * Rotation
> * Flip
> * Zoom
> * Contrast
> * Brightness
> * Hue
> 
> You should apply only one DA technique to each sample of the class Pasture. Create a classification model similar to the previous ones, showing similar reports (accuraccy and loss graphics, plus confusion matrix and classification reports).

For both models, the transfer learning technique from the VGG9 architecture was used. The weights of the feature extractors of this neural network were loaded from training with the ImageNet dataset. The fully connected network has been defined with one hidden layer, 256 neurons, 50% dropout rate and ReLU activation function. The output layer has been defined with 10 neurons using softmax activation function. The model summary is shown below. 

```console
Model: "model_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_2 (InputLayer)         [(None, 64, 64, 3)]       0         
_________________________________________________________________
block1_conv1 (Conv2D)        (None, 64, 64, 64)        1792      
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 64, 64, 64)        36928     
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 32, 32, 64)        0         
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 32, 32, 128)       73856     
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 32, 32, 128)       147584    
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 16, 16, 128)       0         
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 16, 16, 256)       295168    
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 16, 16, 256)       590080    
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 16, 16, 256)       590080    
_________________________________________________________________
block3_conv4 (Conv2D)        (None, 16, 16, 256)       590080    
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 8, 8, 256)         0         
_________________________________________________________________
block4_conv1 (Conv2D)        (None, 8, 8, 512)         1180160   
_________________________________________________________________
block4_conv2 (Conv2D)        (None, 8, 8, 512)         2359808   
_________________________________________________________________
block4_conv3 (Conv2D)        (None, 8, 8, 512)         2359808   
_________________________________________________________________
block4_conv4 (Conv2D)        (None, 8, 8, 512)         2359808   
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 4, 4, 512)         0         
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 4, 4, 512)         2359808   
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 4, 4, 512)         2359808   
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 4, 4, 512)         2359808   
_________________________________________________________________
block5_conv4 (Conv2D)        (None, 4, 4, 512)         2359808   
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 2, 2, 512)         0         
_________________________________________________________________
flatten_2 (Flatten)          (None, 2048)              0         
_________________________________________________________________
dense_4 (Dense)              (None, 256)               524544    
_________________________________________________________________
dropout_2 (Dropout)          (None, 256)               0         
_________________________________________________________________
dense_5 (Dense)              (None, 10)                2570      
=================================================================
Total params: 20,551,498
Trainable params: 527,114
Non-trainable params: 20,024,384
_________________________________________________________________
```

The Figure [3](#fig03) shown the comparison of training history and validation between the model with data augmentation and the model without data augmentation. The categorical crossentropy loss and accuracy are plotted.

<p id="fig02">
<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework09/images/train_comp-history.png" title="Loss and accuracy history for both models" style="width: 100%;"/>
<span style="display: block; text-align: center;"><strong>Figure 3</strong>: Loss and accuracy history for both models.</span>
</p> 

Figure [4](#fig04) shows the comparison between the two models by the confusion matrix.

<p id="fig02">
<img src="https://raw.githubusercontent.com/AdrianoPereira/CAP421/main/lectures/homework09/images/confusion_matrix_model_comp.png" title="Confusion matrix for both models" style="width: 100%;"/>
<span style="display: block; text-align: center;"><strong>Figure 4</strong>: Confusion matrix for both models.</span>
</p> 


