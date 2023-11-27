from MorseCode import encrypt
import unittest


class MyTestCase(unittest.TestCase):
    def test_encryption_single_word(self):
        messege = 'ALHOSSAIN'
        expected = '.- .-.. .... --- ... ... .- .. -.'
        actual = encrypt(messege)
        self.assertEqual(expected, actual)  # add assertion here

    def test_encryption_multiple_words(self):
        messege = 'ALHOSSAIN HABIBI WEH REGOULA'
        expected = '.- .-.. .... --- ... ... .- .. -. / .... .- -... .. -... .. / .-- . .... / .-. . --. --- ..- .-.. .-'
        actual = encrypt(messege)
        self.assertEqual(expected, actual)

    def test_encryption_single_word_with_numbers(self):
        messege = 'ALHOSSAIN333'
        expected = '.- .-.. .... --- ... ... .- .. -. ...-- ...-- ...--'
        actual = encrypt(messege)
        self.assertEqual(expected, actual)

    def test_encryption_single_word_with_space_and_numbers(self):
        messege = 'ALHOSSAIN333 456'
        expected = '.- .-.. .... --- ... ... .- .. -. ...-- ...-- ...-- / ....- ..... -....'
        actual = encrypt(messege)
        self.assertEqual(expected, actual)

    def test_encryption_single_word_lowercase(self):
        messege = 'alhossain'
        expected = '.- .-.. .... --- ... ... .- .. -.'
        actual = encrypt(messege)
        self.assertEqual(expected, actual)

    def test_encryption_single_word(self):
        messege = 'ALHOSSAIN habibi WEH REGOULA333 456'
        expected = '.- .-.. .... --- ... ... .- .. -. / .... .- -... .. -... .. / .-- . .... / .-. . --. --- ..- .-.. .- ...-- ...-- ...-- / ....- ..... -....'
        actual = encrypt(messege)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()










