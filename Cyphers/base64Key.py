import base64

def decryptBASE64(text):
    try:
        decoded = base64.b64decode(text)
        decodedLine = decoded.decode('utf-8') 
        return decodedLine
    except:
        return "Error: Invalid Base64 input"

def encryptBASE64(text):
    try:
        encoded = base64.b64encode(text.encode('utf-8'))  
        return encoded.decode('utf-8')                   
    except Exception as e:
        return f"Error: {e}"

