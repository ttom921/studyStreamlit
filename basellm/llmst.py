import streamlit as st
from langchain_community.llms import Ollama


llm = Ollama(base_url="http://192.168.40.210:11434", model="mistral")


def generate_response(text):
    # return llm.invoke(text)
    for r in llm.stream(text):
        yield r


st.title('Ask me Anything')

# with st.form('form'):
#     text=st.text_area('Enter text:','')
#     sumitted= st.form_submit_button('Submit')
#     if sumitted:
#         # st.info(generate_response(text))
#         resp=""
#         for r in generate_response(text):
#             resp+=r
#             st.info(resp)

with st.form('my_form'):
    text=st.text_area('Enter text:','')
    sumitted= st.form_submit_button('Submit')
    if sumitted:
        st.write_stream(generate_response(text))