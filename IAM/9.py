import boto3

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

response = iam.list_roles()
# print(response)

for rolename in response['Roles']:
    print(rolename['RoleName'])

print('=' * 80)
user_list = iam.list_users()

for user1 in user_list['Users']:
    print(user1['UserName'])
# print(user_list)