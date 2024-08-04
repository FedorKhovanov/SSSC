import pyperclip
import random
import tkinter as tk
from tkinter import ttk

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

def show_about():
    about_text = """
    Чтобы не попасть в ситуацию ХВГ (хотя вероятность генерации одинаковых SSSC менее чем 0.001%) используйте на свой страх и риск)))
    Благодарность в жидкой валюте можно выразить сюда -> Fedor.Khovanov@pepsico.com
    """
    about_window = tk.Toplevel(root)
    about_window.title("Инфо")
    about_label = tk.Label(about_window, text=about_text, font=("Arial", 10), justify="left", padx=20, pady=20) # Шрифт уменьшен
    about_label.pack()

# Создание GUI
root = tk.Tk()
root.title("SSSC Генератор")

# Задание размера окна
window_width = 400
window_height = 200
root.geometry(f"{window_width}x{window_height}")

# Создание меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Добавление меню About
about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Меню", menu=about_menu)
about_menu.add_command(label="Инфо", command=show_about)

# Основное окно
result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=20)

refresh_button = tk.Button(root, text="Сгенерировать SSSC и скопировать в буфер обмена", command=show_result)
refresh_button.pack(pady=20)

# Генерация и отображение числа при запуске приложения
show_result()

root.mainloop()
