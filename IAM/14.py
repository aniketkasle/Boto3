import boto3
import random

iam = boto3.client('iam', endpoint_url="http://localhost:4566")


# list_usr = iam.list_users()
# # print(list_usr)

# for user1 in list_usr['Users']:
#     print(user1['UserName'])

group_id = random.randint(1,1000)
group_name = f"Developer_grp_{group_id}"

group = iam.create_group(
    GroupName=group_name
)
group1 = group['Group']['GroupName']
print(group1)
print('=' * 99)



# user = iam.create_user(
#     UserName = user_name
# )

for index in range(0,5):
    user_name = f"Avengers_{random.randint(1,10000)}"
    user = iam.create_user(UserName = user_name)
    print(user['User']['UserName'])
    print('=' * 99)
    user_added = iam.add_user_to_group(
        GroupName=group1,
        UserName=user_name
        )

# print(user)
# print('=' * 99)

# user_added = iam.add_user_to_group(
#     GroupName=group,
#     UserName=user
# )

print(f"all the users added in the group : {group1}")
print('=' * 99)

list_user_group1 = iam.get_group(
    GroupName=group1
)
for user in list_user_group1['Users']:
    print(user['UserName'])

