
def ceasar_cipher_main(word, num):
  word = word.upper()
  new_word = ""
  num = num % 26
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  for letter in word:
    if letter in alpha:
      new_word = new_word + alpha[(alpha.index(letter) + num) % 26]
    else:
      new_word = new_word + letter

  return new_word

def encipher(word, num): return ceasar_cipher_main(word, -num)

def decipher(word, num): return ceasar_cipher_main(word, num)

while True:
    print("Type E if you wish to encrypt a phrase.")
    print("Type D if you wish to decrypt a phrase.")
    print("Type Q if you wish to quit.")
    choice = input(">>>")

    if choice == "E":
        text = input("Please enter the text you wish to encrypt on one line.\n>>>")
        
        while True:
          shift = input("Please enter the shift.\n>>>")
          if shift.isnumeric():
            shift = int(shift)
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
          shift = input("Please enter the shift.\n>>>")
          if shift.isnumeric():
            shift = int(shift)
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
