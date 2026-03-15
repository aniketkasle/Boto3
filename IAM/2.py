import boto3
import random

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")
random_int = random.randint(1,1000)
username = f"App0_{random_int}"

user = iam.create_user(
    UserName = username
)

print(user)
print('*' * 80)
list = iam.list_users()

for users in list['Users']:
    user1 = users['UserName']
    

    iam.delete_user(
        UserName = user1
    )

    print(f"deleted user : {user1}")
    print('*' * 80)
