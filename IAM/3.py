import boto3
import random

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

id1 = random.randint(1, 10000)
group_name = f"App0_{id1}"

Group = iam.create_group(
    GroupName=group_name
)

# print(f"Group {Group} is created successfully") 


list_group = iam.list_groups()


for group in list_group['Groups']:
    group1 = group['GroupName']
    print(group1)


