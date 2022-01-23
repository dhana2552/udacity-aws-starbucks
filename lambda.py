#Tried Lambda
import json
import boto3
import csv
import random

# Endpoint name of deployed model
ENDPOINT = "linear-learner-2022-01-23-03-32-17-060"
s3 = boto3.client('s3')

def lambda_handler(event, context):

    runtime= boto3.client('runtime.sagemaker')
    
    # Get csv data from s3
    key = event['s3_key']
    bucket = event['s3_bucket']
    csvfile = s3.get_object(Bucket=bucket, Key=key)
    
    #Read the csv
    csv_data = csvfile['Body'].read().split(b'\n')
    
    #Read a record from data dump
    index = random.choice(range(100))
    payload = csv_data[index]

    #Invoke Endopint to get the response
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                       ContentType='text/csv',
                                       Body=payload)
    result = json.loads(response['Body'].read().decode())

    #Response to be returned
    return {
        'statusCode': 200,
        'body': {
            "s3_bucket": bucket,
            "s3_key": key,
            "output": result,
        } 
    }
    
    #Test Event
# {
#   "test_data": "test_data",
#   "s3_bucket": "sagemaker-us-east-1-456758360141",
#   "s3_key": "test/test.csv"
# }