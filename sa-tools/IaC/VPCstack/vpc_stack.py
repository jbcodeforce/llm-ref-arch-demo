from aws_cdk import (
    # Duration,
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_logs as logs,
)
from constructs import Construct
import boto3


class VPCstack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.config = kwargs.pop("config", {})
        vpc_name = self.config.get("vpc_name")
        search= self.lookup_vpc(vpc_name)
        if search == None:
            self.vpc = self.create_vpc(construct_id)
        else:
            self.vpc=ec2.Vpc.from_lookup(self, "lookup", vpc_name=vpc_name, is_default=False)
        CfnOutput(self,"VPC", value=self.vpc.vpc_id, export_name="vpc")

        
    def create_vpc(self, vpc_name: str) -> ec2.Vpc:

        vpc = ec2.Vpc(self, vpc_name,
            max_azs=2,
            vpc_name=vpc_name,
            nat_gateways=1,
            ip_addresses=ec2.IpAddresses.cidr(self.config.get("vpc_cidr")),
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=self.config.get("cidr_mask")
                ),
                ec2.SubnetConfiguration(
                    name="private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=self.config.get("cidr_mask")
                )
            ]
        )
        cwLogs = logs.LogGroup(self, '/aws/vpc/flowlogs') 
        vpc.add_flow_log("flowlogs",destination=ec2.FlowLogDestination.to_cloud_watch_logs(cwLogs),
                              traftraffic_type=ec2.FlowLogTrafficType.ALL)
        return vpc
    

    def lookup_vpc(self, vpc_name: str) -> ec2.Vpc:
        client = boto3.client('ec2')
        response = client.describe_vpcs(
                        Filters=[{
                            'Name': 'tag:Name',
                            'Values': [
                                vpc_name
                            ]
                        }]
                    )
        print(response)
        if len(response['Vpcs']) > 0:
            vpc=response['Vpcs'][0]
        else:
            vpc= None
        return vpc
    
       