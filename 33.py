import boto3

ec2 = boto3.client('ec2', endpoint_url="http://localhost:4566")

response = ec2.describe_instances(
    Filters = [ {
            'Name': 'instance-state-name',
            'Values': ['running']
        }]
)

# print(response)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance1 = instance['InstanceId']
        int_type = instance['InstanceType']
        inst_state = instance['State']['Name']
        
        

        print(f"instance id : {instance1} which is type {int_type} which is {inst_state} in state")
        print('*' * 80)

