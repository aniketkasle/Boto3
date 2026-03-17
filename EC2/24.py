import boto3

ec2 = boto3.resource('ec2', endpoint_url="http://localhost:4566")

for index in range(0,3):

    volume1 = ec2.create_volume(
        AvailabilityZone='eu-west-1a',
        Encrypted=True,
        Iops=123,
        Size=25,        
        VolumeType='gp3',
        )
    print(f"Volume ID : {volume1.id}")

    print('-' * 80)

    instance1 = ec2.create_instances(
        ImageId="ami-0ce2e29a2d366cc93",
        InstanceType="t2.micro",
        MinCount=1,
        MaxCount=1
    )

    instance2 = instance1[0]
    print("Instace id :", instance2.id)

    print("-" * 80)

    instance2.wait_until_running()
    print("instance is running")
    print("-" * 80)

    volume_attach = ec2.meta.client.attach_volume(

        InstanceId = instance2.id,
        VolumeId = volume1.id,
        Device = 'xvdc'
        
    )

    print(f"volume id {volume1.id} is attached to instance {instance2.id}")
    print("=" * 80)

for instances in ec2.instances.all():
    print(f"ID : {instances.id}")