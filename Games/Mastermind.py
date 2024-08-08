import random
import re

def random_sequence():
        colours = ["R", "B", "G", "Y", "P", "O", "I", "V", "L", "A"]
        sequence = []
        for i in range(4):
                sequence.append(random.choice(colours))
        return sequence

def check(sequence, guess):
        right = 0
        wrong = 0
        not_done = [0, 1, 2, 3]
        for i in range(4):
                if guess[i] == sequence[i]:
                        right = right + 1
                        not_done.remove(i)
        new_sequence = []
        new_guess = []
        for i in not_done:
                new_sequence.append(sequence[i])
                new_guess.append(guess[i])
        for i in new_sequence:
                if i in new_guess:
                        wrong = wrong + 1
                        new_guess.remove(i)
        return [right, wrong]

def list1():
        print("You have 10 colours to choose from...")
        print("R: Red")
        print("B: Blue")
        print("G: Green")
        print("Y: Yellow")
        print("P: Purple")
        print("O: Orange")
        print("I: Indigo")
        print("V: Violet")
        print("L: Lilac")
        print("A: Auburn")
        print("   ")

def guess():
        guess = ""
        pattern = r"^[RBGYPOIVLA]{4}$"
        while True:
                guess = input("Please enter your guess...")
                if re.search(pattern, guess):
                        break
                else:
                        print("Invalid guess.")
        print("Your guess was " + guess)
        print("Thank you!")
        return list(guess)

def mastermind():
        print("Generating sequence...")
        sequence = random_sequence()
        print("Done!")
        print("   ")
        list1()
        times = 0
        while True:
                guess1 = guess()
                data = check(sequence, guess1)
                print("Correct colour in correct place: ", data[0])
                print("Correct colour in wrong place: ", data[1])
                times = times + 1
                if data[0] == 4:
                        print("Congratulations! You win!")
                        print("It took you", times, "times to guess the right answer.")
                        break
                else:
                        print_choice = ""
                        while True:
                                print_choice = input("Do you want to print the list of colours again? Y or N?")
                                if print_choice == "Y" or print_choice == "N":
                                        print()
                                        break
                                else:
                                        print("Invalid input.")
                        if print_choice == "Y":
                                list1()

mastermind()
                        
        
