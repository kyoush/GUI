#!/usr/bin/python3
# -*- coding: shift_jis -*-
import tkinter as tk
import sys
from tkinter import messagebox

root = tk.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#���x��
Static1 = tk.Label(text=u'text', foreground='#ff0000', background='#ffaacc')
Static1.place(x=150, y=228)
#Static1.pack()

#Entry���s�̂ł��Ȃ�1�s���̓{�b�N�X
Editbox = tk.Entry(width=50)
Editbox.insert(tk.END, "�}�����镶����")
#Editbox.pack()
Editbox.place(x=5, y=10)

#�G���g���[�̒��g���폜
#Editbox.delete(0, tk.END)

value = Editbox.get()

#�{�^�����������Ƃ��̃A�N�V����
def DeleteEntryValue(event):
    #�G���g���[�̒��g���폜
    Editbox.delete(0, tk.END)



#�{�^��
Button = tk.Button(text=u'���Z�b�g�{�^��',width=50)
#���N���b�N(<Button-1>)������DeleteEntryValue�֐����Ăяo���悤�Ƀo�C���h
Button.bind("<Button-1>",DeleteEntryValue)
#Button.pack()
Button.place(x=5, y=40)

#checkbox
#Checkbox���`�F�b�N����Ă��邩���擾
def check(event):
    global Val1
    global Val2
    global Val3

    text = ""

    if Val1.get() == True:
        text += "����1�̓`�F�b�N����Ă��܂�\n"
    else :
        text +="����1�̓`�F�b�N����Ă��܂���\n"

    if Val2.get() == True:
        text += "����2�̓`�F�b�N����Ă��܂�\n"
    else :
        text +="����2�̓`�F�b�N����Ă��܂���\n"

    if Val3.get() == True:
        text += "����3�̓`�F�b�N����Ă��܂�\n"
    else :
        text +="����3�̓`�F�b�N����Ă��܂���\n"

    messagebox.showinfo('info',text)

#checkbox�̏����l
Val1=tk.BooleanVar()
Val2=tk.BooleanVar()
Val3=tk.BooleanVar()

Val1.set(False)
Val2.set(True)
Val3.set(False)

Checkbox1 = tk.Checkbutton(text=u"����1", variable=Val1)
#Checkbox.pack()
Checkbox1.place(x=5, y=90)

Checkbox2 = tk.Checkbutton(text=u"����2", variable=Val2)
Checkbox2.place(x=5, y=110)

Checkbox3 = tk.Checkbutton(text=u"����3", variable=Val3)
Checkbox3.place(x=5, y=130)

button1 = tk.Button(root, text=u'�`�F�b�N�̎擾',width=30)
button1.bind("<Button-1>",check)
button1.place(x=5, y=150)

root.mainloop()
