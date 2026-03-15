import boto3
import json
import random 

iam1 = boto3.client('iam', endpoint_url="http://localhost:4566")

random_no = random.randint(1,10000)
role_name = f"ec2-role-ssm-{random_no}"

policy_arn1 = [
    "arn:aws:iam::aws:policy/AmazonEC2FullAccess",
    "arn:aws:iam::aws:policy/AmazonS3FullAccess",
    "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
    "arn:aws:iam::aws:policy/CloudWatchFullAccess"   
]

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

json_trust_policy = json.dumps(trust_policy)
iam_role = iam1.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument =json_trust_policy
)

print(iam_role)
print("*" * 80)

for policy1 in policy_arn1:
    permission = iam1.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy1
        )
    print(permission)
    print("*" * 80)

