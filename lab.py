import tkinter as tk
import random

class KeyGenApp:
    def __init__(self, root):
        self.window = root
        self.window.title('مولد المفاتيح (الاختيار 8)')
        self.window.geometry('500x350')

        self.setup_ui()

    def setup_ui(self):
        """إعداد واجهة المستخدم."""
        self.input_label = tk.Label(self.window, text='أدخل الرقم: ', font=14)
        self.input_label.place(relx=0.195, rely=0.23)

        self.key_input = tk.Entry(self.window, width=3, font=16)
        self.key_input.insert(0, '123')  # المدخل الافتراضي للمثال
        self.key_input.place(relx=0.45, rely=0.23)

        self.btn_generate = tk.Button(self.window, text='توليد المفتاح', font=14, width=12, command=self.generate_key)
        self.btn_generate.place(relx=0.195, rely=0.3)

        self.output_label = tk.Label(self.window, text='المفتاح الناتج: ', font=14)
        self.output_label.place(relx=0.195, rely=0.385)

        self.key_output = tk.Entry(self.window, width=30, font=16)
        self.key_output.place(relx=0.29, rely=0.385)

    def generate_key(self):
        """توليد المفتاح بناءً على المدخل."""
        input_value = self.key_input.get()

        if not input_value.isdigit() or len(input_value) != 3:
            tk.messagebox.showwarning('خطأ 449', 'المدخل غير صالح! يرجى إدخال رقم مكون من 3 أرقام.')
            return

        key = self.create_key(input_value)
        self.key_output.delete(0, tk.END)
        self.key_output.insert(0, key)

    def create_key(self, input_value):
        """إنشاء المفتاح مع تطبيق التحريك بناءً على المدخل."""
        input_digits = [int(digit) for digit in input_value]

        # إنشاء الكتلة الأولى بمزيج عشوائي من الحروف والأرقام
        key = []
        key.append(self.generate_random_block())

        # إنشاء الكتل التالية مع تطبيق التحريك
        for i, shift in enumerate(input_digits):
            if i % 2 == 0:  # الأرقام الزوجية: التحريك لليمين
                key.append(self.shift_string(key[i], shift, direction='right'))
            else:  # الأرقام الفردية: التحريك لليسار
                key.append(self.shift_string(key[i], shift, direction='left'))

        return '-'.join(key)

    def generate_random_block(self):
        """إنشاء كتلة عشوائية مكونة من حروف وأرقام."""
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(random.choice(characters) for _ in range(5))

    def shift_string(self, block, shift, direction='right'):
        """تحريك الحروف في الكتلة لليسار أو لليمين."""
        block_list = list(block)
        shift = shift % len(block_list)  # ضمان أن التحريك داخل الحدود

        if direction == 'right':
            return ''.join(block_list[-shift:] + block_list[:-shift])
        elif direction == 'left':
            return ''.join(block_list[shift:] + block_list[:shift])

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyGenApp(root)
    root.mainloop()
