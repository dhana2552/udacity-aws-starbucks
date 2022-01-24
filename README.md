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

## Project Set Up and Installation
Enter AWS through the gateway in the course and open SageMaker Notebook instance.
Upload the files to the notebook instance.
* JSON files: portfolio.json, profile.json, transcript.json
* Jupyter Notebooks: analyse_and_preprocess.ipynb, train_and_deploy.ipynb, transaction_clean.ipynb
* Python file: lambda_function.py


## Project Instructions
* Reading the datasets, cleaning them, concatenating them into a single dataset and carefully performing feature engineering into it, to make it model ready –Applications used: AWS S3, Sagemaker Notebook
* The dataset is then divided into train and test – Applications used: AWS S3, Sagemaker Notebook
* In order to build a model with a suitable machine learning algorithm, the dataset needs to be first trained with various classification algorithms and their metrics will be evaluated - Applications used: AWS S3, Sagemaker Notebook
* The most suitable algorithm is then trained with tuned parameters and deployed to get the endpoint - Applications used: AWS S3, Sagemaker Notebook, Sagemaker Inferences
* Finally, the deployed model is evaluated with AWS Lambda

## analyse_and_preprocess.ipynb
Here where the datasets are explored, cleaned and concatenated into a single dataset.
The cleaned data is uploaded to s3 bucket.


## train_and_deploy.ipynb
The cleaned data is then accessed from s3 in this notebook. It is then scaled, divided into train and test sets and then trained with Sagemaker's **Linear Learner**.
```
linear = LinearLearner(role = role,
                      train_instance_count = 1,
                      train_instance_type='ml.c4.xlarge',
                      predictor_type='binary_classifier',
                      num_classes=2,
                      output_path=output_path,
                      sagemaker_session=sagemaker_session,
                      epochs = 5)
```
The trained model is then deployed to get an endpoint.

## transaction_clean.ipynb
In this notebook, the whole dataset merged from profile and transcript is used. The main purpose is to assign offer ids to transacted data and then use them in the lambda function to predict if the given offer will be successful for the new customers.

The flow of the notebook is as follows:

* Carefully assign null values in the order of reward -> event -> offer_id in profile_transcript.csv dataset
* Merge the dataset with portfolio dataset
* Clean the dataset and perform feature engineering
* Split the dataset into train and test, then evaluate with Random Forest
* Export to csv and use in lambda function

# Lamba function
Use lambda_function.py to evaluate the deployed endpoints. 






