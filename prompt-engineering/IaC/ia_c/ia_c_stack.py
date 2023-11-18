from aws_cdk import (
    Stack,
    Duration,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_iam as iam,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct


class IaCStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(
            self, "J9rVPC", 
            max_azs = 2, # default is all AZs in region, 
            )     

        cluster = ecs.Cluster(self, "J9rCluster", vpc=vpc)

        # Build Dockerfile from local folder and push to ECR
        image = ecs.ContainerImage.from_asset('../pe')

        # Use an ecs_patterns recipe to do all the rest!
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(self, "j9rFargateService",
            cluster=cluster,            # Required
            cpu=256,                    # Default is 256
            desired_count=1,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=image, container_port=8501),  # Docker exposes 8501 for streamlit
            memory_limit_mib=512,       # Default is 512
            public_load_balancer=True,  # Default is False
        )  

        fargate_service.task_definition.add_to_task_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions = ["rekognition:*"],
            resources = ["*"],
            )
        )

        # Setup task auto-scaling
        scaling = fargate_service.service.auto_scale_task_count(
            max_capacity=10
        )
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=50,
            scale_in_cooldown=Duration.seconds(60),
            scale_out_cooldown=Duration.seconds(60),
        )