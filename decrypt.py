from encryption import *
encrypter = encryption()

key = encrypter.padKey( raw_input("Key: ") )

cipherFile = open("c0d3sC1ph3r.txt", 'r')
cipherText = cipherFile.read()
plainText = encrypter.decrypt(cipherText, key)
plainFile = open("c0d3sPl41n.txt", 'w')
plainFile.write(plainText)
