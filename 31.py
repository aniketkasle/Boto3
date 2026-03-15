import boto3

ec2 = boto3.client('ec2' , endpoint_url="http://localhost:4566")

response  = ec2.describe_instances(
    Filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        },
        {
            'Name': 'tag:Environment',
            'Values': ['Prod']
        }
    ]
)

# print(response)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        Instance1 = instance['InstanceId']

        print(Instance1)

        if not Instance1:
            print("no matching running instance found")
        else:
            print("instance to stop :", Instance1 )

            ec2.start_instances(InstanceIds = [Instance1])
            print(f"Stopping instance : {Instance1}")