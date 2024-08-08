
from re import search
from time import time
import numpy as np

def create_answer(data):
    answer = [0] * 81
    for index in range(81):
        for number in range(1, 10):
            if (2 ** index & data[number]):
                answer[index] = number
                break
    new = []
    start = 0
    for i in range(9):
        new.append("".join(list(map(str, answer[start:start + 9]))))
        start = start + 9

    return new

def valid(array):
    compare = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(9):
        row = array[i]
        column = array[:, i]
        row = [i for i in row if i != 0]
        column = [i for i in column if i != 0]
        if len(set(row)) != len(row) or len(set(column)) != len(column):
            return False
    
    for first in range(0, 9, 3):
        for second in range(0, 9, 3):
            three = array[first:first + 3, second:second + 3]
            three = three.reshape(9,)
            three = [i for i in three if i != 0]
            if len(set(three)) != len(three):
                return False
    
    return True

def sudoku(data, number):

    hori = ((7, 56, 448), (3584, 28672, 229376), (1835008, 14680064, 117440512), (939524096, 7516192768, 60129542144), (481036337152, 3848290697216, 30786325577728), (246290604621824, 1970324836974592, 15762598695796736), (126100789566373888, 1008806316530991104, 8070450532247928832), (64563604257983430656, 516508834063867445248, 4132070672510939561984), (33056565380087516495872, 264452523040700131966976, 2115620184325601055735808))
    vert = ((262657, 35253225783296, 4731607869305009471488), (525314, 70506451566592, 9463215738610018942976), (1050628, 141012903133184, 18926431477220037885952), (2101256, 282025806266368, 37852862954440075771904), (4202512, 564051612532736, 75705725908880151543808), (8405024, 1128103225065472, 151411451817760303087616), (16810048, 2256206450130944, 302822903635520606175232), (33620096, 4512412900261888, 605645807271041212350464), (67240192, 9024825800523776, 1211291614542082424700928))

    if 2 ** number & data[0]:
            
        row, column = number // 9, number % 9
        
        coeff_row, coeff_column = row // 3, column // 3
        new_coeff_row = coeff_row * 3
        
        mask = hori[new_coeff_row][coeff_column] + hori[new_coeff_row + 1][coeff_column] + hori[new_coeff_row + 2][coeff_column] + hori[row][0] + hori[row][1] + hori[row][2] - hori[row][coeff_column] + vert[column][0] + vert[column][1] + vert[column][2] - vert[column][coeff_row]

        numbers = [i for i in range(1, 10) if not (data[i] & mask)]

        data[0] = data[0] - 2 ** number

        a = len(numbers) - 1

        while a >= 0:
            i = numbers[a]
            data[i] = data[i] + 2 ** number
            possi = sudoku(data, number + 1)
            if possi: return possi
            data[i] = data[i] - 2 ** number
            a = a - 1
            
        data[0] = data[0] + 2 ** number

    elif number != 81:
        return sudoku(data, number + 1)
    else:
        return data


puzzle = []
data = [0] * 10
pattern = r"^[0-9]{9}$"
for i in range(1, 10):
    while True:
      row = input("Please enter row " + str(i) + ": ")
      if search(pattern, row):
        row = list(map(int, list(row)))
        puzzle = puzzle + row
        break
      else:
        print("Invalid input.")

if valid(np.array(puzzle).reshape(9, 9)): 
    for i in range(81):
        data[puzzle[i]] = data[puzzle[i]] + 2 ** i

    print("Starting now...")

    answer = sudoku(data, 0)

    if answer == None:
        print("No solution.")
    else:
        answer = create_answer(answer)
        for i in answer:
            print(i)
        print("Done!")
else:
    print("Invalid Puzzle.")













