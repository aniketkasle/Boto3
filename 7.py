import boto3

a3 = boto3.client('ec2', endpoint_url="http://localhost:4566")

response = a3.create_volume(
    AvailabilityZone='eu-west-1a',   
    Size=10,                          
    VolumeType='gp3' 

)

print(response)
# print("Volume ID:", response['VolumeId'])
