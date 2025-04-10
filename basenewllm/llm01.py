

# from langchain_community.chat_models.ollama import ChatOllama

# # 將模型初始化出來
# llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")

# prompt = "I am Malenia, blade of Miqulle."

# response = llm.invoke(prompt)
# print(response)


# import asyncio
# from langchain_community.chat_models.ollama import ChatOllama

# # 將模型初始化出來
# llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")
# prompt = "I am Malenia, blade of Miqulle."

# async def main():
#     async for response in llm.astream(prompt):
#         print(response)

# asyncio.run(main())        


from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.ollama import ChatOllama

# 將模型初始化出來
llm = ChatOllama(base_url="http://192.168.40.210:11434", 
    model="mistral", temperature=0.5,max_token=500)

# 設定 PromptTemplate 模板
template = """System: {system_prompt}

Question: {question}"""

prompt= PromptTemplate.from_template(template)

# 填入 system_prompt 和 question
system_prompt = "YouYou are a pro gamer. Let's work this out in a step by step way to be sure we have the right answer."

question="Who is Malenia? Who is Miqulle?"

full_prompt = prompt.format(system_prompt=system_prompt,question=question)
# 與模型交互
response = llm.invoke(full_prompt)
print(response)
