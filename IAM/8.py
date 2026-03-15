import boto3
import random
import json

iam = boto3.client('iam', endpoint_url="http://localhost:4566")

random_no = random.randint(1,10000)
random_role_name = f"SSM_ROLE_INEO_{random_no}"

print(random_role_name)
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
    RoleName=random_role_name,
    AssumeRolePolicyDocument =json_trust_policy
)

print(new_role)
print('*'*80)
response = iam.list_roles()
for rolename in response['Roles']:
    print(rolename['RoleName'])

print('*'*80)

randome_user = f"Aniket_{random_no}"
new_user = iam.create_user(UserName = randome_user)
print(new_user)

print('*'*80)

list = iam.list_users()

for user in list['Users']:
    print(user['UserName'])

print('*'*80)

group_name = f"Developer_{random_no}"
Group1 = iam.create_group(
    GroupName=group_name
)

list_group = iam.list_groups()

for group2 in list_group['Groups']:
    Group_Name = group2['GroupName']
    print(Group_Name)



user_add_group = iam.add_user_to_group(
    GroupName=group_name,
    UserName=randome_user
)
print('*'*80)
