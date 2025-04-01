import time

import streamlit as st

import numpy as np
import pandas as pd

st.set_page_config(
    page_title="自定義網頁標題",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://blog.jiatool.com/about/',
        'About': "# 這是什麼網頁？ \n**[IT空間](https://blog.jiatool.com/)** 示範 streamlit 之用網頁"
    }
)

# st.title('我的第一個應用程式')

# st.write("嘗試創建**表格**:")

# df= pd.DataFrame({
#     'first column':[1,2,3,4],
#     'second column':[10,20,30,40]
# })
# df

# chart_data=pd.DataFrame(
#     np.random.randn(20,3),
#     columns=['a','b','c'])

# st.line_chart(chart_data)

# map_data=pd.DataFrame(
#     np.random.randn(100,2)/[50,50]+[22.6,120.4],
#     columns=['lat','lon']
# )
# st.map(map_data)

# if st.button('不要按!'):
#     st.text("不是叫你不要挾了嗎！")

# if st.checkbox('顯示地圖圖表'):
#     map_data=pd.DataFrame(
#     np.random.randn(100,2)/[50,50]+[22.6,120.4],
#     columns=['lat','lon']
#     )
#     st.map(map_data)

option =st.sidebar.selectbox(
    '你喜歡哪種動物?',
    ['狗','貓','鸚鵡','天竺鼠'])    
st.sidebar.text(f"你的答案:{option}")    

# left_column,right_column=st.columns(2)
# left_column.write("這是左邊欄位")
# right_column.write("這是右邊欄位")


expander=st.expander("點擊來展開...")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")

# tab1,tab2=st.tabs(["Cat 介紹","Dog 介紹"])
# with tab1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
# with tab2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)


# bar= st.progress(0)
# for i in range(100):
#     bar.progress(i+1,f'目前進度 {i+1} %')
#     time.sleep(0.05)
# bar.progress(100,'載入完成！')        


# if st.button('儲存',type="primary"):
#     st.toast(':rainbow[你編輯的內容已經保存]',icon='💾')
#     # 或是簡單點，只顯示文字
#     # st.toast('你編輯的內容已經保存')

# st.success('Success!')
# st.info('Info!')
# st.warning('Warning!')
# st.error('Error!', icon='🚨')

# st.balloons()

# st.snow()

# with st.chat_message("user"):#  或者寫 "human" 
#     st.write("Hi 👋，請問你是誰？")

#另一種寫法
# message=st.chat_message("assistant") #或者寫"ai"
# # message=st.chat_message("assistant",avatar="🦖")  # 自訂頭像
# message.write("你好！我是ChatBot 🤖，可以回答各種問題，提供資訊")
# message.write("有什麼我可以幫助你的嗎?")

# st.chat_input("Say something...")

# with st.form(key='my_form'):
#     form_name=st.text_input(label='姓名',placeholder='請輸入姓名')
#     form_gender= st.selectbox('性別',['男','女','其它'])
#     form_birthday=st.date_input("生日")
#     submit_button= st.form_submit_button(label='Submit')

# if submit_button:
#     st.write(f"hello {form_name},性別:{form_gender},生日:{form_birthday}")

# @st.cache_data(ttl=3600,show_spinner="正在加載資料…") # 👈 Add the caching decorator
# def load_data(url):
#     df=pd.read_csv(url)
#     return df
    
# df=load_data("https://raw.githubusercontent.com/plotly/datasets/master/26k-consumer-complaints.csv")    
# st.dataframe(df)

