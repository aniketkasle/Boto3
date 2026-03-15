import boto3

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

response = iam.list_users()

user_list = []
for user2 in response['Users']:
    user_list.append(user2['UserName'])
    print(user2['UserName'])

print('=' * 99)
print(user_list)

print('=' * 99)

# first_user = response['Users'][0]['UserName']
# print(first_user)

# print('=' * 99)

print(user_list[5])
print('=' * 99)
role_access = iam.create_access_key(
    UserName=user_list[2]
)
print(role_access['AccessKey']['AccessKeyId'])
for accesskey1 in role_access['AccessKey']:
    print(accesskey1['AccessKeyId'])
print(role_access)

