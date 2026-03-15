import boto3

a1 = boto3.resource('ec2', endpoint_url="http://localhost:4566",  # VERY IMPORTANT
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="eu-west-1")

for index in range(0,4):

    volume = a1.create_volume(
        AvailabilityZone='eu-west-1a',
        Encrypted=True,
        Iops=123,
        Size=25,        
        VolumeType='gp3',
    )

    print("Volume id : " , volume)
    

    instance1 = a1.create_instances(
        ImageId="ami-0ce2e29a2d366cc93",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
        
    )

    instance2 = instance1[0]
    print("Instance id : ", instance2)
    
    instance2.wait_until_running()
    print("instace is running")
    

    volume_attach = a1.meta.client.attach_volume(
        InstanceId=instance2.id,
        VolumeId=volume.id,
        Device='xvdc',
    )
    print(f"{volume.id} is attached to {instance2.id}")
    print('=' * 80)

for instances in a1.instances.all():
    print(f"ID : {instances.id}")

