# string_encryptor.py

from phonetic_alphabet_dict import alphabet

def encryptor():
    cypher_script = ''
    for letter in message:
        phonetic = alphabet[letter]
        last = phonetic[-1]
        second = phonetic[1]
        cypher_script = cypher_script + last + second + str(len(alphabet[letter]))
    print('The encrypted message is: ', cypher_script)
    # need to add part that allows punctuation

def decryptor():
    phonetic_keys = list(alphabet)
    decryptor_dict = {}
    for key in phonetic_keys:
        phonetic = alphabet[key]
        last = phonetic[-1]
        second = phonetic[1]
        decryptor_dict[key] = last + second + str(len(alphabet[key]))

    decryptor_lst = list(decryptor_dict)
    temp_str = encrypted
    to_decrypt = ''
    decrypted = ''
    while len(temp_str) > 0:
        first = temp_str[0]
        second = temp_str[1]
        third = temp_str[2]
        to_decrypt = first + second + third
        letter = first + second + third
        temp_str = temp_str.replace(letter, '', 1)
        counter = 0
        for key in decryptor_lst:
            if decryptor_dict[key] == to_decrypt:
                decrypted = decrypted + decryptor_lst[counter]
            counter = counter + 1
    print('The original message was: ', decrypted)
            


exit = False
while exit == False:
    user_input = input('To encrypt a message type "e", to decrypt a message type "d" or to exit type "x": ')
    if user_input == 'e':
        message = input('Please enter the message you would like to encrypt: ')

        encryptor()

        
    elif user_input == 'd':
        encrypted = input(' Please enter the message you would like to decrypt: ')

        decryptor()
    elif user_input == 'x':
        exit = True
    else:
        print('You must enter "e", "d" or "x"')
