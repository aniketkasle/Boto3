import boto3 

ec2 = boto3.client('ec2', endpoint_url="http://localhost:4566")

response = ec2.stop_instances(
    InstanceIds=[
       'i-d193175b81f5d4617'
    ]
)