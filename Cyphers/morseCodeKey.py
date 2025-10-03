import re

MORSE_TO_TEXT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D',
    '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-..-.': '/',
    '-....-': '-', '-.--.': '(', '-.--.-': ')', '.----.': "'",
    '-.-.--': '!', '-...-': '=', '.-.-.': '+', '.-..-.': '"',
    '---...': ':', '-.-.-.': ';', '.-...': '&', '-.--.': '@',
    '...-..-': '$'
}

def decryptMorse(text):
    try:
        text = re.sub(r"\s{2,}", "   ", text)
        words = text.split("   ")
        decrypted = ""
        for word in words:
            chunks = word.split(" ")
            for chunk in chunks:
                if chunk in MORSE_TO_TEXT:
                    letter = MORSE_TO_TEXT[chunk]
                    decrypted += letter
                else:
                    decrypted += "?"  
            decrypted += " "
        return decrypted.strip()
    except Exception as e:
        return f"An error occurred: {e}"
