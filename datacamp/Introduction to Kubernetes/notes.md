# Introduction to Kubernetes at Datacamp

- [Kubernetes](kubernetes.png)

## Modern Software Architecture, Containerization, and Kubernetes

### Modern Software Architecture

- Tradioinal architecture: monoliths
  - Single applications, typically run independent from other applications.
    - Hard to maintain and to update
- Modern architecture: constructed from independent building blocks: microservices
  - Can be independently maintained and updated
  - Ideally suited for cloud computing

- [Traditional vs Modern Architecture](traditional_vs_modern.png)

### Containerization and Kubernetes

- Modern applications consist of potentially thousands building blocks
- Deployed via containers
  - Each building block is delivered in an individual container.
- Kubernetes keeps track of all containers

### Cloud Nativeness and Kubernetes

- Cloud-native: a way to build & deploy applications in the cloud.
- Cloud-native applications are designed to be scalable
- Kubernetes is cloud-native:
  - Simplifies deploying and managing containers
  - Enables easy scaling of applications

### Kubernetes Distributions and Cloud Offerings

- Kubernetes is an open-source project by Google
- We can also use Kubernetes with all cloud providers as a managed service.
- Kubernetes known as K8s.

- kubectl or kubectl help: let you see the available commands and their descriptions.

## Docker and Kubernetes

### Container Orchestration Tools

- Modern software stacks typically consist of potentially thousands of individual containers.
- Managing all these containers is known as Container Orchestration, several container orchestration tools are available.
  - Kubernetes
  - Docker Swarm
  - Docker Compose
  - Apache Mesos
  - HashiCorp Nomad
- Kubernetes can be used in cloud environments as well as on-premises. Also, hybrid environments are possible.

### Kubernetes for Orchestration

- Kubernetes solves the typical challenges of container orchestration:
  - Scheduling and networking (where to deploy a container and how to connect them)
  - How to attach storage to a container
- To do that, Kubernetes interacts with Container Engines.

### Relationship between Kubernetes and Docker

- Often, Docker is your container engine.
- Kubernetes interacts with Docker as a container engine to schedule and maintain containers.
- Docker is typically used for two tasks:
  - Creating and updating Docker images
  - Starting containers from such images
- Kubernetes never creates Docker images. Kubernetes orchestrates containers.

### Kubernetes Manifests

- Manifests are YAML files that describe which objects you want, how they should be configured, where they should be scheduled, and a lot more. Kubernetes objects (e.g., containers) are defined in these manifests.
- The kubectl command is used to apply these manifests to a Kubernetes cluster.
- Manifests are declaritve. You describe what you want, or which state to achieve.
- They are not imperative, you don't describe how to achieve that state.

### kubectl

- kubectl is the command-line tool for interacting with Kubernetes clusters.
- kubectl reads your Manifests, sends them to Kubernetes via its API, and Kubernetes will compute what to do to achieve the desired state.

## Kubernetes Architecture

### Kubernetes Overview

- Kubernetes is built from many elements:
  - Most important ones, from larger to smaller:
    - Clusters and Control Planes
    - Nodes
    - Pods
  - Network connectivity through Services

### Kubernetes Cluster and the Control Plane

- A Kubernetes cluster is a set of connected computers (or Nodes)
- Servers in a datacenter, virtual machines in the cloud, or even your local machine.
- The Kubernetes Control Plane manages these nodes
  - Consists of many components, that can run on any node in the cluster.

### Kubernetes Nodes

- A Kubernetes Node typically runs Linux + Container Engine (e.g., Docker)
- Nodes are also called Worker Machines.
- Nodes run Kubernetes Kubelet
  - Ensures that containers are running in a Pod.

### Kubernetes Pods

- Kubernetes Pods are the smallest deployable unit in Kubernetes.
- A Pod can contain one or more containers.
- The containers in a Pod belong together logically. Share storage and network.
- Pods are ephemeral. They can be stopped and recreated at any time.
- Pods can moved to other nodes at any time.
- This gives Kubernetes flexibility to manage resources and handle incidents efficiently.

