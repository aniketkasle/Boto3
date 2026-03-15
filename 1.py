import boto3

s3 = boto3.client('s3', endpoint_url="http://localhost:4566",  # VERY IMPORTANT
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="eu-west-1")


bucket_name = "my-simple-buckzasfdfet-1zydfetsdgd-public"  
region = "eu-west-1"                     

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print("S3 bucket created successfully")
