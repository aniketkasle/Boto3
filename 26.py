import boto3

ec2 = boto3.resource('ec2', endpoint_url="http://localhost:4566")

response = ec2.meta.client.describe_instances()

print(response)


# for reservations in response['Reservations']:
#     for instance in reservations['Instances']:
#         instance_id = instance['InstanceId']
#         print(f"terminating instance :  {instance_id}")

#         ec2.meta.client.terminate_instances(
#             InstanceIds=[instance_id]
#         )

#         print(f"Instance termination initiated : {instance_id}")



