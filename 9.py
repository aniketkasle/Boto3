import boto3

a3 = boto3.client('iam')

response = a3.delete_role(
    RoleName='Aio-read-only'
)


