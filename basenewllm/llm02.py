# region LLMChain

# from langchain_community.chat_models.ollama import ChatOllama
# from langchain_core.prompts import PromptTemplate
# from langchain.chains import LLMChain

# # 將模型初始化出來
# llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")

# template ="""
# You are a pro gamer. Let's work this out in a step by step way to be sure we have the right answer.
# Question: {question}
# """

# prompt_template=PromptTemplate.from_template(template)

# llm_chain = LLMChain(llm=llm,prompt=prompt_template,verbose=True)

# response = llm_chain.run({"question":"Who is Malenia？"})
# print(response)

#endregion LLMChain


#region SequentialChain
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_community.chat_models.ollama import ChatOllama


# 將模型初始化出來
llm = ChatOllama(base_url="http://192.168.40.210:11434", model="mistral")

template_1=PromptTemplate.from_template("Who is {AKA} in Elden Ring?")
template_2=PromptTemplate.from_template("Give me some facts about {Name}")

llm_chain_1=LLMChain(llm=llm,prompt=template_1,output_key="Name")
llm_chain_2=LLMChain(llm=llm,prompt=template_2,output_key="Ans")

sequential_chain=SequentialChain(
    chains=[llm_chain_1,llm_chain_2],
    input_variables=["AKA"],
    output_variables=["Name","Ans"],
    verbose=True
)
# 測試 SequentialChain
result=sequential_chain({"AKA":"Godfrey"})
print(result["Name"]) # 第一個 Chain 的輸出
print(result["Ans"])  # 第二個 Chain 的輸出
#endregion SequentialChain

