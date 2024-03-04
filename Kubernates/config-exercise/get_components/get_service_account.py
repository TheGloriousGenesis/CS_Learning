# def get_service_account_info():
#     # Path to ServiceAccount token
#     token_path = '/var/run/secrets/kubernetes.io/serviceaccount/token'
#     # Path to ServiceAccount CA certificate
#     ca_cert_path = '/var/run/secrets/kubernetes.io/serviceaccount/ca.crt'
#     # Path to ServiceAccount namespace
#     namespace_path = '/var/run/secrets/kubernetes.io/serviceaccount/namespace'
#
#     # Read the ServiceAccount token
#     with open(token_path, 'r') as token_file:
#         token = token_file.read().strip()
#
#     # Read the ServiceAccount CA certificate
#     with open(ca_cert_path, 'r') as cert_file:
#         ca_cert = cert_file.read().strip()
#
#     # Read the namespace
#     with open(namespace_path, 'r') as ns_file:
#         namespace = ns_file.read().strip()
#
#     return token, ca_cert, namespace


# if __name__ == "__main__":
    # # Usage
    # token, ca_cert, namespace = get_service_account_info()
    # print(f"Token: {token}\nCA Cert: {ca_cert}\nNamespace: {namespace}")