import string

script = string.printable

def encry(text):
    global script

    key = int(input("Enter your key   : "))
    cipher = ""
    for x in text:
        if x in script:
            y = script.find(x)
            y = (y + key)%100
            cipher = cipher+script[y]
        else:
            cipher = cipher + x
        
    return cipher

def decry(cipher):
    global script

    key = int(input("Enter your key   : "))
    text = ""
    for x in cipher:
        if x in script:
            y = script.find(x)
            y = (y - key)%100
            text = text + script[y]
        else:
            text = text + x
        
    return text


if __name__ == "__main__":
    print(30*"=")
    print("1. Encryption\n2. Decryption")
    print(30*"=")

    option = int(input("Choice Mode  : "))

    if option == 1:
        text = input("Enter text (PlainText) : ")
        print(encry(text))
    elif option == 2:
        cipher = input("Enter text (CipherText) : ")
        print(decry(cipher))
    else:
        print("Enter options 1 or 2....")

    