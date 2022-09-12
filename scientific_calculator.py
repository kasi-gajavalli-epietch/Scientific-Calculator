from tkinter import *
from math import *
from pygame import mixer
import speech_recognition

mixer.init()


def click(value):
    ex = entryField.get()
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    l=math.lcm(a,b)
    return l

def hcf(a,b):
    h=math.gcd(a,b)
    return h

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            print(sr)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)

            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1]) #mul(5.0,6.0)
                    entryField.delete(0,END)
                    entryField.insert(END,result)

                else:
                    pass
        except:
            pass

window = Tk()
window.title('Scientific Calculator')
window.config(bg='#101419')
window.geometry('690x486+100+100')

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(window, image=logoImage, bg='#101419')
logoLabel.grid(row=0, column=0)

entryField = Entry(window, font=('arial', 20, 'bold'), bg='#101419', fg='#FFF', width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(window, image=micImage, bd=0, bg='#476C9B', activebackground='#476C9B',command=audio)
micButton.grid(row=0, column=7)
Button(window, text="Close", bg='#476C9B', fg="#FFF",font=('arial', 16), activebackground='#476C9B', command=window.quit).grid(row=8, column=3,pady=16)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ","1", "2", "3", "-", "2π", "cosh", "tanh", "sinh","4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg", "rad", "e", "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1
columnvalue = 0
for i in button_text_list:

    button = Button(window, width=5, height=2, text=i, bd=0, bg='#476C9B', fg="#FFF",font=('arial', 16), activebackground='#476C9B', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

window.mainloop()