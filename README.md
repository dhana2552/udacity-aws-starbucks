# Starbucks Customer Segmentation

## AWS Machine Learning Engineer Nanodegree

For the capstone, I chose to work on Starbucks dataset provided by Udacity as I found it interesting and there are scopes for analyzing huge data which can be used for addressing many demanding problems in the real-world.

## Overview
In this project, the knowledge and methods learned AWS Machine Learning Engineer Nanodegree course is applied to find whether the given offer is successful or not using AWS ML Workflow.

The datasets are downloaded from Udacity classroom. This data set contains simulated data that mimics customer behavior on the Starbucks rewards mobile app. The data is cleaned and preprocessed and the cleaned data is used to train the model. The model is then used to predict the result.

Then they are trained with various classification algorithms and then evaluated. Finally, it is expected to flow through AWS applications such as S3, Sagemaker, Lambda, API Gateway, etc. to make the model available for use. 

The project will be reported with:
* Jupyter notebook with code run to completion
* HTML export of the jupyter notebook
* PDF file of the report

### Dependencies

```
Python 3.9
Numpy
Pandas >= 1.2.4
Matplotlib
Scikit-learn 0.24 
```

### Installation
For this project, Sagemaker notebook instance is used as an integrated development environment. The datasets, files, outputs etc are stored in s3 and the endpoint is evaluated with lambda function.

## Project Instructions

* Reading the datasets, cleaning them, concatenating them into a single dataset and carefully performing feature engineering into it, to make it model ready –Applications used: AWS S3, Sagemaker Notebook
* The dataset is then divided into train and test – Applications used: AWS S3, Sagemaker Notebook
* In order to build a model with a suitable machine learning algorithm, the dataset needs to be first trained with various classification algorithms and their metrics will be evaluated - Applications used: AWS S3, Sagemaker Notebook
* The most suitable algorithm is then trained with tuned parameters and deployed to get the endpoint - Applications used: AWS S3, Sagemaker Notebook, Sagemaker Inferences
* Finally, the deployed model is evaluated with AWS Lambda

