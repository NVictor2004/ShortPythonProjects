

def cipher(text, number, key):
    text = text.upper()
    key = key.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new = ""
    add = 0
    for i in range(len(text)):
        if text[i] in alphabet:
            key_letter = key[(i - add) % len(key)]
            index = (alphabet.index(text[i]) + (alphabet.index(key_letter) * number)) % 26
            new = new + alphabet[index]
        else:
            new = new + text[i]
            add = add + 1
    return new

def encipher(text, key): return cipher(text, 1, key)

def decipher(text, key): return cipher(text, -1, key)

while True:
    print("Type E if you wish to encrypt a phrase.")
    print("Type D if you wish to decrypt a phrase.")
    print("Type Q if you wish to quit.")
    choice = input(">>>")

    if choice == "E":
        text = input("Please enter the text you wish to encrypt on one line.\n>>>")
        
        while True:
          shift = input("Please enter the key.\n>>>")
          if shift.isalpha():
            break
          else:
            print("Invalid input.")
        
        print()
        print("Your ciphertext:")
        print(encipher(text, shift))
        print()
        print("----------------------------------------------")
        
    elif choice == "D":
        text = input("Please enter the text you wish to decrypt on one line.\n>>>")
        
        while True:
          shift = input("Please enter the key.\n>>>")
          if shift.isalpha():
            break
          else:
            print("Invalid input.")
          
        print()
        print("Your plaintext:")
        print(decipher(text, shift))
        print()
        print("----------------------------------------------")
        
    elif choice == "Q":
        print()
        print("Goodbye!")
        break
    
    else:
        print()
        print("Invalid input.")
        print()
