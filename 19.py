import boto3

ec2 = boto3.client('ec2')

instance_detail = ec2.describe_instances(
    InstanceIds=[
        'i-09c4122846c900d2b',
    ]
)

# print("instancetype is : ", instance_detail['Reservations'][0]['Instances'][0]['InstanceType'])
# print("-" * 50)
print("instance details as below : ", instance_detail)