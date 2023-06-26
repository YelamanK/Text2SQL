import os
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
import clickhouse_sqlalchemy
import gradio as gr
from sqlalchemy import create_engine, inspect
import openai
from langchain import OpenAI, SQLDatabase, SQLDatabaseChain
from clickhouse_driver import Client
import clickhouse_driver
import datetime

os.environ['OPENAI_API_KEY'] = "Your OpenAI API Key"

destination_user = "default"
destination_password = "oMdI2ED_lhe3V"
destination_port = 8443
destination_host = "c0a85c19p6.us-central1.gcp.clickhouse.cloud"
destination_database = "Text2SQLdummydata"

destination_connection_url = f"clickhouse+http://{destination_user}:{destination_password}@{destination_host}:{destination_port}/{destination_database}?protocol=https"

destination_engine = create_engine(destination_connection_url)

db = SQLDatabase(engine=destination_engine)

llm = OpenAI(temperature=0)
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))


agent_executor = create_sql_agent(
    llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS
)

def text_to_sql(query):
    instruction = " Proceed until you answer the question or say that you don't know, don't ask my permission, explain your thought process. Please think carefully about your answer and analyse it a couple of times before responding. Also - Google Ads means ads on Google platform and Twitter Ads means ads on Twitter platform, etc."
    result = agent_executor.run(query + instruction)
    return result

title = "Text 2 SQL"
description = "Enter your question and click Run to execute the query."

input_text = gr.inputs.Textbox(label="Enter your question")
output_text = gr.outputs.Textbox()

def run_query(query):
    result = text_to_sql(query)
    return result

gr.Interface(fn=run_query, inputs=input_text, outputs=output_text, title=title, description=description).launch(share=True)
destination_engine.dispose()
