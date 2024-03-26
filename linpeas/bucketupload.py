import boto3
import pandas as pd

s3 = boto3.client('s3')

s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIA33FHZNAJ3OOWXWXB',
    aws_secret_access_key='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'
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload files to S3 bucket
s3.Bucket('securelykavach').upload_file(Filename='wout.pdf', Key='wout.pdf')

for obj in s3.Bucket('securelykavach').objects.all():
    print(obj)