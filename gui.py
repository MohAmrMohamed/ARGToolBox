"""
ARGToolBox GUI - Improved Layout

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

# Import cipher functions
from Cyphers.CeaserKey import decryptCeaser
from Cyphers.Rot13Key import decryptROT13
from Cyphers.AtbashKey import decryptAtbash
from Cyphers.base64Key import decryptBASE64
from Cyphers.binarykey import decryptBinary
from Cyphers.HexKEY import decryptHEX
from Cyphers.morseCodeKey import decryptMorse

# --- Functions ---
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

        # Display result in read-only output
        output_text.config(state="normal")
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result)
        output_text.config(state="disabled")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def toggle_shift_box(event):
    if cipher_choice.get() == "Caesar":
        shift_frame.pack(fill="x", pady=5)
    else:
        shift_frame.pack_forget()

# --- Main GUI ---
root = tk.Tk()
root.title("ARGToolBox Decoder")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# --- Cipher Selection Frame ---
cipher_frame = tk.LabelFrame(root, text="Cipher Selection", padx=10, pady=10, font=("Arial", 10, "bold"))
cipher_frame.pack(fill="x", padx=15, pady=10)

tk.Label(cipher_frame, text="Select Cipher:", font=("Arial", 10)).pack(side="left", padx=(0,5))
cipher_choice = ttk.Combobox(cipher_frame, values=[
    "Caesar", "ROT13", "Atbash", "Base64", "Morse Code", "Binary", "Hex"
], width=20, font=("Arial", 10))
cipher_choice.pack(side="left")
cipher_choice.current(0)
cipher_choice.bind("<<ComboboxSelected>>", toggle_shift_box)

# Shift frame inside cipher selection
shift_frame = tk.Frame(cipher_frame)
shift_label = tk.Label(shift_frame, text="Shift (only for Caesar):", font=("Arial", 10))
shift_entry = tk.Entry(shift_frame, width=5, font=("Arial", 10))
shift_label.pack(side="left", padx=(10,5))
shift_entry.pack(side="left")
if cipher_choice.get() != "Caesar":
    shift_frame.pack_forget()
else:
    shift_frame.pack(side="left", padx=10)

# --- Input Frame ---
input_frame = tk.LabelFrame(root, text="Input Text", padx=10, pady=10, font=("Arial", 10, "bold"))
input_frame.pack(fill="both", padx=15, pady=10, expand=True)

input_text = tk.Text(input_frame, height=7, width=70, font=("Arial", 10), wrap="word")
input_text.pack(fill="both", expand=True)

# --- Decode Button ---
decode_button = tk.Button(root, text="Decode", command=run_decoder, font=("Arial", 12, "bold"),
                          bg="#4CAF50", fg="white", relief="raised", padx=10, pady=5)
decode_button.pack(pady=10)

# --- Output Frame ---
output_frame = tk.LabelFrame(root, text="Decoded Output", padx=10, pady=10, font=("Arial", 10, "bold"))
output_frame.pack(fill="both", padx=15, pady=10, expand=True)

output_text = tk.Text(output_frame, height=7, width=70, font=("Arial", 10), wrap="word", state="disabled", bg="#e8e8e8")
output_text.pack(fill="both", expand=True)

root.mainloop()
