# access token in API in code -> https://github.com/kubernetes-client/python/blob/master/examples/dynamic-client/service.py

from kubernetes import config, dynamic
from kubernetes.client import api_client
from kubernetes.dynamic.exceptions import DynamicApiError

import base64
import boto3
import re
from botocore.signers import RequestSigner


def get_bearer_token(cluster_id, region):
    STS_TOKEN_EXPIRES_IN = 60
    session = boto3.session.Session()

    client = session.client('sts', region_name=region)
    service_id = client.meta.service_model.service_id

    signer = RequestSigner(
        service_id,
        region,
        'sts',
        'v4',
        session.get_credentials(),
        session.events
    )

    params = {
        'method': 'GET',
        'url': 'https://sts.{}.amazonaws.com/?Action=GetCallerIdentity&Version=2011-06-15'.format(region),
        'body': {},
        'headers': {
            'x-k8s-aws-id': cluster_id
        },
        'context': {}
    }

    signed_url = signer.generate_presigned_url(
        params,
        region_name=region,
        expires_in=STS_TOKEN_EXPIRES_IN,
        operation_name=''
    )

    base64_url = base64.urlsafe_b64encode(signed_url.encode('utf-8')).decode('utf-8')

    # remove any base64 encoding padding:
    return 'k8s-aws-v1.' + re.sub(r'=*', '', base64_url)


# def list_services_in_namespace_OUTER_CLUSTER(namespace: str, label_selector: str) -> None:
#     # config.load_incluster_config()
#     config.load_kube_config()
#
#     # Creating a dynamic client
#     clt = dynamic.DynamicClient(
#         api_client.ApiClient(
#         )
#     )
#
#     # OUTER CLUSTER Auth header
#     headers = {'Authorization': 'Bearer ' + get_bearer_token('my_cluster', 'us-east-1')}
#
#     # fetching the service api
#     api = clt.resources.get(api_version="v1", kind="Service")
#
#     # Listing service given namespace and label_selector
#     try:
#         services = api.get(namespace=namespace, label_selector=label_selector)
#         for service in services.items:
#             print(f"Service Name: {service.metadata.name}")
#     except DynamicApiError as e:
#         print(f"An error occurred: {e}")


def local_list_services_in_namespace(namespace: str, label_selector: str) -> None:
    config.load_kube_config()

    # Creating a dynamic client
    clt = dynamic.DynamicClient(
        api_client.ApiClient(
        )
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


# def in_cluster_list_services_in_namespace(namespace: str, label_selector: str) -> None:
#     config.load_incluster_config()
#     # config.load_kube_config() ~/kube/.config
#
#     # Creating a dynamic client
#     clt = dynamic.DynamicClient(
#         api_client.ApiClient(
#         )
#     )
#
#     # fetching the service api
#     api = clt.resources.get(api_version="v1", kind="Service")
#
#     # Listing service given namespace and label_selector
#     try:
#         services = api.get(namespace=namespace, label_selector=label_selector)
#         for service in services.items:
#             print(f"Service Name: {service.metadata.name}")
#     except DynamicApiError as e:
#         print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     ns = "cortex-dev"
#     ls = "component_type=kedroservice"
#     # SET SERVICE_HOST_ENV_NAME
#     # SET SERVICE_PORT_ENV_NAME
#     list_services_in_namespace(ns, ls)

if __name__ == "__main__":
    ns = "dev"
    ls = "component_type=kedroservice"
    local_list_services_in_namespace(ns, ls)
