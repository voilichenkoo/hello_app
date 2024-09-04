#Напишите программу на Python с использованием модуля tkinter,
#которая позволяет пользователю ввести свое имя в окно ввода,
#а затем выводит на экран сообщение "Привет, [имя]!".
import tkinter as tk

def hello_name():
    name = entry.get()
    label_2 = tk.Label(root, text = f"Привет, {name} !" )
    label_2.pack()

root = tk.Tk()
root.title(" Окно приветствия")

label = tk.Label(root, text = "Введите имя ")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text = "Готово", command = hello_name)
button.pack()

root.mainloop()