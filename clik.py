from tkinter import *

clicks = 0


def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))


root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

btn = Button(text="Click Me", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=click_button)
btn.pack()

root.mainloop()

# btn = Button(text="Hello",          # текст кнопки
#              background="#555",     # фоновый цвет кнопки
#              foreground="#ccc",     # цвет текста
#              padx="20",             # отступ от границ до содержимого по горизонтали
#              pady="8",              # отступ от границ до содержимого по вертикали
#              font="16"              # высота шрифта
#              )