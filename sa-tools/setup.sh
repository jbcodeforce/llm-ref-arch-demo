echo "Get AWS information"

export ACCOUNT_ID=$(aws sts  get-caller-identity --query Account --output text)
export REGION=$(aws configure get region)
export ECR_PATH=$ACCOUNT_ID".dkr.ecr."$REGION".amazonaws.com"
export APP_NAME=j9r_llm_demo

aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $ECR_PATH
present=$(aws ecr describe-repositories | jq -r '.repositories[].repositoryName' | grep $APP_NAME)
if [ -z "$present" ]
then
    aws ecr create-repository --repository-name $APP_NAME
else
    echo "ECR repository already exists"
fi