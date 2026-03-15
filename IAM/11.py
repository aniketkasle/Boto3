import boto3

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

list_users1 = iam.list_users()

list_user = []

for user in list_users1['Users']:
    user_name = user['UserName']
    access_key = iam.list_access_keys(UserName=user_name)
    # print('=' * 99)
    for key in access_key['AccessKeyMetadata']:
        # print(key['AccessKeyId'])
        key_id = key['AccessKeyId']
        print(f"{user_name} access keyid {key_id}")
        
        delete_access_key = iam.delete_access_key(
            UserName=user_name,
            AccessKeyId=key_id)
    print('=' * 99)
        
    
    list_user.append(user['UserName'])
    
print(list_user)