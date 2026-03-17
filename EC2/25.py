import boto3

ec2 = boto3.resource('ec2', endpoint_url="http://localhost:4566")

# for instance in ec2.instances.all():
#     print(f"instance id  : {instance.id}")

instance1 = ec2.instances.all()

instance_id = [instance.id for instance in instance1]

print(instance_id)

if instance_id:
    ec2.meta.client.terminate_instances(
        InstanceIds = instance_id
    )
    print("insatnces terminates succesfully")

else:
    print("failed to terminate")




