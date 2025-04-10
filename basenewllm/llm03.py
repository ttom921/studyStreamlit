#region Zero-Shot React Description
# from langchain.agents import initialize_agent, Tool
# from langchain.agents import AgentType
# from langchain_community.chat_models.ollama import ChatOllama
# import math

# def calculate_sqrt(input_text:str)->str:
#     try:
#         number = float(input_text.strip())
#         result=math.sqrt(number)
#         return f"The square root of {number} is {result}"
#     except ValueError:
#         return "Please provide a valid number."

# def calculate_square(input_text:str)->str:    
#     try:
#         number = float(input_text.strip())
#         result=number**2
#         return f"The square of {number} is {result}."
#     except ValueError:
#         return "Please provide a valid number"
# # 創建tool
# sqrt_tool=Tool(
#     name="SquareRootCalculator",
#     func=calculate_sqrt,
#     description="Calculate the square root of a number."
# )
# square_tool=Tool(
#     name="SquareCalculator",
#     func=calculate_square,
#     description="Calculate the square of a number."
# )
# # 這邊要注意一下，模型在做決策的時候，
# # 是根據tool的**name**以及**description**這兩個屬性，
# # 所以這邊就要將名稱及功能寫清楚。
# # 將模型初始化出來
# llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")


# # AgentExecutor
# agent_executor= initialize_agent(
#     tools=[sqrt_tool,square_tool],# 指定工具
#     llm=llm,
#     agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # AgentType
#     verbose=True
# )
# # AgentExecutor 運行
# question="What is the square root of 25"
# response = agent_executor.run(question)
# print(response)

#endregion Zero-Shot React Description

#region Self-Ask with Search
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_community.chat_models.ollama import ChatOllama
from langchain.agents import load_tools
import math
import os

# # 將模型初始化出來
llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")
search_tool = load_tools(["llm-math","wikipedia"],llm=llm)
# tools = load_tools(["llm-math","wikipedia"], llm=llm)
# 初始化AgentExecutor
agent_executor = initialize_agent(
    tools=search_tool,
    llm=llm,
    agent=AgentType.SELF_ASK_WITH_SEARCH,
    verbose=True
)

# 測試 Agent with 兩個問題
question = "What day is today? Also, what happened on this day in history?"
response = agent_executor.run(question)
print(response)

#endregion Self-Ask with Search