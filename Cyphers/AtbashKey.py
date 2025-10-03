def decryptAtbash(text): 
    Charachters = list(text.upper())
    decrypted = ""
    for char in Charachters:
        current = ord(char)
        updated = 25 - (ord(char) - 65) %26 + 65
        letter = chr(updated)
        decrypted += letter
    return decrypted
