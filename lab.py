import tkinter as tk
from tkinter import messagebox
import random

# دالة لإغلاق البرنامج
def cancel():
    window.destroy()

# دالة لحساب الحركات بناءً على الرقم المدخل
def generate_key():
    input_number = entry.get()

    # التحقق من صحة الإدخال (يجب أن يكون رقم مكون من 3 أرقام)
    if len(input_number) != 3 or not input_number.isdigit():
        messagebox.showwarning('إدخال غير صحيح', 'يجب إدخال رقم مكون من 3 أرقام!')
        return

    input_number = list(map(int, input_number))  # تحويل الأرقام إلى قائمة من الأرقام الفردية
    blocks = []
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # توليد الجزء الأول من المفتاح
    part1 = ''.join(random.choices(symbols, k=6))
    blocks.append(part1)

    # الجزء الثاني: تحريك الجزء الأول بمقدار الرقم الأول في الإدخال
    part2 = shift_string(part1, input_number[0])
    blocks.append(part2)

    # الجزء الثالث: تحريك الجزء الثاني بمقدار الرقم الثاني في الإدخال
    part3 = shift_string(part2, -input_number[1])
    blocks.append(part3)

    # الجزء الرابع: تحريك الجزء الثالث بمقدار الرقم الثالث في الإدخال
    part4 = shift_string(part3, input_number[2])
    blocks.append(part4)

    # تجميع المفتاح
    final_key = '-'.join(blocks)
    key_output.delete(0, tk.END)
    key_output.insert(0, final_key)

# دالة لتحريك السلسلة (حروف وأرقام) حسب العدد المعطى
def shift_string(s, shift):
    shifted = ''
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for char in s:
        index = symbols.index(char)
        new_index = (index + shift) % len(symbols)  # التأكد من أن التحريك يكون داخل النطاق
        shifted += symbols[new_index]
    return shifted

# إعداد واجهة المستخدم
window = tk.Tk()
window.title('مولد مفتاح اللعبة')
window.geometry('400x300')

# إضافة صورة خلفية
bg_img = tk.PhotoImage(file='gradient.png')  # تأكد من وجود هذه الصورة في المسار المناسب
label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

# واجهة المستخدم
label_input = tk.Label(window, text='أدخل رقم مكون من 3 أرقام:', font=('Verdana', 12))
label_input.place(relx=0.05, rely=0.1)

entry = tk.Entry(window, width=5, font=('Verdana', 16))
entry.place(relx=0.5, rely=0.1)

btn_generate = tk.Button(window, text='توليد المفتاح', font=('Verdana', 12), command=generate_key)
btn_generate.place(relx=0.05, rely=0.3)

key_output_label = tk.Label(window, text='المفتاح المولد:', font=('Verdana', 12))
key_output_label.place(relx=0.05, rely=0.5)

key_output = tk.Entry(window, width=30, font=('Verdana', 16))
key_output.place(relx=0.5, rely=0.5)

btn_cancel = tk.Button(window, text='إلغاء', font=('Verdana', 12), command=cancel)
btn_cancel.place(relx=0.5, rely=0.7)

# بدء الحلقة الرئيسية للنافذة
window.mainloop()
