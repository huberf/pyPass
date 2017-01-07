import re
# Import textcrypt module or local library
try:
    from textcrypt import *
    encrypter = textcrypt.Encrypt()
except:
    from encryption import *
    encrypter = encryption()
import getpass

def search(key, search):
# Authenticate. Beware, no warnings for incorrect password.
    key = encrypter.padKey(key)
    name = search
    passwords = open("c0d3sC1ph3r.txt", 'r')
    cipherText = passwords.read()
    decipheredText = encrypter.decrypt(cipherText, key)
    toReturn = ""
    found = False
    hasRecord = False
    passwords = decipheredText.split("\n")
    # Search through each password record
    for line in passwords:
        matches = re.findall(name, line, re.IGNORECASE)
        isTitle = True
        if line == "" or not line[0] == 'T':
            isTitle = False
        elif line[0] == 'T' and found:
            found = False

        if found:
            toReturn += line + '<br />'

        if matches and isTitle:
            hasRecord = True
            found = True
            toReturn += line + '<br />'

    if not hasRecord:
        toReturn += "No matching entries found!"
    return toReturn
