#!/usr/bin/env python3
import pyzipper

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']', '|', ';', ':', '"', "'", '<', '>', '?', ',', '.', '/', '`', '~']
known_password_dict = {'n':1, '_':2, '^':3, '`':5, 'W':6, '5':8}


password_combinations = []
for char1 in characters:
    for char2 in characters:
        password_combinations.append(char1 + char2)


for combination in password_combinations:
    password = 'n_^{}`W{}5'.format(combination[0], combination[1])
    try:
        with pyzipper.AESZipFile('The_secret.zip') as zf:
            zf.pwd = password.encode()
            zf.extractall(pwd=password.encode())
            print('Password found:', password)
            break
    except RuntimeError:
        continue
