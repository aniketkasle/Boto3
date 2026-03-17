import boto3

a3 = boto3.client('s3')

response = a3.list_buckets()

for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    a3.put_public_access_block(
        Bucket=bucket_name,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    
    print(f"Public access disabled for bucket: {bucket_name}")