def decryptBinary(text): 
    Charachters = text
    chunks = Charachters.split()
    decrypted = ""
    for chunk in chunks:
        num = int(chunk, 2)
        letter = chr(num)
        decrypted += letter
    return decrypted
print(decryptBinary("00110001 00110010 00110011"))