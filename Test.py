board = [" "]*9
#We're defining the grid of the board and giving a value to every case for the win check
def board_show():
    print("\n    1   2   3")
    print(f"1   {board[0]} | {board[1]} | {board[2]}") #First line
    print("   ---+---+---")
    print(f"2   {board[3]} | {board[4]} | {board[5]}") #Second line
    print("   ---+---+---")
    print(f"3   {board[6]} | {board[7]} | {board[8]}\n") #Third line

#Making a fonction to check if the win condition is completed
def win_check():
    win = [
        [0,1,2],[3,4,5],[6,7,8],   # We're checking the lines
        [0,3,6],[1,4,7],[2,5,8],   # We're checking the collums
        [0,4,8],[2,4,6]            # We're checking the diagonals
    ]
    #We're defining that is any combos in win is true, then the winning condition is completed
    for a,b,c in win:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None

#We're making a fonction to check if the board is full, to check for equality
def board_full():
    if " " in board:
        return False
    else:
        return True 

def game():
    #We're defining an input variable so the player can choose his side: X or O
    player = input("Choisissez votre symbole (X ou O) : ") 
    while player != "X" and player != "O":
        player = input("Erreur ! Choisissez X ou O : ")
    print("Vous jouez", player, "!")

    while True:
        board_show()
        try:
            line = int(input(f"Joueur {player}, choississez une ligne (1-2-3): ")) 
            colum = int(input(f"Joueur {player}, choississez une colonne (1-2-3): "))
            
            #We're cheking if the input is correct
            if line < 1 or line > 3 or colum < 1 or colum > 3:
                print("Les valeurs doivent etre comprise entre 1 et 3")
                continue
            
            #We're checking if the case is available or not
            test_case = (line - 1) * 3 + (colum - 1)
            if board[test_case] != " ":
                print("Case déjà prise, choisissez une autre.")
                continue
        #We're checking if the value enter by the user is incorrect (If he enter anything but a number between 1 and 3)
        except ValueError:
            print("Entrée invalide. Tapez un nombre entre 1 et 3.")
            continue
        
        board[test_case] = player

        winner = win_check()
        if winner:
            board_show()
            print(f"Le joueur {winner} a gagné !")
            break
        if board_full():
            board_show()
            print("Match nul !")
            break

        player = "O" if player == "X" else "X"

game()