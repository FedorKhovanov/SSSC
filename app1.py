import pyperclip
import random
import tkinter as tk
from tkinter import messagebox

def random_number(min_value, max_value):
    pre_result_number = random.randint(min_value, max_value - 1)
    result_number = f"001{pre_result_number}"
    return result_number

def copy_to_clipboard(text):
    pyperclip.copy(text)

def show_result():
    generated_number = random_number(10**16, 10**17)
    result_label.config(text=generated_number)
    copy_to_clipboard(generated_number)
    

# Создание GUI
root = tk.Tk()
root.title("SSSC Generator")

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

refresh_button = tk.Button(root, text="Сгенерировать SSSC и скопировать в буфер обмена", command=show_result)
refresh_button.pack(pady=20)

# Генерация и отображение числа при запуске приложения
show_result()

root.mainloop()