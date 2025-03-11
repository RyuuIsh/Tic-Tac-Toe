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

## 💡 Game Output (CLI Example)
### ✅ Player Starts
```
Tic Tac Toe Game

Do you want to start? (Y for yes): Y
Play against intelligent computer? (Y for yes): Y

 A  B  C
1 .  .  .
2 .  .  .
3 .  .  .

Enter position <row><col>: 2B
Computer placed on: 3A

 A  B  C
1 .  .  .
2 .  X  .
3 O  .  .
```

## ⚙️ Setup & Run the Game
### ✅ 1. Clone the Repository
```
git clone https://github.com/yourusername/Tic-Tac-Toe-AI.git
cd Tic-Tac-Toe-AI
```

### ✅ 2. Run the Game
```
python tic_tac_toe.py
```

### ✅ 3. Start Playing
```
Tic Tac Toe Game

Do you want to start? (Y for yes): Y
Play against intelligent computer? (Y for yes): Y
```

## 🎮 Game Modes
| Mode | Description |
|--------|--------------|
| ✅ Easy |	Computer makes random moves |
| ✅ Hard |	AI tries to block or win |
| ✅ Unlimited |	Keep playing after each game ends |

## 💡 Why Is This Game Special?
✅ Intelligent AI: Can block you and win like a human.<br>
✅ Random Mode: Allows easy fun gameplay.<br>
✅ No External Libraries: 100% Pure Python.<br>
✅ Play Continuously: The game keeps restarting until you quit.<br>

## 🚀 Future Enhancements
✅ Convert the game to GUI using Tkinter/Pygame 🖥️<br>
✅ Implement a Leaderboard for scores 🏆<br>
✅ Add a 2-player mode for local friends 🤝<br>
✅ Deploy it on a web application 🌐<br>

## 💙 Connect With Me
💻 Developer: Ishaan Chhabra<br>
🔗 GitHub: RyuuIsh<br>
<br>
💙 Challenge the AI and Win the Game! 🎮🤖









