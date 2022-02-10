from kubernetes import client, config
import json

config.load_kube_config()


v1 = client.CoreV1Api()
data = v1.list_node()
node_data_dict = data.to_dict()

for each_node in node_data_dict["items"][0]["status"]["addresses"]:
    if "." in each_node["address"]:
        print(each_node["address"])

# data = str(data).replace("\'", "\"")
# print(data)
# k8_data_json = json.loads(str(data))
# print(k8_data_json)

