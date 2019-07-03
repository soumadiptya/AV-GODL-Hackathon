# AV-GODL-Hackathon
**Approach and Codes for the Analytics Vidhya Game of Deep Learning competition**
## Competition Link
https://datahack.analyticsvidhya.com/contest/game-of-deep-learning/

## Problem Statement
This was a multi class Image Classification Problem involving classifying ships into one of 5 categories. Class labels were as follows:
* Container
* Cargo
* Cruise
* Millitary
* Tanker<br>
Images were separated into train and test datasets. <br>
Size of Train - 6480 images <br>
Size of Test - 2680 images <br>
Evaluation Metric for the competition was Weighted F1 score.

## Approach
Due to the relatively small size of Training data, transfer learning was the obvious choice of a solution istead of training a model from scratch. I used the fast AI libray for the contest as it had many best practices for transfer learning incorporated in it.

Used 5 different models - Resnet 18, Resnet 34, Resnet 50, VGG 16 and Densenet. Final predictions were majority class selection of 5 models.

Default Image augmentations provided by the Fast AI library were used and models were trained by unfreezing all layers, selecting a best Learning rate (using lr.find()) and training for 5-10 epochs using the **fit_one_cycle** method

## Final Ranks obtained
Public Leaderbaord- 48/2083, Weighted F1 score - 0.9757 (First Rank- 0.9906)<br>
Private Leaderbaord- 38/2083, Weighted F1 score - 0.9714 (First Rank- 0.9853)<br>

## Approaches for improving rank
After going through the solutions provided by the Top 10 participants following themes seemed to stand out commonly:
1) First and foremost was using deeper models with more layers such as resnet101/resnet152/densenet161/densenet169 etc.
2) Using better loss function such as Focal Loss
3) Ensembling using different Image sizes and different Image augmentation techniques
