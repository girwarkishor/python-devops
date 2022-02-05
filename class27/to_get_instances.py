import boto3
import os

IMAGE_ID = 'ami-03fa4afc89e4a8a09'
SHAPE = 't2.micro'
KEY_PAIR = 'KUNA_KEY_PAIR'

class Ec2Services:
    def __init__(self, name, filter):
        self.name = name
        self.filter = filter
        self.client = self.init_aws_access()
        self.ids_list = []

    def init_aws_access(self):
        client = boto3.resource(
            "ec2",
            aws_access_key_id=os.environ["aws_access_key_id"],
            aws_secret_access_key=os.environ["aws_secret_access_key"],
            region_name=os.environ["region_name"]
        )
        return client

    def get_id(self):
        # https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-status.html

        instances = self.client.instances.filter(
            Filters=[
                {
                    'Name': self.name,
                    'Values': [
                        self.filter
                    ]
                }
            ]
        )

        for instance in instances:
           self.ids_list.append(instance.id)

        return self.ids_list

    def create_ec2_instance(self):
        ec2_instance = self.client.create_instances(
            MinCount=1,
            MaxCount=1,
            ImageId=IMAGE_ID,
            InstanceType=SHAPE,
            KeyName=KEY_PAIR,
        )

        for instance in ec2_instance:
            print(f"instance id is {instance.id}")

            instance.wait_until_running()
            print("ec2 is running")
        return instance
