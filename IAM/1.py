import boto3
import random

iam1 = boto3.client('iam',endpoint_url="http://localhost:4566")

random_number = random.randint(10,1000)
name = f"Aniket_{random_number}"
print(name)

print('*'*80)

user = iam1.create_user(UserName = name)
print(f"User is created successful : {name}")

print('*'*80)

list = iam1.list_users()

for user1 in list['Users']:
    print(user1['UserName'])

 