### Kubernetes Services

- Kubernetes Services: resource for exposing networking connectivity.
- Required to connect to Pod from outside, or to connect Pods to each other.
- Reason: Pod may get re-deployed any time, and will
  - Receive a new IP address
- Services are not ephemeral. They offer stable network connectivity.

### Kubernetes Cheat Sheet

- Kubernetes Cluster: Set of connected computers (Nodes) configured to run Kubernetes.
- Kubernetes Control Plane: Manages the Nodes in a Cluster.
- Kubernetes Nodes: Also called "Worker Machines", running Linux and a Container Engine.
- Kubernetes Pods: Smallest deployable unit in Kubernetes, containing one or more containers.
- Kubernetes Services: Resource for exposing networking connectivity, required to connect to Pods from outside, and for communication between Pods.

## Deploying a First (Stateless) Application

### More on kubectl

- kubectl: main command to interact with Kubernetes objects.
- Objects are e.g., pod, service, etc.
- Typical usage patterns:
  - kubectl create -f "filename.yaml": create new objects, with -f for "filename".
  - kubectl apply -f "filename.yaml": create new objects and change the state of objects.
  - kubectl get "object": overview about objects deployed on Kubernetes.
  - kubectl describe "object": detailed information about an object.
  - kubectl delete "object": delete an object.
- Detailed help is available via kubectl help.

### More on Manifests

- Manifests are declarative.
- Typically YAML, but JSON is also possible.
- Two important sections:
  - metadata: essential information about the object or resource.
  - spec: defines the specifications, or desired state, of the object or resource.
- Sections can be quite deep, depending on the resource to be deployed.

### Stateless Applications

- Stateless apps:
  - General concept
  - Not specific to Kubernetes.
  - Do not save an internal state, or context of processed data.
- When interrupted, a new replica of the stateless app is recreated and starts operating.
- Examples:
  - The database frontend queries a database backend.
  - A search app queries a full text index.
  - A data stream app that converts temperature readings from an IoT sensor from Fahrenheit to Celsius.

### Kubernetes Deployment

- Stateless applications are typically deployed as Kubernetes Deployments.
- A sample Manifest consists of:
  - apiVersion: defines the K8s API and version. For Deployments, it is apps/v1.
  - kind: indicates that we will create a K8s Deployment.
  - metadata: defines various meta information.
  - spec: defines specifications for the Deployment.
    - replicas: number of Pods to run.
    - selector: how pods will be managed.
    - template: defines how new pods are created. Details for the cretion of new Pods in the Deployment.
      - If K8s decides to create a new Pod, it will use this template.
      - It uses the defined template to add 'labels', create 'containers', with respective 'name', docker 'image', and other details like network 'ports' for communication.
- Example Deployment Manifest: [Deployment Manifest](deployment_manifest_example.png)

### Deploying Stateless to a Kubernetes Cluster

- kubectl apply -f "filename.yaml": for creating pods and applying changes.
- Kubernetes Control Plane will schedule the Deployment on Nodes.
  - Then, Pods created is triggered on the Nodes.
- Pods get a unique, but random (unpredictable) identifier, each Pod is "as good as any other".
- kubectl delete -f "filename.yaml": for deleting pods and applying changes.
- kubectl get pods: to get an overview of the Pods running in the cluster.
- kubectl describe pod "podname": to get detailed information about a Pod.

## Scaling and Monitoring an Application

### Scaling on Kubernetes

- Scaling is a technique to add (scale up) or remove (scale down) resources to meet demand.
  - Scale up: react to increased demand.
  - Scale down: save resources when demand decreases.
- Scaling the number of Pods is easy:
  - Either change the number of replicas in the Deployment Manifest and re-apply it.
  - or use the kubectl scale command.
        Example: kubectl scale deployment "deployment-name" --replicas "number"

### Scalability and Cloud Nativeness

