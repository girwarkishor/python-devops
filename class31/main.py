from kubernetes import client, config
import json
import paramiko

config.load_kube_config()


v1 = client.CoreV1Api()
data = v1.list_node()
node_data_dict = data.to_dict()
all_nodes_list = []

for each_node in node_data_dict["items"][0]["status"]["addresses"]:
    if "." in each_node["address"]:
        all_nodes_list.append(each_node["address"])

with open('authorised_keys_duplicate', 'r') as keys:
    data_keys = keys.read()


for each_node in all_nodes_list:
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # windows
    client.connect(each_node, username="docker", key_filename="minikube/new_id_rsa.key")
    stdin, stdout, stderr = client.exec_command(f'echo "{data_keys}" > .ssh/authorized_keys')
    print("stdout")
    print(stdout.read())
    print("stderr")
    print(stderr.read())

#assignment : try to put the above code with standards


# data = str(data).replace("\'", "\"")
# print(data)
# k8_data_json = json.loads(str(data))
# print(k8_data_json)

