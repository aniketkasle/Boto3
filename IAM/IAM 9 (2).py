import boto3
a3 = boto3.client('iam')
response = a3.delete_policy(
    PolicyArn = 'arn:aws:iam::391254865145:policy/s3-get'
)
