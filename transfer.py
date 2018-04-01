# This file transfers new entries from "TO BE TRANSFERRED.txt" to the encrypted log
# Beware, harmful side effects may occur. Ensure you've backed up all your data.
# Import textcrypt if it exists or use included library if not
try:
    from textcrypt import *
    encrypter = textcrypt.Encrypt()
except:
    from encryption import *
    encrypter = encryption()
import sys
import getpass

# Decrypte passwords for now
print "Enter your original encryption key: "
key = encrypter.padKey( getpass.getpass() )
secondText = encrypter.padKey(getpass.getpass("Re-enter Password: "))
if not key == secondText:
    print "Your keys don't match. Aborting!"
    sys.exit()

cipherFile = open("c0d3sC1ph3r.txt", 'r')
cipherText = cipherFile.read()
plainText = encrypter.decrypt(cipherText, key)

# Now write contents to the plain password files as a backup
plainFile = open("c0d3sPl41n.txt", 'w')
plainFile.write(plainText)

# Now add TO BE TRANSFERRED.txt contents
lines = plainText.split('\n')
toAddFile = open("TO BE TRANSFERRED.txt", 'r')
toAddText = toAddFile.read()
# I can simply insert irregardless of lines
lines.insert(len(lines)-2, toAddText)

# Now add updated plain text
plainText = ""
for i in lines:
    plainText += i + '\n'

# Now encrypt everything
cipherText = encrypter.encrypt(plainText, key)

cipherFile = open("c0d3sC1ph3r.txt", 'w')
cipherFile.write(cipherText)
