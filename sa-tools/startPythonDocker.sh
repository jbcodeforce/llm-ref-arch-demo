#!/bin/bash

echo "##########################################################"
echo "Python 3.11.3+ docker image includes spark, keras, boto3, aws cli"
echo
NAME=pythonenv

# give me a test argument
if [ $# -eq 0 ]
then
   TAG=latest
else
    TAG=$1
fi

IMAGE=jbcodeforce/python:$TAG

docker run -e DISPLAY=host.docker.internal:0\
   --name $NAME -v $(pwd):/app/ -v $HOME/.aws:/root/.aws -it \
   --rm -p 5002:5000 -p 8888:8888 -p 8501:8501 \
   $IMAGE /bin/bash 
