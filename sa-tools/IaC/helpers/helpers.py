import os,yaml

def getAppEnv():
    appName=os.getenv("APP_NAME","app").lower()
    if not os.path.isfile(f"./config/{appName}.yaml"):
        raise RuntimeError(f"File config/{appName}.yaml not found")
    return appName

def load_configuration(appName: str) -> dict:
    with open(f"./config/{appName}.yaml", 'r') as f:
        vars= yaml.load(f, Loader=yaml.FullLoader)
    return vars
