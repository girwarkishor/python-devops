import boto3
import os
#aws_access_key_id = ""
#aws_secret_access_key = ""


client = boto3.resource(
    "s3",
    aws_access_key_id=os.environ["aws_access_key_id"],
    aws_secret_access_key=os.environ["aws_secret_access_key"],
    region_name=os.environ["region_name"]
)

bucket = client.Bucket("foodjet")
k = bucket.objects.all()
for each in k:
    print(each.key)


response = client.list_objects(
    Bucket='foodjet',
)

# print(response)

