import boto3

a3 = boto3.client('s3')
response = a3.list_buckets()

print("Bucket containing public : ")
for bucket in response['Buckets']:
    if 'public' in bucket['Name'].lower():
        print(bucket['Name'])