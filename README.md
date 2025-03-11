# 🎮 Python Tic Tac Toe Game (With AI Mode)
This project is a Python-based Tic Tac Toe game where you can:<br>
✅ Play against the Computer (AI) 🤖<br>
✅ Play against a Random Computer 🤔<br>
✅ Restart the Game after winning or draw 🔄<br>
✅ Intelligent AI Mode that can either block you or win the game 🤯<br>
✅ Real-time game simulation on CLI (Command Line Interface) 💻<br>

## Features
1. Play Against Computer (AI)
- You can play against a computer.
- Choose if you want the computer to be intelligent (AI) or random.
<br>
2. Intelligent AI Mode (Hard)
- In AI mode, the computer will:
- Try to win first.
- Block your winning move.
- Take center or corner first if no winning/blocking move.
- Take a random empty spot if nothing else works.
<br>
3. Random Mode (Easy)
- In random mode, the computer will randomly place its move without any logic.
<br>
4. Restart Game Option
- The game will automatically restart after a win or a draw.
- You can keep playing unlimited games without stopping the program.
<br>
5. Grid System
- The grid uses row-column notation:
```
A   B   C
1  .   .   .
2  .   .   .
3  .   .   .
```
- Example Inputs:
Center: 2B<br>
Bottom Left: 3A<br>
Top Right: 1C<br>

## 📂 Project Structure
The game is written purely in Python without any external libraries.
```
/Tic-Tac-Toe-AI
│── tic_tac_toe.py         # Main Game Logic
│── README.md              # Project Description
```

## 🎲 How to Play the Game
1. Run the Game:
```
python tic_tac_toe.py
```
2. Select Who Starts First:
```
Do you want to start? (Y for yes): Y
```
3. Choose Difficulty:
```
Play against intelligent computer? (Y for yes): Y
```
4. Start Making Moves:
The game grid will look like this:<br>
```
  A   B   C
1  .   .   .
2  .   .   .
3  .   .   .
```

## 💎 Win Conditions
The game can have 3 results:<br>
| Result | Explaination |
|--------|--------------|
| ✅ You Win |	If you place 3 X's horizontally, vertically, or diagonally. |
| ❌ Computer Wins |	If the computer places 3 O's first. |
| 🤝 Draw |	If the board is full with no winner. |

