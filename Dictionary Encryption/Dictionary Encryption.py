plaintext = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Etext = list('RZAQJPYDKFIXOSWBLHEVNTGMCU')

def messageEnc(text,plain, encryp):
    dictionary = dict(zip(plain, encryp))
    newmessage = ''
    for char in text:
        try:
            newmessage = newmessage + dictionary[char.upper()]
        except:
            newmessage += ''
    print(text,'has been encryptd to:',newmessage)

def messageDec(text,encryp, plain):
    dictionary = dict(zip(encryp,plain))
    #print(dictionary)
    newmessage = ''
    for char in text:
        try:

            newmessage = newmessage + dictionary[char.upper()]

        except:
            newmessage += ''
    print(text,'has been Decrypted to:',newmessage)


while True:
    print("""
       Simple Dictionary Encryption :
       Press 1 to Encrypt
       Press 2 to Decrypt
       """)
    try:
        choose = int(input())
    except:
        print("Press Either 1 or 2")
        continue

    if choose == 1:

        text = str(input("enter something: "))
        messageEnc(text,plaintext,Etext)
        continue
    else:
        text = str(input("enter something: "))
        messageDec(text,Etext,plaintext)





