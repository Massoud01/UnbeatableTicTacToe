from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import PhotoImage
turn="O"
bot = 'X'
marks=[]
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
gameover=False
computerscore=0
draws=0
def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False
def Winner():
    #lignes
    if (board[1] == board[2] and board[1] == board[3] and board[1] != " "):
            marks.append(1)
            marks.append(2)
            marks.append(3)
            return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != " "):
            marks.append(4)
            marks.append(5)
            marks.append(6)

            return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != " "):
            marks.append(7)
            marks.append(8)
            marks.append(9)
            
            
            
            return True
    #colonnes
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != " "):
            marks.append(1)
            marks.append(4)
            marks.append(7)
            
            
            
      
            return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != " "):
            marks.append(2)
            marks.append(5)
            marks.append(8)
            
            return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3]!= " "):
            marks.append(3)
            marks.append(6)
            marks.append(9)
            
            
            return True
    #diagonales
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != " "):
            marks.append(1)
            marks.append(5)
            marks.append(9)
            
            
            return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != " "):
            marks.append(7)
            marks.append(5)
            marks.append(3)
            
            
            
            return True
    else:
        return False
 
def compMove():
    global bot,turn, gameover,computerscore
    bestScore = -2
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False,-2, 2)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    button = buttons[(bestMove - 1) // 3][(bestMove - 1) % 3]
    if button['text'] == " ":
        button['text'] = "X"
        button['font']="Arial 15 bold"
        button['fg']="red"  
        board[bestMove] = bot
        if Winner():
            for key in marks:
                    winning_button = buttons[(key - 1) // 3][(key - 1) % 3]
                    winning_button['bg'] = 'yellow'
            tkinter.messagebox.showinfo("Tic tac toe", "Computer won this game")
            gameover = True
            computerscore+=1
            computer_Score_label.config(text="Computer Score: "+str(computerscore))
            

        elif checkDraw():
           tkinter.messagebox.showinfo("Tic tac toe", "Game Draw")
           draws+=1
           gameover=True
def max_value(board,depth,alpha,beta):
        bestScore = -2
        best_move = None
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth+1, False, alpha, beta)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
                    best_move= key
                    alpha = max(alpha,bestScore)
                    if beta <= alpha:
                        break
        return bestScore
def min_value(board,depth,alpha,beta):
        bestScore = 2
        best_move= None
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = turn
                score = minimax(board, depth + 1, True, alpha,beta)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
                    best_move= key
                    beta=min(beta,bestScore)
                    if beta <= alpha:
                        break
        return bestScore
 
def minimax(board, depth, isMaximizing,alpha,beta):
    if depth==8:
         return evaluate(board)
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(turn)):
        return -1
    elif (checkDraw()):
        return 0
    if (isMaximizing):
        return max_value(board,depth,alpha,beta)
 
    else:
        return min_value(board,depth,alpha,beta)

def evaluate(board):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]  # Diagonals
    ]

    for combination in winning_combinations:
        if all(board[pos] == bot for pos in combination):
            return 1  # Computer wins

        if all(board[pos] == turn for pos in combination):
            return -1  # Opponent wins
        
def play(event):
    global turn, gameover
    if gameover:
        return #si gameover is true no further moves are allowed
    button=event.widget
    buttonText=str(button)
    clicked=buttonText[-1]
    if clicked=="n":
        clicked=1
    else:
        clicked=int(clicked)
    if button['text']==" ": #pourqu'on puisse pas inserer X ou O dans une meme case
        button['text']="O"
        button['font']="Arial 15 bold"
        button['fg']="blue"  
        board[clicked]=turn
        if Winner():
          tkinter.messagebox.showinfo("Tic tac toe", "You won this game")
          gameover=True
        elif checkDraw():
          global draws
          tkinter.messagebox.showinfo("Tic tac toe", "It's A Draw!")
          draws+=1
          draws_label.config(text="Draws: "+str(draws))
          gameover=True
        else:
            compMove()
        #if turn == 'X':
            #turn = 'O'
        #else:
            #turn = 'X'
def playagain():
    global turn, gameover
    gameover=False
    for row in buttons:
        for button in row:
            button['text'] = ' '
    for key in board:
        board[key] = ' '
    gameover = False
    for key in board:
        winning_button = buttons[(key - 1) // 3][(key - 1) % 3]
        winning_button['bg'] = 'white'
    marks.clear()

def restart():
    global computerscore
    global draws
    computerscore=0
    draws=0
    draws_label.config(text="Draws: 0")
    computer_Score_label.config(text="Computer Score: 0")
    global turn, gameover
    gameover=False

    for row in buttons:
        for button in row:
            button['text'] = ' '
    for key in board:
        board[key] = ' '
    for key in board:
        winning_button = buttons[(key - 1) // 3][(key - 1) % 3]
        winning_button['bg'] = 'white'
    marks.clear()

    gameover = False


 
 
def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True
#creation de la fenetre,labels et frames
fenetre=Tk()
fenetre.minsize(300,300)
fenetre.title("Unbeatable Tic tac toe")
fenetre.resizable(False,False)
frame1=ttk.Frame(fenetre)
frame1.grid()
fenetre.configure(bg="cyan2")
Label1=Label(fenetre,text="Unbeatable Tic Tac Toe",font="Arial 20 bold ",fg='red',bg="cyan2")
Label1.grid(column=0,row=0,padx=150,pady=10)

frame2=Frame(fenetre)
frame2.grid()
frame2.configure(bg="cyan2")


buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = Button(frame2, text=" ", width=10, height=3, relief="sunken",background="white",font="Arial 15 bold")
        button.grid(row=i, column=j)
        button.bind('<Button-1>', play) 
        row_buttons.append(button)
    buttons.append(row_buttons)

playagainButton=Button(frame2,text="Play Again!", width=12, command=playagain,font="Arial 15 bold",fg="blue",bg="cyan2")
restartButton=Button(frame2,text="Restart Game", width=12, command=restart,font="Arial 15 bold",fg="red",bg="cyan2")
playagainButton.grid(column=1, row=4, padx=5,pady=5)
restartButton.grid(column=1, row=6, padx=5,pady=5)

computer_Score_label = Label(frame2, text="Computer Score:"+" "+ str(computerscore), font="Arial 15 bold", fg="blue",bg="cyan2")
computer_Score_label.grid(column=1, row=5, padx=5, pady=5)
draws_label = Label(frame2, text="Draws:"+" "+ str(draws), font="Arial 15 bold", fg="black",bg="cyan2")
draws_label.grid(column=1, row=7, padx=5, pady=5)
 
 
   
 
fenetre.mainloop()
