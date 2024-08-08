# Short Python Projects

## Ciphers
Encryption is the process of converting readable plaintext into incomprehensible ciphertext. Different ciphers use different algorithms to ensure that unauthorised people cannot access confidential data hidden through this process. The intended recipients can convert the ciphertext back into plaintext by using a key.

### Caesar Cipher
This cipher involves shifting each letter of the plaintext a certain number of steps down the alphabet. The number of steps is specified by the key.

### Rail Fence Cipher
This cipher is a type of transposition cipher. It involves writing the plaintext diagonally (in a SE direction) on the rails of an imaginary fence. When the bottom rail is reached, the plaintext continues to be written in a NE direction. When the top rail is reached again, the plaintext is written in a SE direction again. When the plaintext has been completely written out, the ciphertext is created by reading the text horizontally, rail by rail. The number of rails is specified by the key.

### Vigenère Cipher
This cipher involves shifting each letter of the plaintext by a number of steps down the alphabet specified by the corresponding letter of the key.

### Simulated Annealing Algorithm
This algorithm allows the user to input ciphertext encrypted through a monoalphabetic substitution cipher. It will randomly generate a cipher alphabet, decrypt the ciphertext using this alphabet and give the resulting text a score based on how close it is to English. By swapping letters of the alphabet, and through a Simulated Annealing technique, this program will find the score's global maximum. In this way, it will find the correct cipher alphabet and decrypt the original ciphertext.

## Fractals
Fractals are geometric shapes that have detail at extremely small scales. They occur naturally in the shapes of trees, snowflakes and DNA structures. They are often self-similar (the shape looks similar when viewed at different scales). 

### Dragon Curve
This is the fractal that results from continuously folding a strip of paper in half.

### Gosper Curve
This is the fractal that results from continuously replacing each line segment with a complex pattern. 

### Koch Snowflake
This is the fractal that results from continuously replacing the middle third of each line segment with two sides of an equilateral triangle.

### Sierpiński Triangle
This is the fractal that results from continuously splitting each black equilateral triangle into four smaller equilateral triangles and colouring the middle triangle white.

### Space Filling Curve
This Space Filling Curve is a continuous line that fills up a square.

## Games
### Mastermind
This program will allow the user to play the game Mastermind. The computer will randomly generate a sequence of four colours. These colours will be chosen from a list of ten colours (the original game had a list of eight colours). The user must guess this four-colour sequence in 10 or fewer chances. After each wrong guess, the program will reveal the number of right colours in the right place and the number of right colours in the wrong place.
I use an Excel spreadsheet to organise my guesses and the computer's analysis, providing a more effective user interface.

### Sudoku Solver
This Sudoku solver allows the user to input a Sudoku puzzle row by row, replacing the blank spaces with the number 0. The program will solve the puzzle using Recursive Backtracking and return the correct answer.

### XO Engine
This program allows the user to play a game of Noughts and Crosses against the computer. In the program, the user can decide who plays first, and who places noughts ("O") or crosses ("X"). When it is the computer's turn, the program recursively generates every possible set of moves from the current board position. When each set of moves ends (with either a win, loss or draw), the computer will give the position a score based on the number of moves the current player has remaining. The program takes these scores, backtracks through the sets of moves and, assuming that the human player plays perfectly, finds the computer's optimal move.

## Robotics
### Line Following Robot
The robot in the video uses two IR sensors to allow it to follow a black line. I am using my Raspberry Pi 3 to control it. 

### Object Following Robot
The robot in the video is Marty The Robot v2. It has an IR Obstacle sensor and a Colour Obstacle sensor on each of its two feet. Using this, I have programmed it to follow objects. In this video, I have used a roll of red electrical tape, but Marty will follow any object read by its sensors. 

Controlling Marty requires the Python 3 library `martypy`. This can be installed by running the command `pip install martypy`. 

### Colour Sensing Robot
In the video, I am holding a RealSense Depth Camera. The computer is running a closed loop ROS system connecting two Python 3 programs: `Realsense Picture.py` and `Move Robot.py`. The program `Realsense Picture.py` uses the camera to take a picture of the card I am holding it above. The picture is published to the ROS Topic "Images". The program `Move Robot.py` subscribes to this Topic, takes the image, and converts it into the HSV colour space. Using the hue value, it identifies the colour and calls the corresponding command (Green: Move Forward, Yellow: Move Backward, Purple: Slide Right, Blue: Slide Left, Red: Dance). Once Marty's action is complete, `Move Robot.py` publishes a confirmation message to the ROS Topic "Confirm". The program `Realsense Picture.py` subscribes to this Topic. When a confirmation message is received, `Realsense Picture.py` takes another picture, allowing the cycle to repeat. 
