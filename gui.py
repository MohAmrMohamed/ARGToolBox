"""
ARGToolBox GUI

This GUI gathers all cipher decoders and provides a user-friendly interface.

HOW TO ADD A NEW CIPHER:
1. Place your new cipher file in the 'Cyphers' folder.
2. Ensure the file has a function or class for decoding (e.g., decryptMyCipher).
3. Import it at the top of this script:
   from Cyphers.MyCipherFile import decryptMyCipher
4. Add your cipher name to the 'values' list of the dropdown.
5. Add a corresponding 'elif' branch in run_decoder() to call your function.
"""

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

# --- Function to run when "Decode" button is clicked ---
def run_decoder():
    cipher = cipher_choice.get()
    text = input_text.get("1.0", tk.END).strip()
    shift_value = shift_entry.get().strip()

    try:
        if cipher == "Caesar":
            if not shift_value.isdigit():
                messagebox.showerror("Error", "Shift must be an integer!")
                return
            shift = int(shift_value)
            result = decryptCeaser(text, shift)

        elif cipher == "ROT13":
            result = decryptROT13(text)

        elif cipher == "Atbash":
            result = decryptAtbash(text)

        elif cipher == "Base64":
            result = decryptBASE64(text)

        elif cipher == "Morse Code":
            result = decryptMorse(text)

        elif cipher == "Binary":
            result = decryptBinary(text)

        elif cipher == "Hex":
            result = decryptHEX(text)

        # Show result in read-only Text widget
        output_text.config(state="normal")   # temporarily enable editing
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state="disabled")  # disable editing

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# --- Function to toggle shift box visibility ---
def toggle_shift_box(event):
    if cipher_choice.get() == "Caesar":
        shift_label.pack(pady=5)
        shift_entry.pack()
    else:
        shift_label.pack_forget()
        shift_entry.pack_forget()

# --- Tkinter GUI setup ---
root = tk.Tk()
root.title("ARGToolBox Decoder")
root.geometry("500x450")

# Cipher selection
tk.Label(root, text="Select Cipher:").pack(pady=5)
cipher_choice = ttk.Combobox(root, values=[
    "Caesar", "ROT13", "Atbash", "Base64", "Morse Code", "Binary", "Hex"
])
cipher_choice.pack()
cipher_choice.current(0)
cipher_choice.bind("<<ComboboxSelected>>", toggle_shift_box)

# Shift entry (only used by Caesar)
shift_label = tk.Label(root, text="Shift (only for Caesar):")
shift_entry = tk.Entry(root)
toggle_shift_box(None)  # initial toggle

# Input text
tk.Label(root, text="Input Text:").pack(pady=5)
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Decode button
decode_button = tk.Button(root, text="Decode", command=run_decoder)
decode_button.pack(pady=10)

# Output text (read-only)
tk.Label(root, text="Decoded Output:").pack(pady=5)
output_text = tk.Text(root, height=5, width=50, state="disabled")
output_text.pack()

root.mainloop()