- An application needs to be designed for scalability.
- Legacy applications, in particular monoliths, are typically not scalable.
- Modern, cloud native applications are designed with the goal to be easily scalable.

### Monitoring an Application

- Monitoring is essential to ensure that an application is running as expected.
- Observing applications in real-time.
  - Enables reaction to all kind of problems.
- Examples of monitoring tools:
  - Prometheus
  - Grafana
  - Kibana
  - ElasticSearch
  - kubectl
- kubectl for basic monitoring:
  - kubectl get pods: list all Pods.
  - kubectl get services: list all Services.
  - kubectl describe pod "pod-name": detailed information about a Pod.

## Deploying, Scaling, and Monitoring a Stateful Application

### Recap Stateless Applications

- Short recap: stateles applications map to "Deployments" in Kubernetes.
- Used when each Pod of the applications has exactly the same tasks.
- Stateful applications need Pods that belong together in set, but may work on different tasks and different data.
- Much of what we have learned about Deployments can be applied to StatefulSets as well.

### Stateful Applications

- Stateful apps:
  - General concept
  - Fit well to Kubernetes.
  - Save some state.
- When interrupted, a new replica (Pod) can be read the saved state and continue operating from this state.
- Examples:
  - A database backend (e.g., MySQL, PostgreSQL) delivers data to a frontend using 3 Pods.
  - Each time we update data using any of the Pods, that data needs to be persisted.
  - When a Pod terminates, a new one is created and needs to pick up the saved state.

### Kubernetes StatefulSets

- Stateful applications are typically deployed as Kubernetes StatefulSets.
- A sample Manifest consists of:
  - apiVersion: defines the K8s API and version. For StatefulSets, it is apps/v1.
  - kind: indicates that we will create a K8s StatefulSet.
  - metadata: defines various meta information.
  - spec: defines specifications for the StatefulSet.
    - replicas: number of Pods to run.
    - selector: how Pods will be managed.
    - template: defines how new Pods are created. Details for the creation of new Pods in the StatefulSet.
      - If K8s decides to create a new Pod, it will use this template.
      - It uses the defined template to add 'labels', create 'containers', with respective 'name', docker 'image', and other details like network 'ports' for communication.
- Example StatefulSet Manifest: [StatefulSet Manifest](stateful_manifest_example.png)

### Deploying StatefulSets to a Kubernetes Cluster

- StatefulSets are deployed in the same way as Deployments. kubeclt apply -f "filename.yaml"
- Once deployed, a StatefulSet is created different than a Deployment:
  - Pods are created one after the other, not all at once.
  - Pods get predictable names, e.g., pod-0, pod-1, pod-2, etc.
- This means: in contrast to the Pods of a Deployment, the Pods of a StatefulSet have an identity, and a state.

### Scaling A StatefulSet

- Like Deplotments, StatefulSets can be scaled up or down.
  - Either change the number of replicas in the StatefulSet Manifest and re-apply it.
  - or use the kubectl scale command.
        Example: kubectl scale statefulset "statefulset-name" --replicas "number"
- When scaling up, new Pods are created one after the other.
  - Each Pod gets a predictable name, e.g., pod-3, pod-4, pod-5, etc.
- When scaling down, Pods are terminated one after the other.
  - The Pods with the highest number are terminated first.

### Monitoring A StatefulSet

- Like in the case of Deployments, monitoring is essential for StatefulSets. Monitoring enables reactions to all kinds of problems like outages, load spikes, or missing storage.
- Here, we use kubectl to monitor the StatefulSet:
  - kubectl get pods: list all Pods.
  - kubectl get services: list all Services.
  - kubectl get statefulsets: list all StatefulSets.
  - kubectl describe statefulset "statefulset-name": detailed information about a StatefulSet.

## Deploying, Scaling, and Monitoring a Kubernetes Storage

### Persistent Volumes and Persistent Volume Claims

- Fundamental Objects for storage: Persistent Volumes (PV), maintained in parallel to Pods.
- PVs are mapped to Pods using Persistent Volume Claims (PVC).
- A mapped PV allows data persistence when the Pod is stopped, killed, or restarted.
- PVs enable the seperation of storage and compute.

