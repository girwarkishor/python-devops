import boto3
import os


class GetInstancesIds:
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