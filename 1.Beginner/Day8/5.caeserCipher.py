# Enconding text during the times of Julius Caeser.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# Printing the logo.
print(logo + "\n")
choose = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ")
shift = int(input("Type the shift number: "))


# ok
def encrypt(plainText, totalShift):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + totalShift
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is {cipherText}")


cipherText = encrypt(text, shift)


# error.
def decrypt(encryptText, totalShift):
    cipherText = ""
    for letter in encryptText:
        position = alphabet.index(letter)
        newPosition = position - totalShift
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is {cipherText}")


decrypt(cipherText, shift)


# not finish yet