from src.hackkerank.ceasar_cipher import * 

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_middle_Outz_in_caesarcipher(self):
        x = 'middle-Outz'
        result = caesarCipher(x,2)
        self.assertEqual(result,'okffng-Qwvb')
    def test_Hello_World_in_caesarcipher(self):
        x = 'Hello_World!'
        result = caesarCipher(x,4)
        self.assertEqual(result,'Lipps_Asvph!')
    def test_Ciphering_in_caesarcipher(self):
        x = 'Ciphering.'
        result = caesarCipher(x,26)
        self.assertEqual(result,'Ciphering.')
    def test_D3q4_in_caesarcipher(self):
        x = 'D3q4'
        result = caesarCipher(x,0)
        self.assertEqual(result,'D3q4')
    def test_Always_Look_on_the_Bright_Side_of_Life_in_caesarcipher(self):
        x = 'Always-Look-on-the-Bright-Side-of-Life'
        result = caesarCipher(x,5)
        self.assertEqual(result,'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj')
if __name__ == '__main__':
    unittest.main()