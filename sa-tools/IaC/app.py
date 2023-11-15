#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ia_c.sa_tools_stack import SAToolsStack
from VPCstack.vpc_stack import VPCstack
from helpers.helpers import getAppEnv, load_configuration


app = cdk.App()
env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),
app_env = getAppEnv()
config = load_configuration(app_env)

vpc_stack = VPCstack(app, f"{app_env}-vpc",env=env,config=config)
SAToolsStack(app, "SAToolsStack",
   vpc=vpc_stack.vpc,
   config=config,
   env=env
)

app.synth()
