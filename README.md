# A LLM personal playground

This repository is a set of studies around LLM by applying the LLM reference architecture as defined by [A16Z](https://a16z.com/emerging-architectures-for-llm-applications/). The content is also linked to this [generic study notes](https://jbcodeforce.github.io/ML-studies/ml/generative-ai/) and [AWS Bedrock summary](https://jbcodeforce.github.io/aws-studies/ai-ml/bedrock/).
 
## Architecture

Review the reference architecture of an LLM based solution [in this article](https://jbcodeforce.github.io/ML-studies/ml/generative-ai/#reference-architecture-for-llm-solution), it is illustrated in the figure below as it represents the foundation for any AI / LLM app:

![](./docs/diagrams/llm-ra-1.drawio.png)


This repository includes different demonstrations, on how to use this reference architecture for different solutions.

## Python env in docker for development

To avoid impacting with your own python environment, specially with Mac computer, this repository includes a Dockerfile to build a python development environment with all the needed libraries. A virtual env will have done the same but will have used more disk space.

```sh
docker build -t jbcodeforce/python .
```

The `./startPythonDocker.sh` will mount the root folder of the repository to the `/app` folder within the container. A exec inside the container will help us test the code.

```sh
docker exec -ti pythonenv bash
```

## Consulting organization Knowledge Management solution

The business context is illustrated in the following diagram. The fake company has professional staff delivering custom business solution around the company's core products. 

![](./docs/diagrams/sa-tools/biz-context.drawio.png)

The details are in [this file](./sa-tools/README.md)


## A removing noise solution

Some automated monitoring application can generate a lot of events, that could overflow a human, responsible for platform monitoring. This is not a new problem, and alarm filtering and correlation applications, based on inference engines, were used a lot at the end of 90s when network equipments where deployed worldwide.

See the details of this project [here](./ta-afc-llm/README.md)
