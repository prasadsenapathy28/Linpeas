import boto3

s3 = boto3.client('s3')

bucket_name = 'securelykavach'
object_key = 'ex.json'

response = s3.get_object(Bucket=bucket_name, Key=object_key)
json_content = response['Body'].read().decode('utf-8')

print(json_content)