Morse_code_mapping = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-', ' ':'/'}




def encrypt(plain_message):
    # plain_message.upper convert all charecters to upper case
    plain_message = plain_message.upper()
    encryptedMessage = []
    for plainChar in plain_message:
       # to check if that charecter is in our predefined dict
        if plainChar in Morse_code_mapping:
            morseCode = Morse_code_mapping.get(plainChar)
            encryptedMessage.append(morseCode)
    # convert encryptedMessage array into string
    encryptedMessegeString = ' '.join(encryptedMessage)
    print(encryptedMessegeString)
    return encryptedMessegeString


def decrypt(encrypted_message):
    # convert encrypted_message string into array
    morse_codes = encrypted_message.split(' ')
    decrypted_message = []
    # Iterate through each Morse code in the input message
    for code in morse_codes:
        # Iterate through the Morse code mapping to find the corresponding character
        for char, morse_code in Morse_code_mapping.items():
            if code == morse_code:
                decrypted_message.append(char)
    # Join the decrypted characters to form the final decrypted message
    decryptedmessegeString = ''.join(decrypted_message)
    print(decryptedmessegeString)
    return decryptedmessegeString









