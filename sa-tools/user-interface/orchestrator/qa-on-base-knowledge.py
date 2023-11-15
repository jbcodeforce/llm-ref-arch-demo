'''
Orchestrator leveraging existing VectorStore, define a prompt to get some question
answered from a LLM
'''

import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww
from orchestrator.Orchestrator import Orchestrator


if __name__ == "__main__":
   

    query="what is amazon bedrock?"
    orchestrator=Orchestrator()
    response= orchestrator.processHumanQuery(query,"",useVectorStore=False,.2,1)
    print_ww(response)