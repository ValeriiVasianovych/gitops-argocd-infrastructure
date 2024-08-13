# GitOps ArgoCD Infrastructure

## Overview

This repository contains a collection of Helm charts and environment setup files for managing and deploying various applications. It is designed to learn GitOps services and tools like ArgoCD, Argo Workflows, Argo Events.

## Repository Structure

The repository is organized into the following directories:

### `env-setup`

This directory contains configuration files for setting up the environment.

- `applications/`: Contains configuration files for different applications.
- `root.yaml`: The root configuration file for setting up the environment.

### `HelmCharts`

This directory contains Helm charts for deploying various tools and services in a Kubernetes cluster.

- `argo-events/`: Helm chart for Argo Events.
- `argo-rollouts/`: Helm chart for Argo Rollouts.
- `argo-workflows/`: Helm chart for Argo Workflows.
- `crossplane/`: Helm chart for Crossplane.
- `elasticsearch/`: Helm chart for Elasticsearch.
- `fluentd/`: Helm chart for Fluentd.
- `grafana/`: Helm chart for Grafana.
- `prometheus/`: Helm chart for Prometheus.

## Getting Started

To get started with this repository, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Set Up the Environment**

   Navigate to the `env-setup` directory and follow the instructions in the `root.yaml` file to set up your environment.

3. **Deploy Applications**

   Use Helm to deploy applications from the `HelmCharts` directory. For example, to install Grafana:

   ```bash
   helm install grafana ./HelmCharts/grafana
   ```

   Replace `grafana` with the appropriate chart name and adjust the path if necessary.

## Configuration

Each Helm chart and application in this repository may have its own configuration options. Refer to the respective Helm chart's `values.yaml` file or documentation for specific configuration details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.