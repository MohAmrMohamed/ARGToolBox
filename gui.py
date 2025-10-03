"""
ARGToolBox GUI - Improved Layout with Encode/Decode

This GUI gathers all cipher decoders/encoders and provides a user-friendly interface.

HOW TO ADD A NEW CIPHER:
1. Place your new cipher file in the 'Cyphers' folder.
2. Ensure the file has functions for decoding/encoding (e.g., decryptMyCipher, encryptMyCipher).
3. Import them at the top of this script:
   from Cyphers.MyCipherFile import decryptMyCipher, encryptMyCipher
4. Add your cipher name to the 'values' list of the dropdown.
5. Add corresponding 'elif' branches in run_cipher() to call the correct function.
"""

import tkinter as tk
from tkinter import ttk, messagebox

# Import cipher functions
from Cyphers.CeaserKey import decryptCeaser, encryptCeaser
from Cyphers.Rot13Key import decryptROT13, decryptROT13
from Cyphers.AtbashKey import decryptAtbash, decryptAtbash
from Cyphers.base64Key import decryptBASE64, encryptBASE64
from Cyphers.binarykey import decryptBinary, encryptBinary
from Cyphers.HexKEY import decryptHEX, encryptHEX
from Cyphers.morseCodeKey import decryptMorse, encryptMorse

# --- Functions ---
def run_cipher():
    cipher = cipher_choice.get()
    mode = mode_var.get()
    text = input_text.get("1.0", tk.END).strip()
    shift_value = shift_entry.get().strip()

    try:
        if cipher == "Caesar":
            if not shift_value.isdigit():
                messagebox.showerror("Error", "Shift must be an integer!")
                return
            shift = int(shift_value)
            result = encryptCeaser(text, shift) if mode == "Encode" else decryptCeaser(text, shift)

        elif cipher == "ROT13":
            result = decryptROT13(text) if mode == "Encode" else decryptROT13(text)

        elif cipher == "Atbash":
            result = decryptAtbash(text) if mode == "Encode" else decryptAtbash(text)

        elif cipher == "Base64":
            result = encryptBASE64(text) if mode == "Encode" else decryptBASE64(text)

        elif cipher == "Morse Code":
            result = encryptMorse(text) if mode == "Encode" else decryptMorse(text)

        elif cipher == "Binary":
            result = encryptBinary(text) if mode == "Encode" else decryptBinary(text)

        elif cipher == "Hex":
            result = encryptHEX(text) if mode == "Encode" else decryptHEX(text)

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
root.title("ARGToolBox Encoder/Decoder")
root.geometry("600x550")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# --- Mode Selection ---
mode_frame = tk.LabelFrame(root, text="Mode", padx=10, pady=10, font=("Arial", 10, "bold"))
mode_frame.pack(fill="x", padx=15, pady=10)

mode_var = tk.StringVar(value="Decode")
tk.Radiobutton(mode_frame, text="Decode", variable=mode_var, value="Decode", font=("Arial",10)).pack(side="left", padx=5)
tk.Radiobutton(mode_frame, text="Encode", variable=mode_var, value="Encode", font=("Arial",10)).pack(side="left", padx=5)

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

# --- Run Button (Encode/Decode) ---
run_button = tk.Button(root, text="Run", command=run_cipher, font=("Arial", 12, "bold"),
                       bg="#4CAF50", fg="white", relief="raised", padx=10, pady=5)
run_button.pack(pady=10)

# --- Output Frame ---
output_frame = tk.LabelFrame(root, text="Output", padx=10, pady=10, font=("Arial", 10, "bold"))
output_frame.pack(fill="both", padx=15, pady=10, expand=True)

output_text = tk.Text(output_frame, height=7, width=70, font=("Arial", 10), wrap="word", state="disabled", bg="#e8e8e8")
output_text.pack(fill="both", expand=True)

root.mainloop()
