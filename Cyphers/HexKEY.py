def decryptHEX(text):
    try:
        decoded = bytes.fromhex(text.replace(" ", "")).decode("utf-8")
        return decoded
    except Exception:
        return "Error: Invalid hex input"


