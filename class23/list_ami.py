import boto3
import os

client = boto3.client(
    "ec2",
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"],
    region_name=os.environ["region_name"]
)


images = client.describe_images()
# images = client.describe_images(Owners=['self'])

print(images)