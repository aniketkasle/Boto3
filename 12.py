import boto3

ec2 = boto3.client('ec2', endpoint_url="http://localhost:4566")

response = ec2.describe_instances(
    InstanceIds = ['i-0746f2bd1c3ff12b4']
)

print(response)