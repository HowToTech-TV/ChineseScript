import re
import os
import random

def transcribe(content):
  content = re.sub("汇入随机模组","import random", content)
  content = re.sub("汇入视窗元件", "import tkinter", content)
  content = re.sub("另加入对话框模组","from tkinter import messagebox", content)
  content = re.sub("。","",content)
  def replace(match):
    return f'"{match.group(1)}"'
  def replace2(match):
    return f'print("{match.group(1)}")'
  content = re.sub(r'「(.*?)」',replace,content)
  content = re.sub(r'显示"(.*?)"', replace2,content)
  def replace3(match):
    return f'print({match.group(1)})'
  content = re.sub("否则","else",content)
  content = re.sub(r'显示(.*)', replace3,content)
  content = re.sub("，","\n",content)
  content = re.sub("小或等同于", "<=", content)
  content = re.sub(r"(\w+)设定为", r"\1=", content)
  content = re.sub(";","\n  ",content)
  content = re.sub("字串化","str",content)
  content = re.sub("整数化","int",content)
  content = re.sub("浮点化","float",content)
  content = re.sub("序列化","list",content)
  content = re.sub("如果", "if ", content)
  content = re.sub("大或等同于", ">=", content)
  content = re.sub("等于", "==", content)
  content = re.sub("小于", "<", content)
  content = re.sub("大于", ">", content)
  def reprff(match):
    return f"for i in range({match.group(1)}):"
  content = re.sub(r"重复(\d+)次:", reprff, content)
  content = re.sub("无限轮迴:","while True:", content)
  content = re.sub("当", "while", content)
  content = re.sub("停止轮迴", "break", content)
  content = re.sub("定义函式","def ", content)
  def repres(match):
    return f"random.randint({match.group(1)},{match.group(2)})"
  content = re.sub(r"随机整数(\d+)至(\d+)",repres, content)
  content = re.sub("用户輸入","input", content)
  content = re.sub("创建新视窗", "wnd = tkinter.Tk()", content)
  def reprtit(match):
    return f"wnd.title({match.group(1)})"
  content = re.sub(r"视窗标题为(.*)",reprtit, content)
  def reprsize(match):
    return f'wnd.geometry("{match.group(1)}x{match.group(2)}")'
  content = re.sub(r"长(\d+)像素、阔(\d+)像素",reprsize, content)
  def reprlbl(match):
    return f"tkinter.Label(wnd, text={match.group(1)}).pack()"
  content = re.sub(r'在视窗新增文字方塊并展示(.*)', reprlbl, content)
  def reprbtn(match):
    return f"tkinter.Button(wnd, text={match.group(1)}, command={match.group(2)}).pack()"
  content = re.sub(r'在视窗新增按纽并展示(.*)其按后执行命令为(.*)', reprbtn, content)
  content = re.sub("使用全局变量", "global ", content)
  content = re.sub("最后初始化视窗","wnd.mainloop()", content)
  content = re.sub("回传值为", "return ",content)
  def reprerr(match):
    return f"messagebox.showerror({match.group(1)},{match.group(2)})"
  def reprinfo(match):
    return f"messagebox.showinfo({match.group(1)},{match.group(2)})"
  content = re.sub(r"弹出警告对话框(.*)并展示内容(.*)", reprerr, content)
  content = re.sub(r"弹出资讯对话框(.*)并展示内容(.*)", reprinfo, content)
  return content
