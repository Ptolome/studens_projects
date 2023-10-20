from tkinter import *
import speech_recognition as sr
from math import *
import pyaudio
z = []
win = Tk()
win['bg'] = '#8D6E63'
win.title('Сергей не куил deep rock')
win.geometry('550x575')
win.resizable(False, False)
win.attributes('-topmost', 1)
win.attributes('-topmost', 0)
f_top = Frame(win,bg = '#8D6E63')
f_bot = Frame(win,bg = '#8D6E63')
f_ru = Frame(win,bg = '#8D6E63')
f_t = Frame(win,bg = '#8D6E63')
f_tu = Frame(win,bg = '#8D6E63')
f_oh = Frame(win,bg = '#8D6E63')
f_top.pack()
f_oh.pack()
f_bot.pack()
f_ru.pack()
f_t.pack()
f_tu.pack()
label1 = Label(f_top, width=10, text='Кулькулятор', font=('Comic Sans MS', 20, 'bold'),bg='#8D6E63', fg='#B2DFBD', bd=5)
label1.pack()
ent = Entry(f_oh, justify='right', width=400, bd=15,font = (20),bg = '#8D6E63',fg = '#B2DFBD')
ent.pack(ipadx=10, ipady=10)
def daf(a):
    if a == 'один' :
        a = '1'
    elif a == 'два ' :
        a = '2'
    elif a == 'три ':
        a = '3'
    elif a == 'четыре ' :
        a = '4'
    elif a == 'пять':
        a = '5'
    elif a== 'шесть':
        a == '6'
    return( a)
def ghost():
    if len(z) >= 3:
        z.clear()
        ent.delete(0,END)
        print('cl')
def doom():
    ghost()
    x = ent.get()
    x = x + '1'
    ent.delete(0, END)
    ent.insert(-1, x)
def prey():
    ghost()
    x = ent.get()
    x = x + '2'
    ent.delete(0,END)
    ent.insert(-1, x)
def deep_rock():
    ghost()
    x = ent.get()
    x = x + '3'
    ent.delete(0, END)
    ent.insert(-1, x)
def stalk():
    ghost()
    x = ent.get()
    x = x + '4'
    ent.delete(0, END)
    ent.insert(-1, x)
def bios():
    ghost()
    x = ent.get()
    x = x + '5'
    ent.delete(0, END)
    ent.insert(-1, x)
def atomic():
    ghost()
    x = ent.get()
    x = x + '6'
    ent.delete(0, END)
    ent.insert(-1, x)
def the_for():
    ghost()
    x = ent.get()
    x = x + '7'
    ent.delete(0, END)
    ent.insert(-1, x)
def the_cats():
    ghost()
    x = ent.get()
    x = x + '8'
    ent.delete(0, END)
    ent.insert(-1, x)
def poke():
    ghost()
    x = ent.get()
    x = x + '9'
    ent.delete(0, END)
    ent.insert(-1, x)
def joke():
    ghost()
    x = ent.get()
    x = x + '0'
    ent.delete(0, END)
    ent.insert(-1, x)
def pluc():
    x = ent.get()
    z.append(x)
    ent.delete(0,END)
    ent.insert(-1,'')
    z.append('+')
    print(z)
def pr():
    x = ent.get()
    z.append(x)
    ent.delete(0,END)
    ent.insert(-1,'')
    z.append('-')
    print(z)
def da():
    x = ent.get()
    z.append(x)
    ent.delete(0,END)
    ent.insert(-1,'')
    z.append('*')
    print(z)

def ne():
    x = ent.get()
    z.append(x)
    ent.delete(0, END)
    ent.insert(-1, '')
    z.append('/')
    print(z)
def ge():
    x = ent.get()
    z.append(x)
    ent.delete(0, END)
    ent.insert(-1, '')
    z.append('//')
    print(z)
def tur ():
    ghost()
    x = ent.get()
    x = x + '.'
    ent.delete(0, END)
    ent.insert(-1, x)
    print(z)
