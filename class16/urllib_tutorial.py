import urllib3

URL = "http://localhost:9200"

http_object = urllib3.PoolManager()
def get_response():
   data = http_object.request('GET', URL)
   print(data.headers)
   print(data.data.decode())

get_response()