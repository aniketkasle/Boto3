import boto3

# s3 = boto3.client('s3')

# response = s3.list_buckets()

# print('List of Buckets : ', response)
# print('=' * 80)

# for bucket in response['Buckets']:
#     print(bucket['Name'])

# print('=' * 80)

# for bucket in response['Buckets']:
#     print(bucket['Name'],bucket['CreationDate'])

s3 = boto3.resource('s3')

s3_list = s3.meta.client.list_buckets()
print('List of bucket : ', s3_list)

print('=' * 80)

for bucket in s3_list['Buckets']:
    print(bucket['Name']) 