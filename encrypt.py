from encryption import *
encrypter = encryption()

key = encrypter.padKey( raw_input("Key: ") )

plainFile = open("c0d3sPl41n.txt", 'r')
plainText = plainFile.read()

cipherText = encrypter.encrypt(plainText, key)

cipherFile = open("c0d3sC1ph3r.txt", 'w')
cipherFile.write(cipherText)
