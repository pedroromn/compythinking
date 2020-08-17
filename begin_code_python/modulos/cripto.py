def encrypt():
    """
    Function: encrypt
    """
    plainText = input("\nEnter a one-word, lowercase message: ")
    distance = int(input("Enter the distance value: "))
    code = ""
    for ch in plainText:
        ordvalue = ord(ch)
        cipherValue = ordvalue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                            (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
    print(code)


def decrypt():
    """
    Function: decrypt
    """
    code = input("\nEnter the code text: ")
    distance = int(input("Enter the distance value: "))
    plainText = ""
    for ch in code:
        ordvalue = ord(ch)
        cipherValue = ordvalue - distance
        if cipherValue < ord('a'):
            cipherValue = ord('z') - \
                    (distance - (ord('a') - ordvalue - 1))
        plainText += chr(cipherValue)
    print(plainText)


def crypto_test():
    encrypt()
    print('-'*50, end="\n")
    decrypt()