### Storage Classes

- PVs: provisioned either
  - manually by an Kubernetes admin
  - dynamically by regular user.
- Dynamic provisioning happens via Storage Classes (SC) without human intervention. Storage provisioning is a key enabler for automation.
- Storage Classes (SC):
  - Defined by the Kubernetes admin.
  - Different types (different latency, e.g., SDD vs HDD, different backup strategies, etc.)
- If in doubt, use the default Storage Classes.

### Putting It All Together

- There are only three objects that make storage work in Kubernetes:
  - PersistentVolume (PV)
  - PersistentVolumeClaim (PVC)
  - StorageClass (SC)
- A Pod with demand for persisted data uses a PersistentVolumeClaim.
- This PVC has Kubernetes create a PersistentVolume for the Pod.
- This PV is mapped to the claiming Pod.
- A named StorageClass is used, which defines details like latency and backup strategy of the PV.
- This PersistentVolume survives (together with stored data), even when the Pod is terminated.

### Manifest Snippets

- Pod with PersistentVolume: [Pod with PV](pod_pv.png)
- PersistentVolumeClaim with StorageClass: [PVC with SC](pvc_sc.png)

### kubectl Commands for Storage

- kubectl offers a complete set of commands to create and monitor Kubernetes Storage:
  - kubectl get sc: list all available Storage Classes.
  - kubectl get pv: list all deployed Persistent Volumes.
  - kubectl get pvc: list all deployed Persistent Volume Claims.
  - kubectl apply -f "filename.yaml": can be used to deploy storage resources that are declared in Manifests.
  - kubectl delete -f "filename.yaml": can be used to delete storage resources that are declared in Manifests.
  - kubectl describe pv "pv-name": provides detailed information about a Persistent Volume.
  - kubectl describe pvc "pvc-name": provides detailed information about a Persistent Volume Claim.

- kubectl commands in a specific namespace:
  - kubectl get pvc -n "namespace": list all deployed Persistent Volume Claims in a specific namespace.
  - kubectl get pv -n "namespace": list all deployed Persistent Volumes in a specific namespace.
  - kubectl describe pv "pv-name" -n "namespace": provides detailed information about a Persistent Volume in a specific namespace.
  - kubectl describe pvc "pvc-name" -n "namespace": provides detailed information about a Persistent Volume Claim in a specific namespace.
  - kubectl get sc -n "namespace": list all available Storage Classes in a specific namespace.
  - kubectl apply -f "filename.yaml" -n "namespace": can be used to deploy storage resources that are declared in Manifests in a specific namespace.
  - kubectl delete -f "filename.yaml" -n "namespace": can be used to delete storage resources that are declared in Manifests in a specific namespace.
  - kubectl get pods -n "namespace": list all Pods in a specific namespace.

## Networking, Load Balancing, and Security

### More on Labels and Selectors

- Labels:
  - Key/Value pairs attached to Kubernetes objects like Pods or Nodes.
  - Can be used to organize subsets of objects.
  - Can be modified at any time.
  - Examples:
    - environment: prod
    - app: my_cool_app
    - has_GPU: true
- Selectors:
  - Can be used to identify objects with specific labels.
  - Examples:

        ```yml
        selector:
            environment: prod
            app: my_cool_app
        ```

        ```yml
        selector:
            has_GPU: true
        ```

### Networking and Services

- Each Pod gets its own cluster-wide IP address. (internet address)
- Can be used for communication between Pods.
- Not very useful, as Pods can restart at any time, and will get a new IP address.
- Services are used to attach Pods to, and offer stable connectivity.

### Service Manifests

- A Service Manifest consists of:
  - apiVersion: defines the K8s API and version. For Services, it is v1.
  - kind: indicates that we will create a K8s Service.
  - metadata: defines various meta information.
  - spec: defines specifications for the Service.
    - selector: how Pods will be managed.
    - ports: defines the network ports for communication.
    - type: defines the type of the Service.
