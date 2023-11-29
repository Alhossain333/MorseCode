from MorseCode import encrypt, decrypt
if __name__ == '__main__':
    message = 'Hi how are you?'
   # assign encrypt() output to encrypted_message variable
    encrypted_message = encrypt(message)
    print("Encrypted message:", encrypted_message)

    # assign decrypt() output to decrypted_message variable
    decrypted_message = decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)





