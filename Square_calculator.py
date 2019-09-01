from tkinter import *
from math import sqrt

def solver(a,b,c):
    """ Решает квадратичное уравнение и возвращает результат в  строке"""
    D = b*b - 4*a*c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        text = "Дискриминант равен: %s \n X1  равен: %s \n X2 равен: %s \n" % (D, x1, x2)        
    else:
        text = "Дискриминант равен: %s \n Данное уравнение не имеет корней" % D 
    return text
def inserter(value):
    """ Вводиться значение """
    output.delete("0.0","end")
    output.insert("0.0",value)    

def clear(event):
    """ Удаляет текст в окне """
    caller = event.widget
    caller.delete("0", "end")

def handler():
    """ Преобразует вводимый текст в окно """
    try:
        # make sure that we entered correct values
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solver(a_val, b_val, c_val))
    except ValueError:
        inserter("Введите все значения переменных")

root = Tk()
root.title("Калькулятор для квадратных уравнений")
root.minsize(100,100)
root.resizable(width=False, height=False)


frame = Frame(root)
frame.grid()

a = Entry(frame, width=3)
a.grid(row=1,column=1,padx=(10,0))
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="x**2+").grid(row=1,column=2)

b = Entry(frame, width=3)
b.bind("<FocusIn>", clear)
b.grid(row=1,column=3)
b_lab = Label(frame, text="x+").grid(row=1, column=4)

c = Entry(frame, width=3)
c.bind("<FocusIn>", clear)
c.grid(row=1, column=5)
c_lab = Label(frame, text="= 0").grid(row=1, column=6)

but = Button(frame, text="Посчитать", command=handler).grid(row=1, column=7, padx=(10,0))

output = Text(frame, bg="white", font=" Calibri 10", width=35, height=10)
output.grid(row=2, columnspan=8)

root.mainloop()


