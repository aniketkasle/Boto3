import boto3

s3 = boto3.client('s3')
Bucket_name = 'terraform-aws-logs-public-for-terraform-541fh45'
s3.put_public_access_block(

    Bucket = Bucket_name,
    PublicAccessBlockConfiguration={
                    'BlockPublicAcls': False,
                    'IgnorePublicAcls': False,
                    'BlockPublicPolicy': False,
                    'RestrictPublicBuckets': False
                },
                

)


print(f"public access disable succesfully: {Bucket_name}")
