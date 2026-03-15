import boto3

ec2 = boto3.resource('ec2', endpoint_url="http://localhost:4566")

for instance in ec2.instances.all():
    print(f"InstanceID  : {instance.id}")
    print(f"Instancetype : {instance.instance_type}")