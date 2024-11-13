import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    print("Hello World")
    
    summary_template = """
      given the information {information} about a person from I want you to create:
      1. a short summary
      2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm
    res = chain.invoke({"information": "Jack is a 25 year old man who lives in New York and works as a software engineer"})
    print(res)