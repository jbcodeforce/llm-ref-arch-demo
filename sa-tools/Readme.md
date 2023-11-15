# Tech Sellers - Solution Architects tools

An application to demonstrate how to use specific documentation to do RAG on top of Anthropic Claude 2, for tech sellers and field solution architects.


## Requirements

### User Story_1: build corpus

As a solution architect I want to upload a document or give a URL to crawl the content to build a new specific corpus.

Which should be supported by:

* A crawler tool to load specific product documentation from a web site
* PDF to S3 using `aws s3 synch ...`
* Use OpenSearch for vector stores
* Use Bedrock embeddings


## Demonstration:

### Pre-requisite

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* In Bedrock enable Anthropic Claude model and Titan Embeddings

### Infrastructure as code

* Under IaC folder, create virtual environment for Python

    ```
    python3 -m venv .venv
    ```

    For a Windows platform, activate the virtualenv like this:

    ```
    .venv\Scripts\activate.bat
    ```

* Install the Python required dependencies: `pip install -r requirements.txt`

* Run the command below to bootstrap your account. CDK needs it to deploy

`cdk bootstrap`

* Review the CloudFormation template the cdk generates for you stack using the following AWS CDK CLI command:

`cdk synth`

* From the command line, use AWS CDK to deploy the AWS resources.

`cdk deploy --guided`

### Document ingestion feature

The corpus documents need to be ingected into Data lake. As an example we will take a pdf document about a AWS Bedrock product documentation, upload to S3 bucket, which should trigger an event, processed by event bridge.

Event Bridge rule will call a ECS task to do the splitting of the document, embeddings the chunk to be persisted in a vector store.

#### To unit test the solution:

* Start to docker compose under `sa_tools` folder, to run a local opensearch database and a python environment.
* docker exec to pythonenv container. and install needed requirements: `pip install -r requirements.txt`
* Be sure to be connected to AWS
* Start the app.py, which takes a simple doc and runs the Bedrock embeddings, and save that in a opensearch collection named ``.

#### Build corpus while the app is deployed to AWS

1. Take a pdf from one of the AWS PDF. Claude was not trained on Bedrock so we can take its documentation: https://docs.aws.amazon.com/pdfs/bedrock/latest/userguide/bedrock-ug.pdf#what-is-bedrock in [data folder]()
1. Upload to S3