# Enconding text during the times of Julius Caeser.

# Duplicate the alphabet values because Index Error.
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

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


# Course solution:
def caeser(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
        shiftAmount *= -1
    for char in startText:
        if char in alphabet:
            position = alphabet.index(char)
            newPosition = position + shiftAmount
            endText += alphabet[newPosition]
        else:
            endText += char            
    print(f"The {cipherDirection} text is {endText}")


shouldContinue = True
print(logo + "\n")

while shouldContinue:
    choose = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ")
    shift = int(input("Type the shift number: "))

    # This resolves every number greatest the alphabet list index.
    shift = shift % 26
    caeser(startText=text, shiftAmount=shift, cipherDirection=choose)
    result = input("Type [yes] if you want to go again. Otherwise type [no]: ")
    if result == 'no':
        shouldContinue = False
        print('Goodbye.')


""" My solution:
    # Encoded the text.
def encrypt(plainText, totalShift):
    cipherText = ""
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + totalShift
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is {cipherText}")


    # Decoded the cipherText.
def decrypt(cipherText, totalShift):
    plainText = ""
    for letter in cipherText:
        position = alphabet.index(letter)
        newPosition = position - totalShift
        plainText += alphabet[newPosition]
    print(f"The decoded text is {plainText}")
"""
