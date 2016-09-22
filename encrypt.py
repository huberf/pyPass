from encryption import *
import sys
import getpass

encrypter = encryption()

firstText = getpass.getpass()
secondText = getpass.getpass("Re-enter Password: ")

if firstText == secondText:
  key = encrypter.padKey( firstText )
else:
  print "Inputs didn't match."
  sys.exit()

plainFile = open("c0d3sPl41n.txt", 'r')
plainText = plainFile.read()

cipherText = encrypter.encrypt(plainText, key)

cipherFile = open("c0d3sC1ph3r.txt", 'w')
cipherFile.write(cipherText)
