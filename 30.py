import boto3

ec2 = boto3.resource('ec2',endpoint_url="http://localhost:4566")

stopped_instances = ec2.meta.client.describe_instances(
    Filters = [ {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }]
)
instace_need_to_start = []
for reservation in stopped_instances['Reservations']:
    for instance in reservation['Instances']:
        instace_need_to_start.append(instance['InstanceId'])


if not instace_need_to_start:
    print("Stopped instances not found")
    exit()
    

print(instace_need_to_start)

try:
    start_instace = ec2.meta.client.start_instances(InstanceIds = instace_need_to_start)

    waiter = ec2.meta.client.get_waiter('instance_running')
    waiter.wait(InstanceIds=instace_need_to_start)
    print(f"now instance is running : {start_instace}")

except Exception as e:
        print(f"An error occurred: {e}")

