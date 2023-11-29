# Morse Code Encryptor/Decryptor

## Introduction

This Python application allows users to encrypt and decrypt messages using Morse code. Morse code is a method of encoding text characters using sequences of dots and dashes to represent letters, numerals, and punctuation.

The application provides two main functionalities:
- *Encryption*: Converts plain text messages into Morse code.
- *Decryption*: Converts Morse code messages back into plain text.

## How it Works

The application utilizes a predefined Morse code mapping, where each character is associated with its Morse code equivalent. The mappings include letters (A-Z), numbers (0-9), and some common punctuation marks. The encryption function takes a plain text message as input, converts it to uppercase, and then looks up the Morse code for each character in the mapping. The decrypted function reverses this process, mapping Morse code back to the original characters.

## Instructions

### Encryption

To encrypt a message, call the `encrypt` function in the `MorseCode` module, passing the plain text message as an argument.

Example:
```python
from MorseCode import encrypt

message = "HELLO"
encrypted_message = encrypt(message)
print(encrypted_message)
```
### Decryption

To decrypt a Morse code message, use the `decrypt` function provided by the `MorseCode` module. This function takes a Morse code message as input and returns the corresponding plain text.

Example:
```python
from MorseCode import decrypt

encrypted_message = "... --- ..."
decrypted_message = decrypt(encrypted_message)
print(decrypted_message)

```

## Unit Tests

| Test Case                             | Input Message                         | Expected Output                                                      |
|----------------------------------------|---------------------------------------|----------------------------------------------------------------------|
| test_encryption_single_word            | `ALHOSSAIN`                          | `.‐ .‐.. .... --- ... ... .‐ .. ‐.`                                  |
| test_encryption_multiple_words         | `ALHOSSAIN HABIBI WEH REGOULA`       | `.‐ .‐.. .... --- ... ... .‐ .. ‐. / .... .‐ ‐... .. ‐... .. / ...‐ . .... / .-. . ‐‐. --- ..- .-.. .‐` |
| test_encryption_single_word_with_numbers| `ALHOSSAIN333`                       | `.‐ .‐.. .... --- ... ... .‐ .. ‐. ...‐ ...‐ ...‐`              |
| test_encryption_single_word_with_space_and_numbers | `ALHOSSAIN333 456`          | `.‐ .‐.. .... --- ... ... .‐ .. ‐. ...‐ ...‐ ...‐ / ....‐ ..... ‐....`          |
| test_encryption_single_word_lowercase  | `alhossain`                          | `.‐ .‐.. .... --- ... ... .‐ .. ‐.`                                  |
| test_encryption_combination            | `ALHOSSAIN habibi WEH REGOULA333 456` | `.‐ .‐.. .... --- ... ... .‐ .. ‐. / .... .‐ ‐... .. ‐... .. / .‐‐ ‐.... / .-. . ‐‐. --- ..- .-.. .‐ ...‐ ...‐ ...‐ / ....‐ ..... ‐....` |
| test_decrypt_numbers                   | `.---- ..--- ...-- ....- .....`      | `12345`                                                              |
| test_decrypt_special_characters        | `!@#$%`                               | ``                                                                   |
| test_decrypt_single_word               | `.... . .‐.. .‐.. ‐‐‐`                | `HELLO`                                                              |
| test_decrypt_multiple_words            | `.‐ .‐.. .... --- ... ... .‐ .. ‐. / .‐‐‐ --- .-. .‐.. ‐..` | `ALHOSSAIN WORLD`                                       |
| test_decrypt_lowercase                 | `.... . .‐.. .‐.. ‐‐‐`                | `HELLO`                                                              |