def kir():
    x = ent.get()
    gh = int(x)
    ent.delete(0,END)
    g = gh%400
    h = gh%4
    d = gh%100
    if d== 0:
        if g == 0:
            ent.insert(-1, 'Високосный год ')
        else :
            ent.insert(-1,'Не високосный год')
    elif  h == 0:
        ent.insert(-1,'Високосный год')
    elif h != 0:
        ent.insert(-1,'Не високосный год')
    if gh%12 == 0 :
        ent.insert(-1, 'Год обезьяны, ')
    if gh%12 == 1:
        ent.insert(-1, 'Год петуха, ')
    if gh%12 == 2:
        ent.insert(-1, 'Год собаки, ')
    if gh%12 == 3:
        ent.insert(-1, 'Год свиньи, ')
    if gh%12 == 4:
        ent.insert(-1, 'Год крысы, ')
    if gh%12 == 5:
        ent.insert(-1, 'Год быка, ')
    if gh%12 == 6:
        ent.insert(-1, 'Год тигра, ')
    if gh%12 == 7:
        ent.insert(-1, 'Год кролика, ')
    if gh%12 == 8:
        ent.insert(-1, 'Год дракона, ')
    if gh%12 == 9:
        ent.insert(-1, 'Год змеи, ')
    if gh%12 == 10:
        ent.insert(-1, 'Год лошади, ')
    if gh%12 == 11:
        ent.insert(-1, 'Год овцы, ')
def pre():
    x = ent.get()
    z.append(x)
    ent.delete(0, END)
    ent.insert(-1, '')
    z.append('%')
    print(z)
def frog():
    c = ent.get()
    ent.delete(0,END)
    ent.insert(-1, c[:-1])
def chu():
    ent.delete(0,END)
    print(z)
def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration = 0.1)
        data = r.record(source, duration=3)
        text = r.recognize_google(data,language='ru-RU')
        print(text)
        text = daf(text)
        ent.delete(0,END)
        ent.insert( -1,text)
        print(text)
def Entr():
    x = ent.get()
    z.append(x)
    ent.delete(0,END)
    if z[1]=='+':
        b = int(z[0]) + int(z[2])
        ent.insert(-1,str(b))
    elif z[1]=='-':
        b = int(z[0]) - int(z[2])
        ent.insert(-1,str(b))
    elif z[1]=='*':
        b = int(z[0]) * int(z[2])
        ent.insert(-1,str(b))
    elif z[1] == '/':
        b = float(z[0]) / float(z[2])
        ent.insert(-1, str(b))
    elif z[1] == '//':
        b = int(z[0]) // int(z[2])
        ent.insert(-1, str(b))
    elif z[1] == '%':
        b = float(z[0]) % float(z[2])
        ent.insert(-1, str(b))

btn1 = Button(f_bot, width=3, text='1', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=doom).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn2 = Button(f_bot, width=3, text='2', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=prey).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn3 = Button(f_bot, width=3, text='3', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=deep_rock).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn4 = Button(f_ru, width=3, text='4', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=stalk).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn5 = Button(f_ru, width=3, text='5 ', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=bios).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn6 = Button(f_ru, width=3, text='6', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=atomic).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn7 = Button(f_t, width=3, text='7', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=the_for).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn8 = Button(f_t, width=3, text='8', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=the_cats).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn9 = Button(f_t, width=3, text='9', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
              command=poke).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn0 = Button(f_bot, width=3, text='0', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=joke).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn10 = Button(f_tu, width=3, text='+', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=pluc).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn11 = Button(f_tu, width=3, text='-', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=pr).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn12 = Button(f_tu, width=3, text='*', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=da).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn13 = Button(f_bot, width=3, text='/', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=ne).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn14 = Button(f_ru, width=3, text='//', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=ge).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn15 = Button(f_t, width=3, text='%', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=pre).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn16 = Button(f_tu, width=3, text='=', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=Entr).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn17 = Button(f_tu, width=3, text='<-', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=frog).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn18 = Button(f_ru, width=3, text='C', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=chu).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn19 = Button(f_top, width=3, text='speak', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=speak).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
btn20 = Button(f_top, width=3, text='Анализ года', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=kir).pack(side=LEFT, padx=5, pady=5, ipadx=100, ipady=20)
btn21 = Button(f_t, width=3, text='.', font = (20),bg='#B2DFBD', fg='#8D6E63', highlightcolor='red', bd=2,
               command=tur).pack(side=LEFT, padx=5, pady=5, ipadx=20, ipady=20)
win.mainloop()
