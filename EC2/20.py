import boto3

ec2 = boto3.resource('ec2')

Instance1 = ec2.create_instances(

    ImageId="ami-0ce2e29a2d366cc93",
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1,
    KeyName="my-keypair",
    SecurityGroupIds=["sg-0eb9375b73ead0aad"],
    SubnetId="subnet-042920551f6ff256e",
   TagSpecifications=[
        {
        "ResourceType": "instance",
            'Tags': [
                
                    {"Key": "Name", "Value": "Dev-Server"},
                    {"Key": "Environment", "Value": "Dev"},
                    {"Key": "Owner", "Value": "WS8182"},
                    {"Key": "Project", "Value": "CloudMigration"}
                
            ]
        },
    ]
)

Instance2 = Instance1[0]
print("Instance is ready : ", Instance2.id)