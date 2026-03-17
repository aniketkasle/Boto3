import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

try:
    response = s3.list_buckets()
    buckets = response['Buckets']

    for bucket in buckets:
        bucket_name = bucket['Name']

        if "public" in bucket_name.lower():
            print(f"processing bucket : {bucket_name}")
            print("-" * 10)

            s3.put_public_access_block(
                Bucket = bucket_name,
                PublicAccessBlockConfiguration={
                    'BlockPublicAcls': True,
                    'IgnorePublicAcls': True,
                    'BlockPublicPolicy': True,
                    'RestrictPublicBuckets': True
                }
            )

            print(f"public access disbaled for : {bucket_name}")
            print("-" * 10)

except ClientError as es:
    print("Error:", 'es')


