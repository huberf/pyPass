from encryption import *
import getpass
import sys

encrypter = encryption()

firstText = getpass.getpass()
secondText = getpass.getpass("Re-enter Password:")

if firstText == secondText:
  key = encrypter.padKey( firstText )
else:
  print "Inputs didn't match."
  sys.exit()

cipherFile = open("c0d3sC1ph3r.txt", 'r')
cipherText = cipherFile.read()
plainText = encrypter.decrypt(cipherText, key)
plainFile = open("c0d3sPl41n.txt", 'w')
plainFile.write(plainText)
