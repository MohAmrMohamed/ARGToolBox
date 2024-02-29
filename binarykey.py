# This function will turn the input binary text into a utf-8 encoded output 

def binaryToText(binary):
    try:
        # Each byte will be split and spaces will be removed
        binaryList = binary.split()
        # initalizing list to add converted words into
        completeText = []
        # For loop that converts each byte then adds them to the list
        for byte in binaryList:
            letter = str(chr(int(byte, 2)))
            completeText.append(letter)
        # Converts the list into one string
        string = ''.join(completeText)
        return(string)

    except ValueError:
        print('That is not binary')

    except AttributeError:
        print('That is not binary')

    
