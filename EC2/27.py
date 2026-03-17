import boto3
import random

ec2 = boto3.resource('ec2' , endpoint_url="http://localhost:4566")
random_no = random.randint(1,10000)
GroupNamee = f"APP_{random_no}"
print(GroupNamee)
print('*' * 80)
SG =  ec2.meta.client.create_security_group(
    Description='New Security Group',
    GroupName=GroupNamee,
    VpcId='vpc-ca8e69fec9c86fd8a',
)

Security_Group_id = SG['GroupId']

print(Security_Group_id)
# # vpc-ca8e69fec9c86fd8a
print('*' * 80)

volume = ec2.create_volume(
        AvailabilityZone='eu-west-1a',
        Encrypted=True,
        Iops=123,
        Size=25,        
        VolumeType='gp3',
        )

volume_id = volume.id
print(volume_id)
print('*' * 80)

instance = ec2.create_instances(
        ImageId="ami-0ce2e29a2d366cc93",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
)
instance1= instance[0]
print(instance1.id)

print('*' * 80)

instance1.wait_until_running()
print("instance is running")
print("*" * 80)

volume_attach = ec2.meta.client.attach_volume(
        InstanceId = instance1.id,
        VolumeId = volume.id,
        Device = 'xvdc'
)

ec2.meta.client.modify_instance_attribute(
    InstanceId=instance1.id,
    Groups=[Security_Group_id]
)
print(f"volume : {volume.id} and security grp : {Security_Group_id} attch to the {instance1.id}")
