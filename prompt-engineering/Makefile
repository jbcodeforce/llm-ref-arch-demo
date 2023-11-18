SHELL := /bin/bash

help:
	@echo 'Make file to build a streamlit app and deploy it on ECS Fargate'
	@echo '---------------------------------------------------------------'
	@echo make local: 'build the docker image and run locally'
	@echo make init-cdk: 'create CDK project'
	@echo make deploy: 'build Fargate app using CDK'

local:
	cd pe && docker-compose up --build app

init-cdk:
	mkdir IaC && cd IaC && \
	cdk init app --language python && python3 -m venv .venv && source .venv/bin/activate \
	&& pip install --upgrade pip && pip install -r requirements.txt \
	&& cp ../ia_c_stack.py ia_c/. \
	&& cdk synth

teardown:
	cd IaC && cdk destroy