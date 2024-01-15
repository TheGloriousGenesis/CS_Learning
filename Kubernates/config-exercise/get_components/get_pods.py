# access token in API in code -> https://github.com/kubernetes-client/python/blob/master/examples/dynamic-client/service.py

from kubernetes import client, config
from kubernetes.client import ApiException


def list_pods_in_namespace(namespace: str) -> None:
    # Load in cluster config (if within pod)
    config.load_incluster_config()

    # Create an instance of the API class
    v1 = client.CoreV1Api()

    # Listing service given namespace and label_selector
    try:
        pods = v1.list_namespaced_pod(namespace)

        for pod in pods.items:
            print(f"Pod Name: {pod.metadata.name}")

    except ApiException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    ns = "prod"
    list_pods_in_namespace(ns)
