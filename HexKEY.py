def decryptHEX(text):
    decoded = bytes.fromhex(text.replace(" ", "")).decode("utf-8")
    return decoded


