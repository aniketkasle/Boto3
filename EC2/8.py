import boto3

a3 = boto3.client('ec2')
volume_id = "vol-097960e27e004f099"

a3.delete_volume(VolumeId=volume_id)