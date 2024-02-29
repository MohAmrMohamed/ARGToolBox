# Import the base64 module and alias it as b64 for ease
import base64 as b64

# Define a class called Base64Encoder
class Base64Encoder:

    def __init__(self, data):
        self.data = data  # Store the input data in an instance variable
    
    def encodeBase64(self):
        encoded = b64.b64encode(
            self.data.encode('utf-8'))
        # Convert the encoded bytes to a string and return it
        return encoded.decode('utf-8')  
    
    def decodeBase64(self):
        # Remove any leading or trailing whitespace from the input string
        cleaned_data = self.data.strip()
        
        try:
            # Attempt to decode the Base64-encoded data using urlsafe_b64decode
            decoded = b64.urlsafe_b64decode(cleaned_data)
            # Decode the resulting bytes to a string and return it
            return decoded.decode('utf-8')  
        except b64.binascii.Error as e:
            return 'already decoded'


