# This dictionary holds all morse code definitions
morseCodeDict = {
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
    '-....-': '-', '-.--.': '(', '-.--.-': ')', '.----.': '\'',
    '-.-.--': '!', '-...-': '=', '.-.-.': '+', '.-..-.': '"',
    '---...': ':', '-.-.-.': ';', '.-...': '&', '-...-': '=',
    '-.--.': '@', '...-..-': '$'
}


def morseCodeConverter(code):
    words = code.split('   ') # Split the input when there are 3 spaces
    decodedMessage = [] 
    for word in words:
        letters = word.split(' ') # Splits letters when there is a space
        decodedWord = ''
        for letter in letters:
            if letter in morseCodeDict: # Checks if code is in dict
                decodedWord += morseCodeDict[letter] # Adds to the message
        decodedMessage.append(decodedWord) 
    finalMessage = ' '.join(decodedMessage) # Converts the list into a string
    return finalMessage

