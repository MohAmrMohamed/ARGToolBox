import base64

def decryptBASE64(text):
    decoded = base64.b64decode(text)
    decodedLine = decoded.decode('utf-8') 
    return decodedLine

