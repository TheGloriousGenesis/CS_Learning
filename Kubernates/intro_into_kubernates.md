Intro into kubernates - https://cloudacademy.com/course/introduction-to-kubernetes/interacting-with-kubernetes/

- Need Docker experience
- Need Yaml experience

|      Word       |                                             Definition                                              |
|:---------------:|:---------------------------------------------------------------------------------------------------:|
|    Resources    |               Instances of Kubernetes objects (e.g Deployment, services, namespaces)                |
|   Controller    |    Observe the state of the cluster and look for changes to desired state of resources or system    |
|    Workloads    |        Resources that run containers (Deployments, StatefulSets, Jobs, Cronjobs, DaemonSets)        |
| Resource config | Declarative files applied to cluster (with kubectl) and then picked up and actuated by a controller |


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

## Resources
- Uniquely identified by the following declarative tags:
  - apiVersion
  - Kind
  - metadata.namespcae
  - metadata.name
- Spec specifies the state of the resource

## Nodes
- Q: Do all nodes share container network too?

## Ingress
Acts as entrypoint to cluster

## FAQ
Q: I get a connection error when executing a simple command such as `kubectl get pods`, how do i resolve this?

A: This error comes from issues connecting to the API server (master components) might come from the context that kubectl is using. Execute the following commands and ensure that `docker-desktop` context (or whichever you need), is set as default context
```
kubectl config get-contexts

kubectl config use-context docker-desktop
```
