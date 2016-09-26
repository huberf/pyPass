try:
    from textcrypt import *
    encrypter = textcrypt.Encrypt()
except:
    from encryption import *
    encrypter = encryption()
import getpass
import sys

key = encrypter.padKey( getpass.getpass() )

cipherFile = open("c0d3sC1ph3r.txt", 'r')
cipherText = cipherFile.read()
plainText = encrypter.decrypt(cipherText, key)
plainFile = open("c0d3sPl41n.txt", 'w')
plainFile.write(plainText)
