import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
    ImageId="ami-0ce2e29a2d366cc93",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="my-keypair",
    SecurityGroupIds=["sg-0eb9375b73ead0aad"],
    SubnetId="subnet-042920551f6ff256e",


)

instance = instances[0]
print("Created instances : ", instance.id)

instance.wait_until_running()
print("instace is running")