import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
list1 = s3.meta.client.list_buckets()
for bucket in list1['Buckets']:
    print(bucket['Name'])

print("=" * 80)

try : 
    encrypt = s3.meta.client.get_bucket_encryption(
    Bucket = bucket['Name'])
    print("bucket encrypted successfully")

except ClientError as error:
    print('eroor : ' ,error)

print("=" * 80)

try : 
    public_access = s3.meta.client.put_public_access_block(
        Bucket=bucket['Name'],
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
    }
    
)
    print("successfully blocked public access")
    
except ClientError as e:
    print("error : " , e)
print("=" * 80)
