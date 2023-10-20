import tkinter
from tkinter import *
import keyboard as keyb
import speech_recognition as sr

def transk(a):
    a = a.replace('Запятая', ',')
    a = a.replace('запятая', ',')
    a = a.replace('Точка', '.')
    a = a.replace('точка', '.')
    a = a.replace('Двоеточие', ':')
    a = a.replace('двоеточие', ':')
    a = a.replace('Вопросительный знак', '?')
    a = a.replace('вопросительный знак', '?')
    a = a.replace('Восклицательный знак', '!')
    a = a.replace('восклицательный знак', '!')
    return a

# import pyperclip
# def copy():
# eda = text1.get()
# pyperclip.copy(eda)
# import xerox
# def copy_buf():
# x = text1.get()
# print(x)
# xerox.copy(x)
def copy_buf():
    win.clipboard_clear()
    x = text2.get(1.0,END)
    win.clipboard_append(x)
def speak():
    btn_7.configure(fg='green')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.1)
        data = r.record(source, duration=10)
        text = r.recognize_google(data, language='ru-RU')
        text=transk(text)
        text2.delete(1.0, END)
        text2.insert(1.0, text)
        print(text)

def saiv1():
    x = ent11.get()
    y = ent12.get()
    print(x, y)
    bd[x] = y
    keyb.add_abbreviation(x, y)
    btn_1.configure(fg = 'green')

def saiv2():
    x = ent21.get()
    y = ent22.get()
    print(x, y)
    bd[x] = y
    keyb.add_abbreviation(x, y)
    btn_2.configure(fg='green')


def saiv3():
    x = ent31.get()
    y = ent32.get()
    print(x, y)
    bd[x] = y
    keyb.add_abbreviation(x, y)
    btn_3.configure(fg='green')


def saiv4():
    x = ent41.get()
    y = ent42.get()
    print(x, y)
    bd[x] = y
    keyb.add_abbreviation(x, y)
    btn_4.configure(fg='green')


def saiv5():
    x = ent51.get()
    y = ent52.get()
    print(x, y)
    bd[x] = y
    keyb.add_abbreviation(x, y)
    btn_5.configure(fg='green')


def saiv6():
    x = ent61.get()
    y = ent62.get()
    print(x, y)
    bd[x] = y
    keyb.add_abbreviation(x, y)
    btn_6.configure(fg='green')


def chur():
    text2.delete(1.0, END)
def util_1():
    ent11.delete(0,END)
    ent12.delete(0,END)
    btn_1.configure(fg='black')
def util_2():
    ent21.delete(0,END)
    ent22.delete(0,END)
    btn_2.configure(fg='black')
def util_3():
    ent31.delete(0,END)
    ent32.delete(0,END)
    btn_3.configure(fg='black')
def util_4():
    ent41.delete(0,END)
    ent42.delete(0,END)
    btn_4.configure(fg='black')
def util_5():
    ent51.delete(0,END)
    ent52.delete(0,END)
    btn_5.configure(fg='black')
def util_6():
    ent61.delete(0,END)
    ent62.delete(0,END)
    btn_6.configure(fg='black')
def tuh():
    f = open('t_bd.txt', 'a', encoding='utf-8')
    for i in bd:
        f.write(i + ':' + bd[i] + '\n')
    f.close

def load():
    f = open('t_bd.txt','r', encoding='utf-8')
    z = f.readlines()
    f.close()
    f.close()
    for i in z :
        i = i.replace('\n','')
        x,y = i.split(':')
        keyb.add_abbreviation(x, y)
        a = (''.join(z))
    text1.insert(1.0,a)
bd = {}
win = Tk()
win.title('Счастье обычного сотрудника большой компани, который хочет мало печатать,а не вот это вот всё')
win.geometry('1200x700')
win['bg'] = '#BDBDBD'
win.resizable(False, False)
canvas = tkinter.Canvas(win,height = 700,width  = 1200)
img = tkinter.PhotoImage(file = '567.png')
lab = Label(win, image= img)
lab.place(x = 0, y = 0, relwidth = 1, relheight = 1)
canvas.pack()
f_f = Frame(canvas, bg='#BDBDBD')
f_1 = Frame(win, bg='#BDBDBD')
f_2 = Frame(win, bg='#BDBDBD')
f_3 = Frame(win, bg='#BDBDBD')
f_4 = Frame(win, bg='#BDBDBD')
f_5 = Frame(win, bg='#BDBDBD')
f_6 = Frame(win, bg='#BDBDBD')
f_X = Frame(win, bg='#BDBDBD')
f_7 = Frame(win, bg='#BDBDBD')
f_f.pack()
f_1.pack()
f_2.pack()
f_3.pack()
f_4.pack()
f_5.pack()
f_6.pack()
f_7.pack()
f_X.pack()

