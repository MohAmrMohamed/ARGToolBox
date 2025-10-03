def decryptROT13(text): 
    Charachters = list(text.upper())
    decrypted = ""
    for char in Charachters:
        current = ord(char)
        updated = (ord(char) - 65 - 13) %26 +65
        letter = chr(updated)
        decrypted += letter
    return decrypted

# Need to fix spaces and special charachters