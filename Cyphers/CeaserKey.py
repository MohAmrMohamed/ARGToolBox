def decryptCeaser(text, shift): 
    Charachters = list(text.upper())
    decrypted = ""
    for char in Charachters:
        if char.isalpha():
            current = ord(char)
            updated = (ord(char) - 65 - shift) %26 +65
            letter = chr(updated)
            decrypted += letter
        else:
            decrypted += char
    return decrypted

# Need to fix spaces and special charachters