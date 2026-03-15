import boto3

ec2 = boto3.client('ec2' , endpoint_url="http://localhost:4566")

stopped_instances = ec2.describe_instances(
    Filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

)

for reservation in stopped_instances['Reservations']:
    for instance in reservation['Instances']:
        instances1 = instance['InstanceId']

        stop_instance = ec2.stop_instances(
            InstanceIds = [instances1]
        )
        print('stopped instances : ', instances1)

        terminate = ec2.terminate_instances(
            InstanceIds = [instances1]
        )
    
        print('Terminated the instance : ', terminate)

        print('*' * 80)