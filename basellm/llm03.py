
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
# # 加载外部文档

# # 使用WebBaseLoader加载文档
# # 指定要加载的网页URL
# url = "https://www.gutenberg.org/files/1727/1727-h/1727-h.htm"
# # 创建WebBaseLoader实例
# loader=WebBaseLoader(url)

# # 加载文档
# data= loader.load()

# # 打印加载的文档前100个字符，以验证是否成功加载
# print(data[:100])

# 第四部分：文档处理与分割

# # 假设`data`是我们从前面步骤中加载的文档数据
# loader = TextLoader("./about_me.txt",encoding='utf-8')
# # 加载文档
# data= loader.load()
# # 使用RecursiveCharacterTextSplitter对文档进行分割
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
# # 执行分割操作
# all_splits = text_splitter.split_documents(data)
# # 打印分割后的文档片段数量，以及前一个片段的内容，以验证分割是否成功
# # print(f"总共分割出{len(all_splits)}个片段。")
# # print(f"第一个片段的内容为：{all_splits[0]}")

# # # 初始化Ollama
# # llm = Ollama(base_url="http://192.168.40.210:11434", model="mistral")
# # # 使用Ollama进行简单的查询
# # response = llm("why is the sky blue")

# # # 打印查询结果
# # print(response)

# # 第五部分：构建向量数据库与嵌入模型
# # 初始化Ollama嵌入模型
# # 假定Ollama服务已经在本地运行
# oembed = OllamaEmbeddings(base_url="http://192.168.40.210:11434", model="nomic-embed-text")
# # 为文档片段生成向量
# # 假定`all_splits`包含了我们之前分割的文档片段
# # vectors = [oembed.embed_documents(embedding_text) for embedding_text in all_splits]
# # 打印出第一个文档片段的向量，以验证向量生成是否成功
# # print(vectors[0])

# # 构建向量数据库
# # 使用文档片段向量构建ChromaDB向量数据库

# vectorstore = Chroma.from_documents(
#     documents=all_splits,
#     embedding=oembed,
#     persist_directory="db",
#     collection_name="about",
# )



