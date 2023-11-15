import os,sys

import gradio as gr

from langchain.llms import Bedrock
from langchain.chains import ConversationChain
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock,  print_ww

def  get_chat_response(message,history):
    return "Hello " + message + "!"

if __name__ == "__main__":
    print(sys.path)
    aws_bedrock_client = bedrock.get_bedrock_client()
    llm= Bedrock(
                client=aws_bedrock_client,
                model_id="anthropic.claude-v1"
            )
    chain = ConversationChain(llm=llm)
    demo = gr.ChatInterface(
        get_chat_response,
        chatbot=gr.Chatbot(height=300),
        textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
        retry_btn=None,
        undo_btn="Delete Previous",
        clear_btn="Clear",
        )
    demo.queue().launch(share=False)