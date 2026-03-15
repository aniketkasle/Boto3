import boto3
import random

ec2 = boto3.resource('ec2' , endpoint_url="http://localhost:4566")

for index in range(0,2):

    random_no = random.randint(1,10000)
    GroupNamee = f"APP_{random_no}"
    print(GroupNamee)
    print("-" * 80)

    SG = ec2.meta.client.create_security_group(
    Description='New Security Group',
    GroupName=GroupNamee,
    VpcId='vpc-ca8e69fec9c86fd8a',
    )
    Security_Group_id = SG['GroupId']

    print(Security_Group_id)
    print('-'*80)

    Volume1 = ec2.create_volume(
        AvailabilityZone='eu-west-1a',
        Encrypted=True,
        Iops=123,
        Size=25,        
        VolumeType='gp3',
        )
    
    volume_id = Volume1.id
    print(volume_id)
    print("-" * 80)

    instance1 = ec2.create_instances(
        ImageId="ami-0ce2e29a2d366cc93",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
        )
    
    instance2 = instance1[0]
    print(instance2.id)

    print('-' * 80)

    instance2.wait_until_running()
    print("Instance2 is running now")

    print('-'*80)

    ec2.meta.client.attach_volume(
        InstanceId = instance2.id,
        VolumeId = volume_id,
        Device = 'xvdc'
        )
    
    ec2.meta.client.modify_instance_attribute(
    InstanceId=instance2.id,
    Groups=[Security_Group_id]
    )

    print(f"Volume : {volume_id} and security group : {Security_Group_id} attach to the instance : {instance2}")
    print('='*80)

