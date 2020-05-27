import boto3
import pandas as pd
import logging
import os


client = boto3.client('s3')
s3 = boto3.resource('s3')
        
log_file_name = 'AWS_Console/AWS Console.log'
bucket = 'septa-redshift-data-load'

filename = r'C:\Users\asvh\Documents\Projects\Efficiency Review\Budget Reports\Departmental Spending.csv'

def start_logger(log_file_name):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    log_format = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')

    file_handler = logging.FileHandler(log_file_name)

    file_handler.setFormatter(log_format)

    logger.addHandler(file_handler)
    logger.info('Running {}'.format(__name__))

def upload_to_aws(filename, bucket):
    try:
        logger.info('Uploading File to bucket {}'.format(bucket))
        s3.meta.client.upload_file(filename,bucket,'DSD test.csv')
        logger.info('File Successfully uploaded')

    except Exception as e:
        logger.error(e)
        logger.exception(e)


start_logger(log_file_name)

my_bucket = s3.Bucket(bucket)

for i in my_bucket.objects.all():
    print(i)
