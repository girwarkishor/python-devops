from elasticsearch import Elasticsearch


class EsOperations():
    def __init__(self, server="localhost", port="9200"):
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




es_connect = EsOperations()
connection_obj = es_connect.connect()
es_connect.check_connection(connection_obj)
response = es_connect.create_index(connection_obj, "rao23", 3, {"name":"rao23"})
print(response)
