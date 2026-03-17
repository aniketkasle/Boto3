import boto3

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

list_groups = iam.list_groups()
# print(list_groups['Groups']['GroupName'])
list_groups1 = []
for groupame in list_groups['Groups']:
    list_groups1.append(groupame['GroupName'])
    list_user_group1 = iam.get_group(GroupName=groupame['GroupName'])
    user_list = []
    for user in list_user_group1['Users']:
        user_list.append(user['UserName'])
        # users_name1 = user['UserName']
    print(f"Users in group {groupame['GroupName']} : {user_list}")
    print('=' * 99)

print(list_groups1)

