import tkinter as tk
import random
import pygame

# دالة لتشغيل الموسيقى
def play_music():
    pygame.mixer.music.load("Cyberpunk_2077_Main_Theme.mp3")  # تحميل ملف الموسيقى
    pygame.mixer.music.play()  # تشغيل الموسيقى

# دالة لتوليد المفتاح
def generator():
    input_value = key_input.get()

    # التأكد من أن المدخل صالح
    if input_value == '' or not input_value.isdigit() or int(input_value) > 999 or int(input_value) < 100:
        tk.messagebox.showwarning('Error 449', 'The key cannot be generated!')
    else:
        elements = [0, 0, 0, 0, 0]
        key = ""
        element_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # القائمة التي تحتوي على الحروف والأرقام

        # توليد العنصر الأول
        for i in range(5):
            elements[i] += random.randint(0, 34)
            key += element_list[elements[i]]
        key += "-"

        # توليد العنصر الثاني
        for i in range(4):
            elements[i] += (int(input_value) // 100)
            if elements[i] > 35:
                elements[i] -= 10
            elif elements[i] >= 26 and (elements[i] - (int(input_value) // 100)) <= 25:
                elements[i] -= 25
            key += element_list[elements[i]]
        key += "-"

        # توليد العنصر الثالث
        for i in range(3):
            elements[i] -= ((int(input_value) // 10) % 10)
            if elements[i] < 26 and (elements[i] + ((int(input_value) // 10) % 10)) > 25:
                elements[i] += 10
            elif elements[i] < 0:
                elements[i] += 25
            key += element_list[elements[i]]
        key += "-"

        # توليد العنصر الرابع
        for i in range(2):
            elements[i] += (int(input_value) % 10)
            if elements[i] >= 35:
                elements[i] -= 10
            elif elements[i] >= 26 and (elements[i] - (int(input_value) % 100)) <= 25:
                elements[i] -= 25
            key += element_list[elements[i]]
        key_output.delete("0", tk.END)  # مسح المحتوى القديم
        key_output.insert(0, key)  # إدخال المفتاح الجديد

if __name__ == "__main__":
    # إنشاء نافذة البرنامج
    window = tk.Tk()
    window.title('Key generator for Cyberpunk 2077')  # عنوان النافذة
    window.geometry('1200x675')  # أبعاد النافذة
    pygame.init()  # تهيئة مكتبة pygame

    # إضافة صورة الخلفية الخاصة بلعبة Cyberpunk 2077
    bg_img = tk.PhotoImage(file='cyberpunk2077.png')  # تأكد من مسار الصورة
    lbl_bg = tk.Label(window, image=bg_img)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    play_music()  # تشغيل الموسيقى

    # إضافة المدخلات
    input_label = tk.Label(window, text='Enter secret sequence (3 digits): ', font=14)
    input_label.place(relx=0.195, rely=0.23)
    key_input = tk.Entry(window, width=3, font=16)
    key_input.insert(0, '000')  # قيمة افتراضية
    key_input.place(relx=0.45, rely=0.23)

    # إضافة زر التوليد
    btn_guess = tk.Button(window, text='Generate KEY', font=14, width=12, command=generator)
    btn_guess.place(relx=0.195, rely=0.3)

    # إضافة مخرج المفتاح
    output_label = tk.Label(window, text='Game key: ', font=14)
    output_label.place(relx=0.195, rely=0.385)
    key_output = tk.Entry(window, width=30, font=16)
    key_output.place(relx=0.29, rely=0.385)

    # بدء البرنامج
    window.mainloop()
