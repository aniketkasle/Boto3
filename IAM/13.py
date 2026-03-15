import boto3
import json

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

policy_arn1 = [
    "arn:aws:iam::aws:policy/AmazonEC2FullAccess",
    "arn:aws:iam::aws:policy/AmazonS3FullAccess",
    "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
    "arn:aws:iam::aws:policy/CloudWatchFullAccess"   
]

list_role = iam.list_roles()

for role in list_role['Roles']:
    role_name = role['RoleName']

    for policy2 in policy_arn1:
        iam.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy2
        )
        print(f"{policy2} attached to {role_name}")