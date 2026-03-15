import boto3
import random 
iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

user_id = random.randint(1,1000)
user_name =  f"App01_{user_id}"

user_add_group = iam.add_user_to_group(
    GroupName='App0_6200',
    UserName='Aniket_588'
)

print(user_add_group)
response = iam.list_groups_for_user(
    UserName='Aniket_588',
   
)

print(response)