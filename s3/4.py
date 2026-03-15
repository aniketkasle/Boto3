import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3') 

s3list = s3.meta.client.list_buckets()
for bucket in s3list['Buckets']:
    print(bucket['Name'])

    try:

        encrypt = s3.meta.client.get_bucket_encryption(
            Bucket = bucket['Name']
            )
        print("Bucket encrypted successfully")
    except ClientError as e:
        print("error : ", e)

    
    try:
        version = s3.meta.client.put_bucket_versioning(
            Bucket = bucket['Name'],
            VersioningConfiguration = {
                'Status': 'Enabled'
        })
        print("Bucket version enabled successfully")
    
    except ClientError as e:
        print("error : ", e)
    print("=" * 80)


print("*" * 80)
