import json

from argparse_files import args
from elasticsearch import Elasticsearch


SERVER_NAME = "localhost"
PORT = "9200"

class EsOperations():
    def __init__(self, server, port):
        self.host = server
        self.port = port

    def connect(self):
        connection = Elasticsearch([{'host': self.host, 'port':self.port}])
        return connection

    def check_connection(self, conn):
        if not conn or not conn.ping():
            raise ValueError("Connection not established")

    def create_index(self, conn, index, id, document):
        """To create the table in elastic search

        Args:
            conn(es object): Connection of es container
            index(str): Table name in es
            id(int): Row id of table
            document(dict): Json data

        Returns:
            response(str): es message data
        """
        response = conn.index(index=index, id=id, document=document)
        return response


def read_file(file_path):
    with open(file_path, "r") as config_data:
        data = config_data.read()
        dict_data = json.loads(data)
    return dict_data


filename = args.filename
index = args.index
row = args.row
es_connect = EsOperations(SERVER_NAME, PORT)
connection_obj = es_connect.connect()
es_connect.check_connection(connection_obj)
response = es_connect.create_index(connection_obj, index, row, read_file(filename))
print(response)
print("End result ", response["_shards"]["successful"])

