import boto3
import os
import botocore

client = boto3.resource(
    "ec2",
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"],
    region_name=os.environ["region_name"]
)

VPC_ID = "vpc-fa8c9092"


try:
    security_group = client.create_security_group(
        Description="sec group from automation",
        GroupName="ssh-group",
        VpcId=VPC_ID,
    )
except botocore.exceptions.ClientError:
    print("sec group already exist")
else:
    security_group.authorize_ingress(
        CidrIp="0.0.0.0/0",
        FromPort=22,
        ToPort=22,
        IpProtocol="tcp"
    )
