import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

File_path = 'C:/Users/anike/OneDrive/Desktop/Aniket/Boto3/s3/my-keypair.pem'
bucket = 'amxh-askjbasdf-sayali-peddawad'
s3_key = '/uploads/Downloads/my-keypair.pem'

try:
    s3.upload_file(File_path , bucket, s3_key)
    print("file uploaded successfully")

except ClientError as error:
    print('eroor : ' ,error)
