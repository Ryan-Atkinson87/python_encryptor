# string_encryptor.py

from phonetic_alphabet_dict import alphabet

def encryptor():
    cypher_script = ''
    for letter in message:
        phonetic = alphabet[letter]
        last = phonetic[-1]
        cypher_script = cypher_script + last + str(len(alphabet[letter]))
    print(cypher_script)
"""
This needs finishing
def decryptor():
    phonetic_keys = list(alphabet)
    decryptor_dict = {}
    for key in phonetic_keys:
        decryptor_dict[] = 
"""    
                                                              

message = input('Please enter the message you would like to encrypt: ')

encryptor()

encrypted = input(' Please enter the message you would like to decrypt: ')

