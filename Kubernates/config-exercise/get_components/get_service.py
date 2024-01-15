# access token in API in code -> https://github.com/kubernetes-client/python/blob/master/examples/dynamic-client/service.py

from kubernetes import config, dynamic
from kubernetes.client import api_client
from kubernetes.dynamic.exceptions import DynamicApiError


def list_services_in_namespace(namespace: str, label_selector: str) -> None:
    config.load_incluster_config()

    # Creating a dynamic client
    clt = dynamic.DynamicClient(
        api_client.ApiClient()
    )

    # fetching the service api
    api = clt.resources.get(api_version="v1", kind="Service")

    # Listing service given namespace and label_selector
    try:
        services = api.get(namespace=namespace, label_selector=label_selector)
        for service in services.items:
            print(f"Service Name: {service.metadata.name}")
    except DynamicApiError as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    ns = "prod"
    ls = "component_type=kedroservice"
    list_services_in_namespace(ns, ls)