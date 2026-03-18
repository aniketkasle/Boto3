import boto3
import random

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

list_user = iam.list_users()
# print(list_user)
list_users = []
for user in list_user['Users']:
    list_users.append(user['UserName'])
print(list_users)
print('=' * 99)
user_for_enable_mfa = random.choice(list_users)
print(user_for_enable_mfa)



# mfa_enabled = iam.enable_mfa_device(
#     UserName=user_for_enable_mfa,
#     SerialNumber='arn:aws:iam::123456789012:mfa/Aniket',
#     AuthenticationCode1 = '123456' ,
#     AuthenticationCode2='685854'
# )
print('=' * 99)

# print(f"MFA is setup for the user : {user_for_enable_mfa}")

# enabled_device = iam.list_mfa_devices(
#     UserName=user_for_enable_mfa)

# print(enabled_device)

# print('=' * 99)
mfs_devices = []
for user1 in list_users:
    enbaled_mfs = iam.list_mfa_devices(UserName=user1)
    for username1 in enbaled_mfs['MFADevices']:
        mfs_devices.append(username1['UserName'])
print(mfs_devices)