# label1 = Label(f_f, text='Сокращение', width=20, bg='#BDBDBD', font=('Constantia', 10 ), fg='black', padx=5,
# pady=5, bd=5).pack(side=LEFT, ipady='11',pady = '5')
# label2 = Label(f_f, text='Что означает', width=80, bg='#BDBDBD', font=('Constantia', 20), fg='black',
# padx=5, pady=5, bd=5).pack(side=LEFT, ipady='11',pady = '5')
# label3 = Label(f_7, text='поле для ввода:', width=80, bg='#BDBDBD', font=('Constantia', 15), fg='black',
# padx=5, pady=5, bd=5).pack(side=LEFT, ipady='11', pady='5')
ent11 = Entry(f_1, width=20, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent12 = Entry(f_1, width=80, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent21 = Entry(f_2, width=20, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent22 = Entry(f_2, width=80, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent31 = Entry(f_3, width=20, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent32 = Entry(f_3, width=80, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent41 = Entry(f_4, width=20, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent42 = Entry(f_4, width=80, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent51 = Entry(f_5, width=20, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent52 = Entry(f_5, width=80, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent61 = Entry(f_6, width=20, bg='#BDBDBD', fg='black', font=('Constantia', 10))
ent62 = Entry(f_6, width=80, bg='#BDBDBD', fg='black', font=('Constantia', 10))
text1 = Text(f_X, width=49, height=15, bg='white', fg='black', font=('Constantia', 10))
text2 = Text(f_X, width=80, height=15, bg='white', fg='black', font=('Constantia', 10))
ent11.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent12.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent21.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent22.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent31.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent32.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent41.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent42.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent51.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent52.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent61.pack(side=LEFT, ipady='18', pady='5', padx='5')
ent62.pack(side=LEFT, ipady='18', pady='5', padx='5')
text1.pack(side=LEFT, ipady='18', pady='5', padx='5')
text2.pack(side=LEFT, ipady='18', pady='5', padx='5')
btn_1 = Button(f_1, text='Задействовать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=saiv1,
font=('Constantia', 10))
btn_1.pack(
ipady='11', pady='5',side = LEFT)
btn_11 = Button(f_1, text='убрать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=util_1,
font=('Constantia', 10)).pack(ipady='11', pady='5',padx = '10')
btn_2 = Button(f_2, text='Задействовать', width=20, bg='#90A4AE', fg='black', pady=5, padx=5, command=saiv2,
font=('Constantia', 10))
btn_2.pack(ipady='11', pady='5',side = LEFT)
btn_22 = Button(f_2, text='убрать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=util_2,
font=('Constantia', 10)).pack(ipady='11', pady='5',padx = '10')
btn_3 = Button(f_3, text='Задействовать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=saiv3,
font=('Constantia', 10))
btn_3.pack(ipady='11', pady='5',side = LEFT)
btn_33 = Button(f_3, text='убрать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=util_3,
font=('Constantia', 10)).pack(ipady='11', pady='5',padx = '10')
btn_4 = Button(f_4, text='Задействовать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=saiv4,
font=('Constantia', 10))
btn_4.pack(ipady='11', pady='5',side = LEFT)
btn_44 = Button(f_4, text='убрать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=util_4,
font=('Constantia', 10)).pack(ipady='11', pady='5',padx = '10')
btn_5 = Button(f_5, text='Задействовать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=saiv5,
font=('Constantia', 10))
btn_5.pack(ipady='11', pady='5',side = LEFT)
btn_55 = Button(f_5, text='убрать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=util_5,
font=('Constantia', 10)).pack(ipady='11', pady='5',padx = '10')
btn_6 = Button(f_6, text='Задействовать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=saiv6,
font=('Constantia', 10))
btn_6.pack(ipady='11', pady='5',side = LEFT)
btn_66 = Button(f_6, text='убрать', width=20, bg='#90A4AE', fg='black', padx=5, pady=5, command=util_6,
font=('Constantia', 10)).pack(ipady='11', pady='5',padx = '10')
btn_7 = Button(f_X, text='Говор', width=20, bg='#90A4AE', fg='black', command=speak, font=('Constantia', 10))
btn_7.pack(
ipady='11', pady='5')
# btn_445 = Button(f_X,text = 'копировать ' ,width = 20,fg = 'black',command = copy).pack(ipady ='5')
btn_8 = Button(f_X, text='C', width=20, bg='#90A4AE', fg='black', command=chur, font=('Constantia', 10)).pack(
ipady='11', pady='5')
btn_9 = Button(f_X, text='скоп', width=20, bg='#90A4AE', fg='black', command=copy_buf, font=('Constantia', 10)).pack(
ipady='11', pady='5')
btn_10 = Button(f_X, text='сохр', width=20, bg='#90A4AE', fg='black', command= tuh, font=('Constantia', 10)).pack(
ipady='11', pady='5')
load()
win.mainloop()