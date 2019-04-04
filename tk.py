#!/usr/bin/python3
# -*- coding: shift_jis -*-
import tkinter as tk
import sys
from tkinter import messagebox

root = tk.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#ラベル
Static1 = tk.Label(text=u'text', foreground='#ff0000', background='#ffaacc')
Static1.place(x=150, y=228)
#Static1.pack()

#Entry改行のできない1行入力ボックス
Editbox = tk.Entry(width=50)
Editbox.insert(tk.END, "挿入する文字列")
#Editbox.pack()
Editbox.place(x=5, y=10)

#エントリーの中身を削除
#Editbox.delete(0, tk.END)

value = Editbox.get()

#ボタンを押したときのアクション
def DeleteEntryValue(event):
    #エントリーの中身を削除
    Editbox.delete(0, tk.END)



#ボタン
Button = tk.Button(text=u'リセットボタン',width=50)
#左クリック(<Button-1>)されるとDeleteEntryValue関数を呼び出すようにバインド
Button.bind("<Button-1>",DeleteEntryValue)
#Button.pack()
Button.place(x=5, y=40)

#checkbox
#Checkboxがチェックされているかを取得
def check(event):
    global Val1
    global Val2
    global Val3

    text = ""

    if Val1.get() == True:
        text += "項目1はチェックされています\n"
    else :
        text +="項目1はチェックされていません\n"

    if Val2.get() == True:
        text += "項目2はチェックされています\n"
    else :
        text +="項目2はチェックされていません\n"

    if Val3.get() == True:
        text += "項目3はチェックされています\n"
    else :
        text +="項目3はチェックされていません\n"

    messagebox.showinfo('info',text)

#checkboxの初期値
Val1=tk.BooleanVar()
Val2=tk.BooleanVar()
Val3=tk.BooleanVar()

Val1.set(False)
Val2.set(True)
Val3.set(False)

Checkbox1 = tk.Checkbutton(text=u"項目1", variable=Val1)
#Checkbox.pack()
Checkbox1.place(x=5, y=90)

Checkbox2 = tk.Checkbutton(text=u"項目2", variable=Val2)
Checkbox2.place(x=5, y=110)

Checkbox3 = tk.Checkbutton(text=u"項目3", variable=Val3)
Checkbox3.place(x=5, y=130)

button1 = tk.Button(root, text=u'チェックの取得',width=30)
button1.bind("<Button-1>",check)
button1.place(x=5, y=150)

root.mainloop()
