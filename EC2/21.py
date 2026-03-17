import boto3

ec2 = boto3.client('ec2')

# Instance = ec2.stop_instances(InstanceIds=[
#         'i-09f178148b329e0bd','i-02b28f5e4b1f4c850','i-085569552dcb5229f'
#     ],Hibernate=False,
    
#     DryRun=False,
#     Force=True
#     )

instance = ec2.terminate_instances(
    InstanceIds = ['i-0a6fcddcc65116bad']
)

