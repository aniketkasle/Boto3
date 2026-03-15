import boto3
import json

iam = boto3.client('iam' , endpoint_url="http://localhost:4566")

trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

json_trust_polcy = json.dumps(trust_policy)

response  = iam.create_role(
    RoleName='Ec2_SSM_Role',
    AssumeRolePolicyDocument =json_trust_polcy
)

list_roles = iam.list_roles()
print(list_roles)