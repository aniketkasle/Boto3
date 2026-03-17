import boto3

a3 = boto3.client('s3')

response = a3.list_buckets()

for bucket in response['Buckets']:
    bucket_name = bucket['Name']
    a3.put_bucket_tagging(
          Bucket=bucket_name,
          Tagging={
        'TagSet': [
            {
                'Key': 'Status',
                'Value': 'Active'
            },
             {
                'Key': 'Owner',
                'Value': 'Aniket'
            }
        ]
    }
    )
    
    print(f"bucket tagged now: {bucket_name}")