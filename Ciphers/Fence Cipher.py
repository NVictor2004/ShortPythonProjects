
def remove(text):
    alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    new = ""
    for letter in text:
        if letter in alpha:
            new = new + letter
    return new

def encode(string, n):
    data = [""] * n
    add = 1
    index = 0
    for i in string:
        data[index] = data[index] + i
        index = index + add
        if not (0 <= index < n):
            add = -add
            index = index + add + add
    return "".join(data)
    
def decode(string, n):
    numbers = [i for i in range(len(string))]
    data = [[0]] * n
    add = 1
    index = 0
    for i in numbers:
        data[index] = data[index] + [i]
        index = index + add
        if not (0 <= index < n):
            add = -add
            index = index + add + add
    data = [i[1:] for i in data]
    new = []
    for i in data:
        new = new + i
    data = new
    new = ""
    for i in range(len(string)):
        index = data.index(i)
        new = new + string[index]
    return new

while True:
    print("Type E if you wish to encrypt a phrase.")
    print("Type D if you wish to decrypt a phrase.")
    print("Type Q if you wish to quit.")
    choice = input(">>>")

    if choice == "E":
        text = remove(input("Please enter the text you wish to encrypt on one line.\n>>>"))
        
        while True:
          shift = input("Please enter the number of rails.\n>>>")
          if shift.isnumeric():
            shift = int(shift)
            break
          else:
            print("Invalid input.")
        
        print()
        print("Your ciphertext:")
        print(encode(text, shift))
        print()
        print("----------------------------------------------")
        
    elif choice == "D":
        text = remove(input("Please enter the text you wish to decrypt on one line.\n>>>"))
        
        while True:
          shift = input("Please enter the number of rails.\n>>>")
          if shift.isnumeric():
            shift = int(shift)
            break
          else:
            print("Invalid input.")
          
        print()
        print("Your plaintext:")
        print(decode(text, shift))
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
