""" This file is responsible for gathering all
files and create a GUI that display them in a
user friendly matter, the GUI is completely made from AI"""
import tkinter as tk
from tkinter import ttk, messagebox

# Import your cipher functions
from Cyphers.CeaserKey import decryptCeaser
from Cyphers.Rot13Key import decryptROT13
from Cyphers.AtbashKey import decryptAtbash
from Cyphers.base64Key import decryptBASE64
from Cyphers.binarykey import decryptBinary
from Cyphers.HexKEY import decryptHEX
from Cyphers.morseCodeKey import decryptMorse


# Function to run when "Decode" button is clicked
def run_decoder():
    cipher = cipher_choice.get()
    text = input_text.get("1.0", tk.END).strip()
    shift_value = shift_entry.get().strip()

    try:
        if cipher == "Caesar":
            shift = int(shift_entry.get())
            result = decryptCeaser(text, shift)

        elif cipher == "ROT13":
            result = decryptROT13(text)

        elif cipher == "Atbash":
            result = decryptAtbash(text)

        elif cipher == "Base64":
            result = decryptBASE64(text)#.decodeBase64()

        elif cipher == "Morse Code":
            result = decryptMorse(text)

        elif cipher == "Binary":
            result = decryptBinary(text)

        elif cipher == "Hex":
            result = decryptHEX(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# --- Tkinter GUI setup ---
root = tk.Tk()
root.title("ARGToolBox Decoder")
root.geometry("500x400")

# Cipher selection
tk.Label(root, text="Select Cipher:").pack(pady=5)
cipher_choice = ttk.Combobox(root, values=[
    "Caesar", "ROT13", "Atbash", "Base64", "Morse Code", "Binary", "Hex"
])
cipher_choice.pack()
cipher_choice.current(0)

# Shift entry (only used by Caesar)
tk.Label(root, text="Shift (only for Caesar):").pack(pady=5)
shift_entry = tk.Entry(root)
shift_entry.pack()

# Input text
tk.Label(root, text="Input Text:").pack(pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Decode button
decode_button = tk.Button(root, text="Decode", command=run_decoder)
decode_button.pack(pady=10)

# Output text
tk.Label(root, text="Decoded Output:").pack(pady=5)
output_text = tk.Text(root, height=5, width=50)
output_text.pack()

root.mainloop()
