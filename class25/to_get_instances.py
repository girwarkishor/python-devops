import boto3
import os

client = boto3.resource(
    "ec2",
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"],
    region_name=os.environ["region_name"]
)

# https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-status.html

instances = client.instances.filter(
    # InstanceIds=[
    #         "i-075f46586dbfc2acf"
    # ]
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running'
            ]
        }
    ]
)

for instance in instances:
    print(f"EC2 instance with id {instance.id}")