import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Для работы с изображениями
import pygame  # Для воспроизведения музыки
import random

def generate_key():
    dec_input = entry_input.get()
    if not dec_input.isdigit() or len(dec_input) != 3:
        messagebox.showerror("Ошибка", "Введите DEC-число из 3 знаков.")
        return

    dec_digits = [int(d) for d in dec_input]
    blocks = []
    shift_direction = 1  # Начинаем сдвиг вправо

    # Генерация первого блока (случайные буквы и цифры)
    first_block = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=5))
    blocks.append(first_block)

    # Генерация последующих блоков с учётом сдвигов
    current_block = first_block
    for shift in dec_digits:
        current_block = shift_block(current_block, shift, shift_direction)
        blocks.append(current_block[:-1])  # Уменьшаем длину блока на 1
        shift_direction *= -1  # Меняем направление сдвига

    generated_key = "-".join(blocks)
    entry_output.delete(0, tk.END)
    entry_output.insert(0, generated_key)

def shift_block(block, shift, direction):
    """Выполняет сдвиг символов блока на заданное количество позиций."""
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    result = []
    for char in block:
        idx = symbols.index(char)
        new_idx = (idx + direction * shift) % len(symbols)
        result.append(symbols[new_idx])
    return ''.join(result)

# Настройка интерфейса
root = tk.Tk()
root.title("Keygen - Вариант 8")
root.geometry("400x300")
root.resizable(False, False)

# Настройка музыки
pygame.mixer.init()
pygame.mixer.music.load("background_music.mp3")  # Замените на название вашего файла музыки
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение

# Настройка фона
image = Image.open("background_image.jpg")  # Замените на название вашего файла изображения
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(relwidth=1, relheight=1)

# Ввод DEC-числа
label_input = tk.Label(root, text="Введите DEC-число (3 знака):", bg="lightblue", font=("Arial", 12))
label_input.pack(pady=10)
entry_input = tk.Entry(root, font=("Arial", 12), justify="center")
entry_input.pack(pady=5)

# Кнопка генерации
btn_generate = tk.Button(root, text="Сгенерировать ключ", font=("Arial", 12), command=generate_key)
btn_generate.pack(pady=10)

# Поле вывода ключа
label_output = tk.Label(root, text="Сгенерированный ключ:", bg="lightblue", font=("Arial", 12))
label_output.pack(pady=10)
entry_output = tk.Entry(root, font=("Arial", 12), justify="center", state="readonly")
entry_output.pack(pady=5)

# Запуск приложения
root.mainloop()
