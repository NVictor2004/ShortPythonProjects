import math
import random
import numpy

def fitness_level_using_quadgrams(cipher_text, numbers):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #cipher_text has no spaces and no non-letters!
    sum1 = 0
    for i in range(len(cipher_text) - 4):
        term = cipher_text[i: i + 4]
        a, b, c, d = alpha.index(term[0]), alpha.index(term[1]), alpha.index(term[2]), alpha.index(term[3])
        sum1 = sum1 + numbers[a][b][c][d]
    return sum1 / 0.95

def decipher(cipher_text, cipher_alphabet):
    new = ""
    for i in cipher_text:
        num = cipher_alphabet.index(i)
        new = new + chr(65 + num)
    return new

def random_alphabet():
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
    new = ""
    num = 26
    for i in range(26):
        while alphabet[num] == " ":
            num = random.randint(0, 26)
        new = new + alphabet[num]
        alphabet[num] = " "
    return new

def swap_two(cipher_alphabet):
    num1, num2 = 0, 0
    while num2 == num1:
        num1 = random.randint(0, 25)
        num2 = random.randint(0, 25)
    cipher_alphabet = list(cipher_alphabet)
    cipher_alphabet[num1], cipher_alphabet[num2] = cipher_alphabet[num2], cipher_alphabet[num1]
    return "".join(cipher_alphabet)

def remove(text):
    alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    new = ""
    for letter in text:
        if letter in alpha:
            new = new + letter
    return new

def SA(text, limit, T):
    takeaway = T / limit
    cipher_text = remove(text.upper())

    numbers = [[[[-10.0] * 26] * 26] * 26] * 26

    file = open("quadgrams.txt", "r")
    data = []
    for line in list(file):
        data.append(line.split(","))
    file.close()
    numbers = numpy.array(numbers)

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for line in data:
        term = line[0]
        a, b, c, d = alpha.index(term[0]), alpha.index(term[1]), alpha.index(term[2]), alpha.index(term[3])
        numbers[a][b][c][d] = float(line[1].strip("/n"))

    current_alpha = random_alphabet()
    current_goodness = fitness_level_using_quadgrams(decipher(cipher_text, current_alpha), numbers)
    while limit > 0:
        new_alpha = swap_two(current_alpha)
        new_goodness = fitness_level_using_quadgrams(decipher(cipher_text, new_alpha), numbers)
        chance = math.exp((new_goodness - current_goodness) / T)           
        if new_goodness > current_goodness or random.random() < chance:
            current_alpha = new_alpha
            current_goodness = new_goodness
        limit = limit - 1
        T = T - takeaway
    print()
    print("Current Alphabet:", current_alpha)
    print("Current Plaintext:\n" + decipher(cipher_text, current_alpha))


print("Please enter the text you wish to decrypt on one line.")
print("At least 1200 characters is recommended.")
print("NOTE: All non-alphabetic characters will be removed. All alphabetic characters will be converted to uppercase.")
text = input(">>>")
print()

print("Please enter the total number of iterations.")
print("At least 6000 iterations is recommended.")
while True:
    limit = input(">>>")
    if limit.isnumeric():
        limit = int(limit)
        break
    else:
        print("Invalid input.")
print()

print("Please enter the initial temperature.")
print("A temperature of 60 is recommended.")
while True:
    T = input(">>>")
    if T.isnumeric():
        T = int(T)
        break
    else:
        print("Invalid input.")
print()
print("Calculating plaintext...")
SA(text, limit, T)







    


















    
        

