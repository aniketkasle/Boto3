import boto3

ec2 = boto3.resource('ec2')

volume = ec2.create_volume(
    AvailabilityZone='eu-west-1a',
    Encrypted=True,
    Iops=123,
    Size=123,
    SnapshotId='snap-0541595fa43d07c23',
    VolumeType='gp3'
    )


print('created volume : ', volume)
print("-" * 50)

instance = ec2.create_instances(

    ImageId="ami-0ce2e29a2d366cc93",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="my-keypair",
    SecurityGroupIds=["sg-0eb9375b73ead0aad"],
    SubnetId="subnet-042920551f6ff256e",
   
)

instance1 = instance[0]
print ('created instace : ', instance1.id)
print("-" * 50)

instance1.wait_until_running()
print("instace is running")
print("-" * 50)

attche = ec2.meta.client.attach_volume(
    
    InstanceId=instance1.id,
    VolumeId=volume.id,
    Device='xvdc',
)