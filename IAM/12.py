import boto3
import random
import json

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

list_role = iam.list_roles()
# print(list_role)

role_name1 = []

for role in list_role['Roles']:

    # print(role['RoleName'])
    role_name1.append(role['RoleName'])
print(role_name1)
print('=' * 99)
permission_role = random.choice(role_name1)
print(permission_role)
    #  print('=' * 99)
    # role_name = random.choice(role['RoleName'])
    # print(role_name)
    # # print(role['RoleName'])
print('=' * 99)
attache_permissions = iam.list_attached_role_policies(RoleName = permission_role)
print(attache_permissions)