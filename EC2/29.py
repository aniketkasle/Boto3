import boto3


ec2 = boto3.resource('ec2' , endpoint_url="http://localhost:4566")

response  = ec2.meta.client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)


# print(response)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        Instance1 = instance['InstanceId']
        print(f"instance id : {Instance1}")

        tag = ec2.meta.client.create_tags(
            
             Resources=[Instance1],
             Tags=[
        {
            'Key': 'Environment',
            'Value': 'Prod'
        },{
            'Key': 'Application',
            'Value': 'SAP1'
        }])
                

# Descibe_instance = ec2.meta.client.describe_instances(
#     InstanceIds=['i-56d2976791137e176', 'i-df365825e9f28e879']

# )
# print(Descibe_instance)


print(response)