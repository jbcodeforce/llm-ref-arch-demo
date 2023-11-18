'''
Orchestrator for doing some prompt test
'''

from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import RetrievalQA,ConversationalRetrievalChain,LLMChain
from langchain.prompts import PromptTemplate

import json,boto3
import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock

assumeRole = os.environ.get("ROLE_ARN",None)
aws_bedrock_client = bedrock.get_bedrock_client(assumed_role=assumeRole)

'''
return a default set of parameters based on the model's provider selected
'''
def get_inference_parameters(model_id, temperature): 
    #grab the model provider from the first part of the model id
    bedrock_model_provider = model_id.split('.')[0] 
    
    if (bedrock_model_provider == 'anthropic'): #Anthropic model
        return { #anthropic
            "max_tokens_to_sample": 4000,
            "temperature": temperature, 
            "top_k": 250, 
            "top_p": 1, 
            "stop_sequences": ["\n\nHuman:"] 
           }
    
    elif (bedrock_model_provider == 'ai21'): #AI21
        return { #AI21
            "maxTokens": 4000, 
            "temperature": temperature, 
            "topP": 0.5, 
            "stopSequences": [], 
            "countPenalty": {"scale": 0 }, 
            "presencePenalty": {"scale": 0 }, 
            "frequencyPenalty": {"scale": 0 } 
           }
    
    elif (bedrock_model_provider == 'cohere'): #COHERE
        return {
            "max_tokens": 4000,
            "temperature": temperature,
            "p": 0.5,
            "k": 0,
            "stop_sequences": [],
            "return_likelihoods": "NONE"
        }
    
    elif (bedrock_model_provider == 'meta'): #META
        return {
            "temperature": temperature,
            "top_p": 0.9,
            "max_gen_len": 2000 #temp
        }
    
    else: #Amazon
        #For the LangChain Bedrock implementation, these parameters will be added to the 
        #textGenerationConfig item that LangChain creates for us
        return { 
            "maxTokenCount": 4000, 
            "stopSequences": [], 
            "temperature": temperature, 
            "topP": 0.9 
        }


def get_llm(model_id, temperature):
    
    model_kwargs = get_inference_parameters(model_id, temperature)
    
    llm = Bedrock(
        client=aws_bedrock_client,
        model_id=model_id, #set the foundation model
        model_kwargs=model_kwargs) #configure the properties for Claude
    
    return llm


def read_file(file_name):
    with open(file_name, "r") as f:
        text = f.read()
     
    return text


def get_context_list():
    return ["Prompt engineering basics", "Content creation", "Summarization", "Question and answer", "Translation",  "Advanced techniques: Claude"]


def get_context(lab):
    if lab == "Prompt engineering basics":
        return read_file("basic.txt")
    if lab == "Summarization":
        return read_file("summarization_content.txt")
    elif lab == "Question and answer":
        return read_file("qa.txt")
    elif lab == "Content creation":
        return read_file("qa.txt")
    elif lab == "Translation":
        return read_file("qa.txt")
    elif lab == "Advanced techniques: Claude":
        return read_file("summarization_content.txt")


def get_prompt(template, context=None, user_input=None):
    
    prompt_template = PromptTemplate.from_template(template) #this will automatically identify the input variables for the template
    
    if "{context}" not in template:
        prompt = prompt_template.format()
    else:
        prompt = prompt_template.format(context=context) #, user_input=user_input)
    
    #prompt_template = PromptTemplate(
    #    input_variables=["context", "user_input"],
    #    template=template,
    #)
    
    #prompt = prompt_template.format(context=context, user_input=user_input)
    
    return prompt


def get_llama_response(model_id, temperature, prompt):

    llama_payload = json.dumps({ 
    	'prompt': prompt,
        'max_gen_len': 2000,
    	'top_p': 0.9,
    	'temperature': temperature
    })
    
    bedrock_runtime = boto3.client(service_name='bedrock-runtime')
    
    response = bedrock_runtime.invoke_model(
        body=llama_payload, 
        modelId=model_id, 
        accept='application/json', 
        contentType='application/json'
    )
    
    body = response.get('body').read().decode('utf-8')
    response_body = json.loads(body)
    return response_body['generation'].strip()

'''
'''
def get_text_response(model_id, temperature, template, context=None, user_input=None): 
    llm = get_llm(model_id, temperature)
    
    prompt = get_prompt(template, context, user_input)
    
    temp_model_provider = model_id.split('.')[0] #temp meta
    
    if temp_model_provider == "meta":
        response = get_llama_response(model_id, temperature, prompt)
        print("META")
    else:
        response = llm.predict(prompt)

    print(response)
    
    return response