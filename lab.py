import tkinter as tk
import random
import string
from tkinter import messagebox
import pygame

# Global variables for UI components
window = None
dec_input_entry = None
key_display = None

def generate_key():
    """Generates a key based on a 3-digit DEC input."""
    dec_input = dec_input_entry.get().strip()
    
    # Validate the input (must be a 3-digit DEC number)
    if not dec_input.isdigit() or len(dec_input) != 3:
        messagebox.showerror("Error", "Please enter a valid 3-digit DEC number.")
        return

    # Extract shifts from the input
    shifts = [int(digit) for digit in dec_input]
    key_parts = []
    current_length = 5

    # Generate key blocks with alternating shifts
    for i, shift in enumerate(shifts):
        block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=current_length))
        if i % 2 == 0:
            block = shift_string(block, shift)
        else:
            block = shift_string(block, -shift)
        key_parts.append(block)
        current_length -= 1  

    # Add the final block with 2 characters
    last_block = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    key_parts.append(last_block)

    # Join blocks to form the key and display it
    key = '-'.join(key_parts)
    key_display.delete(0, tk.END)
    key_display.insert(0, key)

def shift_string(s, shift):
    """Shifts characters in the string by a specified amount."""
    characters = string.ascii_uppercase + string.digits
    shifted = []
    
    for char in s:
        if char in characters:
            index = characters.index(char)
            new_index = (index + shift) % len(characters)
            shifted.append(characters[new_index])
        else:
            shifted.append(char)
    
    return ''.join(shifted)

def animate_frame(frame):
    """Animates the background color of a frame."""
    colors = ['#FF4500', '#FFD700', '#32CD32', '#1E90FF', '#8A2BE2']
    
    def change_color(index):
        frame.config(bg=colors[index % len(colors)])
        window.after(500, change_color, index + 1)
    
    change_color(0)

def setup_ui():
    """Sets up the user interface for the key generator."""
    global window, dec_input_entry, key_display

    window = tk.Tk()
    window.title("Cyber Dabbas 2024")
    window.geometry("1300x750")

    # Set up the background image
    bg_image = tk.PhotoImage(file="background_image.png")
    window.bg_image = bg_image  # Prevent garbage collection of the image
    background_label = tk.Label(window, image=bg_image)
    background_label.place(relwidth=1, relheight=1)

    # Create a frame for input and buttons
    frame = tk.Frame(window, borderwidth=3, relief="ridge", bg='#006400')
    frame.pack(padx=5, pady=5)
    frame.place(x=569, y=448)
    
    # Input label and entry
    dec_input_label = tk.Label(frame, text="Enter a 3-digit DEC number:", bg='white', fg='black')
    dec_input_label.pack(pady=5, padx=5)
    
    dec_input_entry = tk.Entry(window, bg='#006400', fg="white", font=("Arial", 12))
    dec_input_entry.pack(pady=5)
    dec_input_entry.place(relx=0.444, rely=0.65)

    # Button to generate the key
    generate_button = tk.Button(window, text="Generate Key", command=generate_key, bg='#4682B4', fg='white', font=("Arial", 12))
    generate_button.pack(pady=3, padx=10)
    generate_button.place(x=580, y=525)

    # Output entry for the generated key
    key_display = tk.Entry(window, font=("Arial", 14), bg='#006400', justify='center', fg="white")
    key_display.pack(pady=10)
    key_display.place(relx=0.45, rely=0.75)

    # Play background music
    pygame.mixer.init()
    pygame.mixer.music.load("background-music.mp3")
    pygame.mixer.music.play(-1)

    # Start frame animation
    animate_frame(frame)

if __name__ == "__main__":
    setup_ui()
    window.mainloop()
