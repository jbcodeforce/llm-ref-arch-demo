from aws_cdk import (
    Stack,
    aws_lambda,
    aws_iam as iam,
    aws_s3 as s3,
    aws_ec2 as ec2,
    Duration,
    aws_apigateway as apigw,
    aws_events as events 
)
import aws_cdk as cdk

from constructs import Construct
from helpers.BaseStack import BaseStack

class SAToolsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create S3 bucket with cdk
        self.asset_bucket = s3.Bucket(self, "S3Bucket",
                block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
                bucket_name=self.config.get("s3_bucket_name"),
                encryption=s3.BucketEncryption.KMS_MANAGED,
                enforce_ssl=True,
                versioned=False,
                event_bridge_enabled=True,
                auto_delete_objects=True,
                removal_policy=cdk.RemovalPolicy.DESTROY)
        #add policy to invoke bedrock model, and read from S3
        invoke_model_policy = iam.Policy(self, "InvokeModelPolicy",
            statements=[
                iam.PolicyStatement(
                    actions=["bedrock:InvokeModel"],
                    resources=[f"arn:aws:bedrock:{self.region}::foundation-model/anthropic.claude-v2"]
                )
            ]
        )

       