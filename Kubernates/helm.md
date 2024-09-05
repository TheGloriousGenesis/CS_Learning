# Helm

Used to manage packages in my kubernetes cluster

## Glossary

Chart - Helm package - contains all the resources necessary to run an application/service in a cluster
(similar to yum npm file)

Repository is the place where charts can be collected and shared

Release - Instance of chart running in cluster
(1 chart can be installed many times into the same cluster)

installed(chart) == Release

Each release has its own release name
each install creates new release even if it uses same chart

Helm interacts with Kubernetes API server (helm 3 later, before it used tiller)

## Implementation

Helm uses Go templates for templating resource files

Uses `values.yaml` file to configure chart before/during installation

Uses `requirements.yaml` file to configure chart dependencies


## To know

- RBAC to restrict access to Helm

- Securing helm releases

## Questions
1. Are we having a chart for each kedro service? Or a chart for each usecase?
2. How to configure chart (as chart uses default options) before installation
3. How are we keeping track of chart versioning (use semantic versioning)
4. Apart from kedroservice/client/configstore are we also templating the traefik/authorisation files

Good for static deployments

templates
- CatalogService 
- KedroClient
- ConfigStore

usecase dir
    values.yaml --> kustomization.yaml
    requirements.yaml /chart.yaml



## 
Each Argo app for environment


App of app

- App check folder

- if checks for app that is argo app

Argo project vs Argo app?


testappname == root == Application == 1 per cluster if one use case in one cluster


- check k8-manifest
  - Argo project

Argo setup 1 - + Cluster


Argo App : Managed / deployed using one or more component in argo project
Argo Project : 


Can we have 1 client for multiple kedro service

3 apps for one cluster
1 namespace per environment


1 traefik --> 3 ingress routes

Use helm for deploying static applications/services

- Can't use helm to deal with dynamic applications:
  - I thought all kedroservices will have the same format regardless if team so why can't we change the chart using chart.yaml (chart metadata)?

Kedroservice template

new usecase
- Chart.yaml (use to parameterize the chart)
- New code for usecase
- Values.yaml (used to parametrize the template)


Single argo cd mapping 

path mapping


## Secret management