from kubernetes import client, config


config.load_kube_config()


v1 = client.CoreV1Api()
data = v1.list_node()

# sample output is in class29.txt file
# assignment to parse the ip address from data
# #
# # get namespaces
# #
# #
# print(v1.list_namespace())


# #get pods
# # kubectl get pods --all-namespaces
#
# print(v1.list_pod_for_all_namespaces())


containers = []
containers_pod = client.V1Container(name="nginx-deployment", image="nginx")
containers.append(containers_pod)


pod_spec = client.V1PodSpec(containers=containers)
pod_metadata = client.V1ObjectMeta(name="my-pod", namespace="default")

pod_body = client.V1Pod(api_version='v1', kind="Pod", metadata=pod_metadata, spec=pod_spec)

v1.create_namespaced_pod(namespace="default", body=pod_body)



