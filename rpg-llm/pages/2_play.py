import streamlit as st
import ollama 
from typing import Dict, Generator #型別檢查

st.set_page_config(page_title="GPT", page_icon=":game_die:", layout="wide")
# Connect to the remote Ollama server
client = ollama.Client(host='http://192.168.40.210:11434')

def ollama_generator(model_name: str, messages: Dict) -> Generator:
    stream = client.chat(
        model=model_name, messages=messages, stream=True)
    for chunk in stream:
        # print(chunk)
        yield chunk['message']['content'] # 建立Generator

# st.title("Ollama with Streamlit demo") # 網頁標題        
# st.set_page_config(page_title="GPT", page_icon=":game_die:", layout="wide")

st.title("Ollama with Streamlit demo")# 網頁標題  
st.divider()

# 儲存網頁狀態
if "selected_model" not in st.session_state:
    st.session_state.selected_model = ""
if "messages" not in st.session_state:
    st.session_state.messages = []
   
    # print(dir(client))
    # print(client.list().models)
    # 透過st.selectbox建立語言模型選單（電腦內pull過的模型）
modellst=[]
for x in client.list().models:
    # print(x)
    # target = ':'
    # idxstr=x.model.rfind(target)
    # strrange=slice(0,idxstr)
    # print(x.model[slice(0,idxstr)])
    # modellst.append(x.model[slice(0,idxstr)])
    modellst.append(x.model)
    # print(modellst) 
# 透過st.selectbox建立語言模型選單（電腦內pull過的模型）    
st.session_state.selected_model = st.selectbox(
          "Please select the model:", modellst)

# 顯示使用者訊息和儲存語言模型輸出
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How could I help you?"):
    # Add user message to chat history # 儲存使用者訊息
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container # 對話窗
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.write_stream(ollama_generator(
            st.session_state.selected_model, st.session_state.messages))
    # 儲存語言模型輸出        
    st.session_state.messages.append(
        {"role": "assistant", "content": response})        

