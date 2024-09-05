
Two machines running ubuntu is needed 

on v1.30

I will be doing tasks during the certification exam

Imperative : Run cli to apply to cluster, you are in command (the worker), great in testing, POC's (Quick). Not recommended in production

Declarative: Apply templates to cluster, you are the manager. 

# Exam

All command line tooling. NO VSCODE

Set VIM settings for ease: https://vi.stackexchange.com/questions/7975/how-can-i-change-the-indent-size
(ensure you set `set expandtab`! this changes tabs to spaces so that the yaml executes correctly)

More vim help: https://gist.github.com/LunarLambda/4c444238fb364509b72cfb891979f1dd

Learn how to install packages in linux: https://askubuntu.com/questions/879877/how-to-know-whether-a-particular-package-is-installed-on-ubuntu

Kubectl quick reference: https://kubernetes.io/docs/reference/kubectl/quick-reference/



# Containers:

- Helps decouple dev ops (runtime environment) from developer code
- Container is not a virtual machine
- Need container runtime : Docker
  
- Software packages --> Images
- Server --> Registry
- An instance of image is a container

# Image:

- File system snapshot

- #chroot -> change process to different directory

# Container runtime
- At runtime, extract images to machine. Launches executable then chroots 

# Event driven architecture 

- Apiserver = register software for events in cluster. Everything goes through kubelet
- Controllers tells kubelets to execute things and kubelet executes things in the pod
- Controllers registers for events from apiserver
- Kubelet acts as agent on pod
- kubeserver verifies input -> put in etcd if successful-> 
- kube scheduler watches for pods being created
- scheduler decides which machine to run a pod on (tells worker node to run the spec). Updates entry in etcd to say what node it stated
- Kubelet watches for node modification. takes spec and talks to container runtime interface (cri) to launch containers, CNI to set up networking, CSI to set up storage!
- Kubelet heartbeats to apiserver (writes entry to database), updates state in etcd
- etcd is the database kubernetes uses to store info regarding your cluster.
- scheduler job picks which machine to run pod on, you tell via spec which one to run on.
- Node == Host == Machine
- Pod is scheduled onto a machine (a pod is one or more containers)

# Pod

- 1 or more containers
- only one IP address per pod
- `kubectl run newpod --image=<IMAGE>`
- minimum requirement: name and repo

# Deployments

- creates replicaSets

# 

Label: Grouping mechanism for selector
Selector: send info to things that have a certain label
Annotation: Can change how controller behaves with pod


# Operator

- Watching based controller
- Query the current state, compare it against the spec and execute code based on how they differ


# Service
- Type: ClusterIP
- Act as load balancer by default
- Can set clusterIP as None: DNS record (headless)


## NodePort

- Can be used to expose stuff outside cluster.

# Advice

- Search up API reference to check what is the template required for things ; https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/

# Dockerfile

Create dockerfile
- entrypoint first, command after can provide both.

build container

verify the image

push to repository


## Container

`kubectl exec -it <Pod-Name> -- /bin/bash`

# Helm

Package manager for kubernetes

# Registry

You can create a registry within the cluster!