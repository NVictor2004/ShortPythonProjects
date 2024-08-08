
from re import search

def print_bitboard(number):
    binary = bin(number)[2:].zfill(12)
    start = 0
    for row in range(4):
        for i in range(start, 12, 4):
            print(binary[i], end = " ")
        start = start + 1
        print()
    print()

def print_data(data):
    start = 10
    for row in range(3):
        for i in range(start, -1, -4):
            print(data[i], end = " ")
        start = start - 1
        print()
    print()

def check(cp_bb):
    # /
    temp = cp_bb & (cp_bb >> 3)
    if (temp & (temp >> 3)): return True

    # -
    temp = cp_bb & (cp_bb >> 4)
    if (temp & (temp >> 4)): return True
    
    # \
    temp = cp_bb & (cp_bb >> 5)
    if (temp & (temp >> 5)): return True

    # |
    temp = cp_bb & (cp_bb >> 1)
    if (temp & (temp >> 1)): return True

    return False

def comp_move(all_bb, current_bb, comp_playing, possis):
    scores = []
    if len(possis) > 0:
        for possi in possis:
            if check(current_bb + 2 ** possi):
                score = len(possis)
                if not comp_playing: score = -score
                return [score, possi]
            else:
                scores.append([(comp_move(all_bb + (2 ** possi), current_bb ^ all_bb, not comp_playing, [i for i in possis if i != possi]))[0], possi])
    else:
        return [0, 0]
    return (sorted(scores, key = lambda x:x[0], reverse = comp_playing))[0]

all_bb = 0
current_bb = 0
possis = [0, 1, 2, 4, 5, 6, 8, 9, 10]
blank = "_"
data = [blank] * 12

while True:
    print("Should the computer play first or second? Please type either 1 or 2.")
    choice = input(">>>")
    if choice == "1" or choice == "2":
        break
    else:
        print("Invalid input.")

if choice == "1":
    comp_playing = True
    comp_letter = "X"
    human_letter = "O"
else:
    comp_playing = False
    comp_letter = "O"
    human_letter = "X"


print("--------------------------------------------")

if not comp_playing:
    print_data(data)

while True:
    if len(possis) == 0:
        print("It's a draw!")
        break
    elif comp_playing:
        score, move = comp_move(all_bb, current_bb, comp_playing, possis)
        all_bb = all_bb + 2 ** move
        current_bb = current_bb + 2 ** move
        possis.remove(move)
        data[move] = comp_letter
        print_data(data)
        print("The computer has moved!")
    else:
        while True:
            pattern = r"^[0-9]+$"
            print("\nMove Number Grid:")
            print_data([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            print("To make your move, enter the number in the position corresponding to where you want to move.")
            print("What is your move?")
            move = input(">>>")
            if search(pattern, move) and (int(move) in possis):
                break
            else:
                print("Invalid Move.")

        move = int(move)
        all_bb = all_bb + 2 ** move
        current_bb = current_bb + 2 ** move
        possis.remove(move)
        data[move] = human_letter
        print_data(data)
        print("The human has moved!")
    
    input("Press Enter to continue...")
    print("--------------------------------------------")
    if check(current_bb):
        if comp_playing:
            print("The computer has won!")
        else:
            print("The human has won!")
        break
    comp_playing = not comp_playing
    current_bb = all_bb ^ current_bb

print("--------------------------------------------")
        
        
        




