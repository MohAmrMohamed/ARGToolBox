import base64

def decryptBASE64(text):
    try:
        decoded = base64.b64decode(text)
        decodedLine = decoded.decode('utf-8') 
        return decodedLine
    except:
        return "Error: Invalid Base64 input"

