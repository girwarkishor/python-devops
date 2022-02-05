import boto3
import os

IMAGE_ID = 'ami-03fa4afc89e4a8a09'
SHAPE = 't2.micro'

client = boto3.resource(
    "ec2",
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"],
    region_name=os.environ["region_name"]
)


ec2_instance = client.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId=IMAGE_ID,
    InstanceType=SHAPE,
    KeyName="KUNA_KEY_PAIR",
)

for instance in ec2_instance:
    print(f"instance id is {instance.id}")

    instance.wait_until_running()
    print("ec2 is running")
