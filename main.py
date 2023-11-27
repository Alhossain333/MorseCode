from MorseCode import encrypt, decrypt
if __name__ == '__main__':
    message = 'Hi how are you?'
    encrypted_message = encrypt(message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)





