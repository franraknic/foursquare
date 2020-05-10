#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
description:

Four-Square Cipher algorithm
https://en.wikipedia.org/wiki/Four-square_cipher

author: Fran Raknić fraknic@tvz.hr

"""
import random


class FourSquare:

    def __init__(self):
        self.allowed_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'm', 'o', 'p', 'q', 'r', 's',
                              't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphabet = [
            ["a","b","c","d","e"],
            ["f","g","h","i","k"],
            ["l","m","n","o","p"],
            ["q","r","s","t","u"],
            ["v","w","x","y","z"]
        ]

        self.alpha_table1 = self.alphabet
        self.alpha_table2 = self.alphabet

    def encrypt(self, plain_text, key_matrix1, key_matrix2):

        plain_text = plain_text.replace(" ", "")
        if len(plain_text) % 2 is not 0:
            plain_text = plain_text + "x"
        plain_text = " ".join(plain_text[i:i+2] for i in range(0, len(plain_text), 2))
        print("Encrypting : ", plain_text)
        plain_text_bigrams = plain_text.split()

        cipher_text = list()


        for bigram in plain_text_bigrams:
            indx1 = self.get_char_index(bigram[0], self.alpha_table1)
            indx2 = self.get_char_index(bigram[1], self.alpha_table2)

            c1 = key_matrix1[indx1[0]][indx2[1]]
            c2 = key_matrix2[indx2[0]][indx1[1]]

            cipher_text.append((c1, c2))

        return cipher_text

    def decrypt(self, cipher_text, key_matrix1, key_matrix2):

        cipher_text = cipher_text.replace(" ", "")
        if len(cipher_text) % 2 is not 0:
            cipher_text = cipher_text + "x"
        cipher_text = " ".join(cipher_text[i:i+2] for i in range(0, len(cipher_text), 2))
        print("Decrypting : ", cipher_text)
        cipher_text_bigrams = cipher_text.split()

        plain_text = list()

        for bigram in cipher_text_bigrams:
            indx1 = self.get_char_index(bigram[0], key_matrix1)
            indx2 = self.get_char_index(bigram[1], key_matrix2)

            c1 = self.alpha_table1[indx1[0]][indx2[1]]
            c2 = self.alpha_table2[indx2[0]][indx1[1]]

            plain_text.append((c1, c2))

        return plain_text

    def generate_cipher_alpha(self):
        """ Generates a 5x5 matrix of non-repeating characters """

        random_alpha = list()
        random_ints = random.sample(range(0, 25), 25)
        cipher = list()

        for n in random_ints:
            random_alpha.append(self.allowed_chars[n])

        cipher.append(random_alpha[0:5])
        cipher.append(random_alpha[5:10])
        cipher.append(random_alpha[10:15])
        cipher.append(random_alpha[15:20])
        cipher.append(random_alpha[20:25])

        return cipher

    def get_char_index(self, letter, matrix):
        r, c = 0, 0
        for row in matrix:
            for chr in row:
                if chr == letter:
                    return r, c
                c += 1
            r += 1
            c = 0


if __name__ == '__main__':

    fs = FourSquare()

    # Generate 5x5 key matrixes
    k1 = fs.generate_cipher_alpha()
    k2 = fs.generate_cipher_alpha()

    print("Key matrix 1: ", k1)
    print("Key matrix 2: ", k2)

    # Encryption algorithm
    cipher_text = fs.encrypt("attack at dawn", k1, k2)
    print("Ciphertext for 'attack at dawn' : ", cipher_text)

    # Decryption algorithm
    cipher_string = [''.join(pair) for pair in cipher_text]
    cipher_string = ''.join(cipher_string)
    plain_text = fs.decrypt(cipher_string, k1, k2)
    print("Plaintext for '", cipher_string, "'", plain_text)

