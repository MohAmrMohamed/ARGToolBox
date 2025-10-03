def decryptHEX(text):
    try:
        decoded = bytes.fromhex(text.replace(" ", "")).decode("utf-8")
        return decoded
    except Exception:
        return "Error: Invalid hex input"

def encryptHEX(text):
    try:
        return text.encode('utf-8').hex()
    except Exception as e:
        return f"Error: {e}"
