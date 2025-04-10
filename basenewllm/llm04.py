import streamlit as st
from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


#  將模型初始化出來
llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")

template ="""System: You are a pro gamer. Let's work this out in a step by step way to be sure we have the right answer.
Question: {question} 
"""

prompt_template =PromptTemplate.from_template(template)

def chat(input):
    full_prompt=prompt_template.format(question=input)
    response = llm.invoke(full_prompt)
    return response

st.title("llm chat web")

question =st.text_input("請輸入問題:")
if st.button("Send"):
    response=chat(question)
    st.text_area("模型的回答: ", value=response,height=250)


    # Who is Malenia? Who is Miqulle?