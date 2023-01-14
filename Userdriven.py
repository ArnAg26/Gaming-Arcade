import Wordle
import TicTacToe
import Oddeven
while True:
    print("Hello There!")
    print("Welcome to our gaming arcade!")
    print("What would you like to play?")
    print('''We have the following options for you:
    1 -> Odd Even Cricket
    2 -> Tic Tac Toe
    3 -> Wordle''')
    N=int(input("Please enter your choice: "))
    if N==1:
        print("You chose Odd Even Cricket")
        print("\n")
        print("The guidelines for this game is as follows: ")
        print("The rules for this game are very similar to those of cricket")
        print(''' There will be a toss in the beginning to decide batting or bowling
After the toss, the user has to enter digits between 0 and 6 for the game to proceed.
If you are batting, your score will added until you get out.
If you are bowling, you have to enter digits until the batsman gets out.
After both the innings, the total score of both the competitors is computed and then the winner is declared.''')
        print("\n")
        print("ENJOY!")
        Oddeven.oddeven()
    elif N==2:
        print("You chose Tic Tac Toe")
        print("\n")
        print("The guidelines for this game is as follows: ")
        print("The rules are similar to that of Tic Tac Toe")
        print('''There would be a 3*3 board on which users have to put their markers.
Both the players would first have to enter their markers/identifiers on the board.
The players then have to put their markers on the board on their desired coordinates.
To do so, they have to enter the coordinates (x,y) in a space separated format.
After this, if a pattern of 3 consecutive markers is formed then the user corresponding to that marker wins the game.
If, the users exhaust all the 9 chances, then it is a draw.''')
        print("\n")
        print("ENJOY!")
        TicTacToe.tictactoe()
    elif N==3:
        print("You chose Wordle")
        print("\n")
        print("The guidelines for the game are as follows: ")
        print("The rules are similar to the famous game Wordle")
        print(''' There would be a random word being generated for you to guess.
You have to type a 5 letter word as your guess.
If any letter of your entered word is there in the answer, then it shows "Y" in place of that letter.
If any letter of your entered word is there in the answer in the exact same position, then it shows "G" in place of that letter.
If you guess the correct word within 6 chances, you win.
Otherwise, you lose.''')
        print("\n")
        print("ENJOY")
        Wordle.wordle()
    Q=input("More(Y/N)?: ")
    if Q in "Nn":
        break

    


