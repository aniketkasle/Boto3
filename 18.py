import boto3

ec2 = boto3.resource('ec2')

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
print('Instace id of new Ec2 : ', instance1.id)
print("-" * 50)

instance1.wait_until_running()
print("instance is running")
print("-" * 50)

current_sgs = [sg["GroupId"] for sg in instance1.security_groups]

new_sg = "sg-06fd112384d54db75"

if new_sg not in current_sgs:
    instance1.modify_attribute(Groups = current_sgs + [new_sg])
    print("new security group is attached")
else:
    print("new SG is already attached")