- Example Service Manifest: [Service Manifest](service_manifest_example.png)

### Load Balancing

- A load balancer in Kubernetes distributes load over Pods.
- Avoids uneven load on resources, increases efficiency and lowers response times.
- Example:
  - Providing a service from multiple Pods.
  - Load balancer will distribute load evenly to Pods.

### Load Balancing in Kubernetes

- Load balancers are typically pre-configured by Kubernetes Provider (Cloud Provider)
- No need to declare additional manifests for a load balancer - will automatically be created and attached to the service.
- [Load Balancer Example](load_balancing_example.png)

### Ingress

- Ingress objects are used to route HTTP and HTTPS requests (Traffic) from outside the cluster to Services inside the cluster.
- Ingress rules define which requests are served by which service.
- Typically used in combination with load balancing.

### Kubernetes Security

- Security in modern IT architectures is an extremely important, but complex field with many facets.
- Kubernetes has all necessary components to secure applications running on it, e.g:
  - the "Secret" API for confidential objects like passwords, tokens, keys etc.
  - tools and APIs to enable encrypted network communication.
  - methods for authentication of users.
  - role-based and attribute-based access control ("RBAC" and "ABAC").

### Workflow of Pods and Services

- Declare the Pods to be attached to your Service. Don't forget to define appropriate labels to be attached to the Pods.
- Deploy the Pods.
- Declare the Service. Don't forget to define a Selector to "select by label" the Pods to be attached to the Service.
- Deploy the Service.

## Data Pipelines on Kubernetes

### What are Data Pipelines?

- Set of processes to move, transform, or analyze data.
- Typical steps:
  - ETL: Extract data from various data sources, then Transform into a meaningful schema, finally Load into a target data sink (e.g., a data warehouse)
  - ELT: Extract data from various data sources, then Load into a target data sink (e.g., a data lake), finally Transform data into meaningful schema when needed.
  - [ETL vs ELT](etl_elt_examples.png)

### Data Pipeline on Kubernetes

- The steps of a data pipeline map nicely to Kubernetes objects:
  - Extract, Transform, Load steps: Pods (Deployment or StatefulSet)
  - Extracted and Transformaed Data: Persistent Volumes
- Kubernetes can scale out Deployments and Storage as required, hence increase throughput.
- [Example of Data Pipeline](data_pipeline_example.png)

### Open-Source Tools for Data Pipelines

- Many open-source software exists that is readily deployable on Kubernetes
- Some examples:
  - Extract: Apache NiFi, Apache Kafka with Kafka Connect
  - Transform: Apache Spark, Apache Kafka, PostgreSQL
  - Load: Apache Spark, Apache Kafka with KSQL, PostgreSQL
  - Storage on top of PVs: Minio, Ceph

## MLOps on Kubernetes

### What is MLOps?

- A paradigm to deploy and maintain machine learning models in production.
- A set of best-practice workflows with focus on continuous development of such models
- Inspired by DevOps:
  - Machine learning models are developed and tested in isolated experimental systems, and then deployed to production systems.
  - When in production, continuous monitoring; retraning may be triggered.
- Data scientists, data engineers, and IT teams can work on deployed models synchronously and ensure model accuracy.

### Implementing MLOps on Kubernetes

- The MLOps paradigm maps very well to Kubernetes:
  - Isolated experimental systems: can be realized via Pods and Kubernetes Storage.
  - Monitoring production ML models: enabled via lifecycle of Pods (and deployed image versions)
  - Synchronous work on model accuracy: built in from the very beginning by Kubernetes architecture.
- Several frameworks for MLOps exist; the two best-known open-source solutions are
  - mlflow
  - kubeflow

### Kubeflow - An Overview

- Kubeflow allows simple deployments of ML workflows specifically on Kubernetes.
- Covers each step of the ML model lifecycle
- Consists of several components which cover these steps, working independently
- Python can be used to develop and deploy ML models via an API
  - no need to use kubectl
