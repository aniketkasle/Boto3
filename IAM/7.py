import boto3
import json
import random

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")
random_no = random.randint(1, 5000)

role_name = f"SSM_IAM_{random_no}_Role"
print(role_name)
print('*' * 80)

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

new_role = iam.create_role(
    RoleName=role_name,
    AssumeRolePolicyDocument =json_trust_policy
)

print(new_role)
print('*' * 80)

for policy2 in policy_arn1:
    permission = iam.attach_role_policy(
        RoleName=role_name,
        PolicyArn=policy2
        )
    
    print(permission)
    print('*' * 80)

permission_attch = iam.list_attached_role_policies(RoleName=role_name)
print(permission_attch)

print('*' * 80)

for policy2 in permission_attch['AttachedPolicies']:
    print(policy2['PolicyName'])
print('*' * 80)
    # for policyname1,i in enumerate(policy2):
    #     policy_name = policyname1[i]['PolicyName']

list_role = iam.list_roles()
for rolename in list_role['Roles']:
    print(rolename['RoleName'])
print('*' * 80)