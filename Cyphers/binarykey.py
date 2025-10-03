def decryptBinary(text): 
    try:
        Charachters = text
        chunks = Charachters.split()
        decrypted = ""
        for chunk in chunks:
            num = int(chunk, 2)
            letter = chr(num)
            decrypted += letter
        return decrypted
    except ValueError:
        return "Error: Invalid binary input"
    
def encryptBinary(text):
    try:
        return ' '.join(format(ord(c), '08b') for c in text)
    except Exception as e:
        return f"Error: {e}"
 