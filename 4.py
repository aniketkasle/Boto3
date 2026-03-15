import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(f"Deleting objects in bucket: {bucket.name}")
 
    bucket.objects.all().delete()
   
    bucket.delete()
    print(f"Bucket deleted: {bucket.name}")
