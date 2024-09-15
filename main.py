from typing import Text
import streamlit as st
from ChineseScript import transcribe
import subprocess

if "default" not in st.session_state:
    st.session_state["default"] = "显示「你好, 世界！」"
if "fuck" not in st.session_state:
    st.session_state["fuck"] = "你好, 世界!"
if "shit" not in st.session_state:
    st.session_state["shit"] = 'print("你好, 世界!")'
st.set_page_config(
    page_title="中文程式",
    page_icon="🀄️",
)

st.write("# 中文程式语言")

col1, col2 = st.columns(2)

with col1:
    st.write("Python 编译结果")
    body = st.session_state["shit"]
    code = st.code(body, language="python", line_numbers=True)
    st.write("执行结果")
    output = st.code(st.session_state["fuck"], language=None)
with col2:
    txt = st.text_area("程式码", value=st.session_state["default"],height=400)
    title = st.text_input("档案名称", "新文件")
    col3, col4 = st.columns(2)
    col3 = st.download_button(
        label="下载档案",
        data=txt,
        file_name=f"{title}.cscript"
    )
    def on_click():
        global txt
        content = transcribe(txt)
        with open("cache.py", "w") as file:
            file.write(content)
        command = ["python","cache.py"]
        output = subprocess.Popen(command, stdout = subprocess.PIPE).communicate()[0]
        st.session_state["fuck"] = output.decode("utf-8")
        st.session_state["shit"] = content
        
    col4 = st.button("执行程式", on_click=on_click)
    
    
x = st.file_uploader("上传文件", type=["txt"])
if x is not None:
    content = ""
    for line in x:
        content = content + line.decode("utf-8") + "\n"
    st.session_state["default"] = content
        

 

