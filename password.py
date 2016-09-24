import re
try:
    from textcrypt import *
    encrypter = textcrypt.Encrypt()
except:
    from encryption import *
    encrypter = encryption()
import getpass

print "Hello " + getpass.getuser()
key = encrypter.padKey(getpass.getpass())
if True:
    while True:
        passwords = open("c0d3sC1ph3r.txt", 'r')
        cipherText = passwords.read()
        decipheredText = encrypter.decrypt(cipherText, key)
        tmp = open("temp.dat", 'w')
        tmp.write(decipheredText)
        tmp.close()
        passwords = open("temp.dat", 'r')
        line = " "
        decryptLine = ""
        print "Enter the name of the organization or site..."
        name = raw_input("> ")
        found = False
        while not line == "":
                line = passwords.readline()
                matches = re.findall(name, line,re.IGNORECASE)
                isTitle = True
                if line == "" or not line[0] == 'T':
                    isTitle = False
                if matches and isTitle:
                        found = True
                        print line[0:len(line)-1]
                        line = ""
                        # Now iterate, printing each line, until the next entry begins
                        while line == "" or (not line[0] == "T"):
				if not line == "":
	                                print line[0:len(line)-1]
                                line = passwords.readline()

        if not found:
                print "No matching entries found!"

        tmp = open("temp.dat", 'w')
        tmp.write("")
        tmp.close()
else:
    print "Get out of the system hacker!!!!!"


'''
Deprecated but kept for the cool factor

def printDecrypt():
    import string
    output = "decipher = {"
    for i in range(1, len(string.printable)):
        first = string.printable[i]
        second = string.printable[i - 1]
        if first == '\\':
            first =  '\\\\'
        elif first == '\'':
            first = '\\\''
        elif first == '\n':
            first = '\\n'
        elif first == '\t':
            first = '\\t'
        elif first == '\r':
            first = '\\r'
        if second == '\\':
            second = '\\\\'
        elif second == '\'':
            second = '\\\''
        elif second == '\n':
            second = '\\n'
        elif second == '\t':
            second = '\\t'
        elif second == '\r':
            second = '\\r'
    output += "'" + first + "':'" + second + "',"
    output += "'" + string.printable[0] + "':'" + string.printable[len(string.printable) - 1] + "'}"
    print output

decipher = {'1':'0','2':'1','3':'2','4':'3','5':'4','6':'5','7':'6','8':'7',
          '9':'8','a':'9','b':'a','c':'b','d':'c','e':'d','f':'e','g':'f',
          'h':'g','i':'h','j':'i','k':'j','l':'k','m':'l','n':'m','o':'n',
          'p':'o','q':'p','r':'q','s':'r','t':'s','u':'t','v':'u','w':'v',
          'x':'w','y':'x','z':'y','A':'z','B':'A','C':'B','D':'C','E':'D',
          'F':'E','G':'F','H':'G','I':'H','J':'I','K':'J','L':'K','M':'L',
          'N':'M','O':'N','P':'O','Q':'P','R':'Q','S':'R','T':'S','U':'T',
          'V':'U','W':'V','X':'W','Y':'X','Z':'Y','!':'Z','"':'!','#':'"',
          '$':'#','%':'$','&':'%','\'':'&','(':'\'',')':'(','*':')','+':'*',
          ',':'+','-':',','.':'-','/':'.',':':'/',';':':','<':';','=':'<',
          '>':'=','?':'>','@':'?','[':'@','\\':'[',']':'\\','^':']','_':'^',
          '`':'_','{':'`','|':'{','}':'|','~':'}',' ':'~','\t':' ','\n':'\t',
          '\r':'\n','':'\r','':'','0':''}
'''
