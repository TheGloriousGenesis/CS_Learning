Intro into kubernates - https://cloudacademy.com/course/introduction-to-kubernetes/interacting-with-kubernetes/

Setting up own CA for local https development - https://deliciousbrains.com/ssl-certificate-authority-for-local-https-development/
- Need Docker experience
- Need Yaml experience

[glossary of Kubernetes](https://kubernetes.io/docs/reference/glossary/?all=true#term-control-plane)

|      Word       |                                                                                          Definition                                                                                           |
|:---------------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|    Resources    |                                                            Instances of Kubernetes objects (e.g Deployment, services, namespaces)                                                             |
|   Controller    |                                                 Observe the state of the cluster and look for changes to desired state of resources or system                                                 |
|    Workloads    |                                                     Resources that run containers (Deployments, StatefulSets, Jobs, Cronjobs, DaemonSets)                                                     |
| Resource config |                                              Declarative files applied to cluster (with kubectl) and then picked up and actuated by a controller                                              |
|     Context     |                                          Specifies which namespace and cluster and user the kubectl command will use   (1 context to one namespace)                                           |
|   API Server    |                                                                      Control plane component that serves kubernetes API                                                                       |
|     Kubelet     |                      A node agent that runs on every node in the cluster and performs functions such as running containers and managing workloads and executing pod spec                      |
|  ServiceAccont  | Provides identity to pods to authenticate pod to the API server. Not necessarily only pods that use service accounts external application CI/CD if it needs to access cluster or k8 processes |
|     Subject     |                                                                             Any actor that is an object in k8 API                                                                             |
|      RBAC       |                                      Role Based Access Control. Assign policies to service account to define what action they can perform in the cluster                                      |
## Definition

- container orchestration tool designed to automate deploying and scaling applications

- It puts containers on machines within the distributed system based on some preconfiguration (availble resources, time etc)
- Can move containers as machines are added/removed

- Q: What is the benefit of using different container runtimes?

## Benefits

- Multiple cluster can join to create federation
- Seemless horizontal scaling

## Deploying Kubernetes

### Single Node cluster
- Use Docker Desktop
- Useful for CI
- Start quickly for testing

### Multi Node cluster
- Decide if you want it fully managed or fully controlled
- Fully managed e.g Amazon EKS

## Kubernetes Architecture
> [!INFO]
> CREATE INFOGRAPHIC : Cluster > Nodes > Pods > Container, Resources

A control plane is the most important part of a cluster and is responsible for managing the cluster 

- Kubernetes API has 2 parts - Resource Type and controller

- Cluster : all of the machiens collectively
- Nodes: machines in cluster (vm/ machine) [kubernetes ref](https://kubernetes.io/docs/tutorials/kubernetes-basics/explore/explore-intro/)
  - Two types:
    - workers:
      - can have multiple pods [PODS](#pods)
        - inside pods there are 
          - one or many containerised code with your app in it and volumes.
          - volumes are shared storage for that pod
    - masters:
      - control worker nodes via control plane
        - Control plane set of APIs and software that kubernetes users interact with
        - API and software are referred to as master components
- Services: define rules for communication between pods or 
  - Each service exposes sets of endpoints (which are pods) along with a policy about how to make the pod accessible over a network. The pods that are aligned with service usually defined by selector
- Deployments: manage deploying configuration changes to running pods + horizontal scaling

## Interacting with Kubernates
- Send API requests to master components
- either through Client Libraries / API / kubectl


## Pods
- Share container network (all pods connecting)
- Pods can communicate with any other pods in the network regardless of where the pod resides (E.g if its within another node)
- One IP address per Pod
- Declare config of pod in manifest (yml). it should contain info regarding the things it can contain (container image, container ports, restart policy, resource limits)
- When you send the manifest to API server it does something like the following:
  - Determines which resources are available for your pod.
  - Send your pod to the node that has the resources that are available
  - Node pulls container images and starts pod container
- Manifest:
  - spec is  where all the meat go. Must define minimum one container in there
    - Define port to expose container
    - 
  - metadata: how to identify pod with additional data
    - labels to retrieve data
- Pods are scheduled to run on Nodes in a cluster

## Kubelet

Runs on every node in the cluster and performs functions such as running containers and managing workloads.
Its a node agent that ensures containers are run in pods as specified in pod spec.

It communicates with the control plane. It receives pod spec from API server and spins up what is required. also reports back regarding status and what is required

## Resources
- Uniquely identified by the following declarative tags:
  - apiVersion
  - Kind
  - metadata.namespcae
  - metadata.name
- Spec specifies the state of the resource

> [!CRITICAL]
> Not all resources are in namespaces

## Nodes
- Q: Do all nodes share container network too?

## Service

When a service is created it creates a DNS entry which is in the form `<service-name>.<namespace-name>.svc.cluster.local`
which is callable by a container by just the `<service-name>` (as it will resolve to the service which is local to the namespace used by container).

## Ingress
Acts as entrypoint to cluster

## Security

Security concepts in kubernetes - https://kubernetes.io/docs/concepts/security/

## Service Account

Service account exist as objects in the API server and have the following properties:
1. Has one SA to Namespace (1 to 1) (there can be many SA's in a single namespace)
2. Exist in cluster 
3. Can be quickly created for specific tasks

An SA is similar to user account but one a bigger scale. 

|                          User Account                          |              Server Account              |
|:--------------------------------------------------------------:|:----------------------------------------:|
|                      Human authenticated                       |          Computer authenticated          |
| Do not exist in API server (opaque data - external to cluster) | Exist in API server(internal to cluster) |
|                         Used by people                         |       Used by workloads/automation       |

When a pod is created, a default SA is created with all permissions allowed. 
An application running inside a Pod can access kubernetes API using the default mounted SA credentials. 

> [!IMPORTANT]
> Although API credentials are automatically mounting to the pod during creation, you can opt out of this behaviour via the 
> `automountServiceAccountToken: false` setting on a service object and on pod object.

### Why use service account?
- When pods need to communicate with K8 API server
- When pods need to communicate with external services
- When external service needs to communicate with K8 API server

To access kubernetes directly via a REST API with a http client like `curl` or a browser you can use a configured SA.
To access K8 via API you need a token. This token can either be term-lived (mounted onto the pod), or you can generate a token 
using `kubectl create token <name-of-token>` (this is not recommended, mounted tokens are recommended instead).

You can also use an SA to state imagepullsecrets instead of stating imagepullsecrets for each pod that uses a private registry. 

## Role based access control

Good learning resources here -> https://learnk8s.io/rbac-kubernetes 

Kubernetes does not have objects which represent regular user accounts. Any subject that presents a valid certificate signed by the clusters
certificate authority is considered authenticated.

RBAC regulates access to computer or network resources. This is done by the use of API objects **Role** and **ClusterRole**.
These roles contain the permissions on subject in k8 can have.
- A Role always sets permissions within a particular namespace
- A ClusterRole is non-namespace specific, so can grant permissions to cluster scoped resources or multiple namespace access
- Aggregated ClusterRole allows role management to be more dynamic and centralized. Allows grouping of other ClusterRoles to one central place. (instead of giving someone 5 different clusterroles, group them into one clusterrole)

If you want to define a namespace specific role, use Role, else use ClusterRole for cluster wide roles

All roles must be bound by Rolebinding/ClusterRoleBinding object.

Rolebinding grants the permissions defined in a role to a user, service account or Group.

The name of the subject during role binding has no requirements apart from the fact that `system:` prefix is reserved (can be used but has special meaning).

### Token Generation
why you would volumemount token - > https://stackoverflow.com/questions/75292056/how-to-add-mountable-secrets-to-a-service-account

Service Account token is used for API authentication and not for consumption within the Pod itself.

If you want to use the secret within a Pod, you will have to reference it in the Pod's specification. 

Service accounts have tokens that an subject can use for authentication. These tokens are not configurable on the default account. This token from the projected volume is a JSON Web Token.
Tokens for service accounts usually use projected volumes. This allow for specific control over SA token configuration, enhancing security. Project volumes also enable automatic rotation of tokens by the kubelet,
which means tokens aren't static and less issues if compromised.

This token can have an expiration time, which can be specified. The kubelet will manage the generation, storage and refreshing of the token. The refreshing is managed by the K8 cluster configuration (unable to manage this administratively). The application is then responsible for load token on a schedule without tracking expiration.

You don't need to call this to obtain an API token for use within a container, since the kubelet sets this up for you using a projected volume

default audience for tokenrequest is kube-apiserver

project volume contains and exposes the following to application code running within the pod:
1. `serviceaccountToken`
2. `configMap` - stores the certificate authority data information to certify kube-apiserver.
3. `downwardAPI` - makes sure the name of the namespace the pod is in is available to application code running in pod.

## FAQ
Q: I get a connection error when executing a simple command such as `kubectl get pods`, how do i resolve this?

A: This error comes from issues connecting to the API server (master components) might come from the context that kubectl is using. Execute the following commands and ensure that `docker-desktop` context (or whichever you need), is set as default context
```
kubectl config get-contexts

kubectl config use-context docker-desktop
```

Q: What exists in the API server?

Q: What is an API server?

Q: How do you access kubernetes API from within a pod?

A: https://kubernetes.io/docs/tasks/run-application/access-api-from-pod


## Trouble-shooting:

### Check if SA works

1. Get token: 
   1. `TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)` OR
   2. `TOKEN=$(cat /var/run/secrets/tokens/sa-dev-token)` OR
   2. `TOKEN=$(cat <path-to-token>)`
2. Execute command: `curl --cacert /var/run/secrets/kubernetes.io/serviceaccount/ca.crt --header "Authorization: Bearer $TOKEN" https://kubernetes.default.svc/api/v1/namespaces/dev/pods/`

### Check if token has expired in pod
1. Enter pod: `kubectl exec -n <namespace> -it <pod_name> -- bash`
2. Get token: `TOKEN=$(cat /var/run/secrets/tokens/sa-dev-token)`
3. Get payload: `PAYLOAD=$(echo $TOKEN | cut -d '.' -f2 | base64 -d)`
4. Pad payload if necessary: `PADDED_PAYLOAD=$(echo $PAYLOAD | sed -e 's/[^=]\{1\}$/&==/;s/[^=]\{2\}$/&=/')`
5. Decode payload: `DECODED_PAYLOAD=$(echo $PADDED_PAYLOAD | base64 -d)`
6. Download jq for json parsing and get `exp` field (can skip and just look at value from DECODED_PAYLOAD): `apt-get update && apt-get install -y jq`
7. Get current time: `CURRENT_TIME=$(date +%s)`
8. Check if token is still valid:
```bash
if [ $CURRENT_TIME -gt $EXP ]; then
    echo "Token has expired."
else
    echo "Token is still valid."
fi
```

### Validate token using TokenRequest API
1. Ensure you are in the right context `kubectl config current-context`
2. Ensure the token has permissions to create a tokenreview object
3. Check if Kubernetes API server has been configured to authenticate tokens
   1. check the `/etc/kubernetes/manifests/kube-apiserver.yaml` in self managed clusters, EKS service if its aws
   2. look for flags that associated with authentication that start with `--` e.g `--service-account-key-file`: Points to the file containing the key for verifying service account tokens.
   3. Access master cluster logs via `journalctl` 
4. If EKS check:
   1. IAM roles `aws-auth` configmap
   2. IAM roles for kubernetes service accounts can be added to manage AWS service access.

Kubernetes are properly set up and that the tokens they generate are compatible with the API server's configuration.

