
# import os, shutil


# import json
# from langchain_community.llms import Ollama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate

# class MyOutputParser(StrOutputParser):
#     def parse(self,text):
#         return text.replace('Assistant: ','')

# output_parser= MyOutputParser()    

# llm = Ollama(base_url="http://192.168.40.210:11434", model="mistral")
# # print(llm.invoke("Hi,how are you today?"))
# prompt=ChatPromptTemplate.from_messages([
#     ("user","{input}"),
# ])

# chain=prompt | llm | output_parser

# input_text=input('>>> ')
# while input_text.lower() != 'bye':
#     print(chain.invoke({
#       'input':input_text
#     }))
#     input_text=input('>>> ')

# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain.chains import create_retrieval_chain
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.llms import Ollama
# from langchain_community.embeddings import OllamaEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_core.documents import Document

# llm = Ollama(base_url="http://192.168.40.210:11434", model="mistral")
# embeddings=OllamaEmbeddings(base_url="http://192.168.40.210:11434",model="mistral")

# docs=[
#     Document(page_content='變身水（Polyjuice Potion）可變成其他人的樣貌。不可拿來變身成動物，也對動物產生不了效果（包括半人半動物的生物），誤用動物毛髮的話，則會變成動物的容貌。'),
#     Document(page_content='吐真劑（Veritaserum）出自《火盃的考驗》，特徵為像水一樣清澈無味，使用者只要加入三滴，就能強迫飲用者說出真相。它是現存最強大的吐實魔藥，在《哈利波特》的虛構世界觀中受英國魔法部嚴格控管。J·K·羅琳表示，吐真劑最適合用在毫無戒心、易受傷害、缺乏自保技能的人身上，有些巫師能使用鎖心術等方式保護自己免受吐真劑影響。'),
#     Document(page_content='福來福喜（Felix Felicix）出自《混血王子》，是一種稀有而且難以調製的金色魔藥，能夠給予飲用者好運。魔藥的效果消失之前，飲用者的所有努力都會成功。假如飲用過量，會導致頭暈、魯莽和危險的過度自信，甚至成為劇毒。'),
# ]


# vectordb = FAISS.from_documents(docs, embeddings)
# retriever=vectordb.as_retriever()

# prompt =ChatPromptTemplate.from_messages([
#      ('system', 'Answer the user\'s questions in Chinese, based on the context provided below:\n\n{context}'),
#      ('user', 'Question: {input}'),
# ])
# document_chain=create_stuff_documents_chain(llm,prompt)

# retrieval_chain=create_retrieval_chain(retriever,document_chain)
# context=[]

# input_text=input('>>> ')
# while input_text.lower() != 'bye':
#     response=retrieval_chain.invoke({
#         'input':input_text,
#         'context':context
#     })    
#     print(response['answer'])
#     context=response['context']
#     input_text=input('>>> ')


from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

llm = Ollama(base_url="http://192.168.40.210:11434", model="mistral")
embeddings=OllamaEmbeddings(base_url="http://192.168.40.210:11434",model="mistral")


vector= FAISS.from_texts(['My name is Tom'],embeddings)
retriever= vector.as_retriever()

prompt=ChatPromptTemplate.from_messages([
    ('system', 'Answer the user\'s questions based on the below context:\n\n{context}'),
    ('user', '{input}'),
])

document_chain= create_stuff_documents_chain(llm,prompt)

prompt = ChatPromptTemplate.from_messages([
    ('system', 'Answer the user\'s questions based on the below context:\n\n{context}'),
    ('user', '{input}'),
])
document_chain = create_stuff_documents_chain(llm, prompt)

prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
])
retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

chat_history = []
input_text = input('>>> ')
while input_text.lower() != 'bye':
    if input_text:
        response = retrieval_chain.invoke({
            'input': input_text,
            'chat_history': chat_history,
        })
        print(response['answer'])
        chat_history.append(HumanMessage(content=input_text))
        chat_history.append(AIMessage(content=response['answer']))
    input_text = input('>>> ')
# prompt=ChatPromptTemplate.from_messages([
#     MessagesPlaceholder(variable_name='chat_history'),
#     ("user","{input}"),
#     ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
# ])
# retriever_chain = create_history_aware_retriever(llm,retriever,prompt)
# retrieval_chain= create_retrieval_chain(retriever_chain,document_chain)

# chat_history=[]
# input_text=input('>>> ')
# while input_text.lower() != 'bye':
#     if input_text:
#         response=retrieval_chain.invoke({
#             'input': input_text,
#             'chat_history': chat_history,
#         })
#         print(response['answer'])
#         chat_history.append(HumanMessage(content=input_text))
#         chat_history.append(AIMessage(content=response['answer']))
#     input_text=input('>>> ')    