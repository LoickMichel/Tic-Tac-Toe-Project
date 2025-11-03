import random

grid = [" "]*9
#We're defining the grid of the board and giving a value to every case for the win check
def grid_show():
    print("\n    1   2   3")
    print(f"1   {grid[0]} | {grid[1]} | {grid[2]}") #First line
    print("   -----------")
    print(f"2   {grid[3]} | {grid[4]} | {grid[5]}") #Second line
    print("   -----------")
    print(f"3   {grid[6]} | {grid[7]} | {grid[8]}\n") #Third line

#Making a fonction to check if the win condition is completed
def win_check():
    win = [
        [0,1,2],[3,4,5],[6,7,8],   # We're checking the lines
        [0,3,6],[1,4,7],[2,5,8],   # We're checking the collums
        [0,4,8],[2,4,6]            # We're checking the diagonals
    ]
    #We're defining that is any combos in win is true, then the winning condition is completed
    for a,b,c in win:
        if grid[a] == grid[b] == grid[c] != " ":
            return grid[a]
    return None

#We're making an improved IA that uses logic instead of randomness
def ia(board, signe):
    opponent = "O" if signe == "X" else "X"
    winning_lines = [
        (0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)
    ]

    #First, the AI checks if it can win in one move
    for a, b, c in winning_lines:
        line = [board[a], board[b], board[c]]
        if line.count(signe) == 2 and line.count(" ") == 1:
            return [a, b, c][line.index(" ")]

    #Then, the AI checks if the opponent can win and blocks it
    for a, b, c in winning_lines:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count(" ") == 1:
            return [a, b, c][line.index(" ")]

    #If not, the AI plays the center if it's free
    if board[4] == " ":
        return 4

    #If not, the AI plays a corner if it's free
    for i in [0, 2, 6, 8]:
        if board[i] == " ":
            return i

    #If no better move, the AI plays the first available cell
    for i in range(9):
        if board[i] == " ":
            return i

    #If there is no move left (should not happen), return None
    return None


def game():
    mode = input("Voulez-vous jouer contre un autre joueur (1) ou contre l'IA (2) ? ")
    while mode not in ["1","2"]:
        mode = input("Erreur ! Choisissez 1 ou 2 : ")
    
    #We're defining an input variable so the player1 can choose his side: X or O
    player1 = input("Player 1, choisissez votre symbole (X ou O) : ") 
    while player1 != "X" and player1 != "O":
        player1 = input("Erreur ! Choisissez X ou O : ")
    
    #Automatically assigning the opposite symbol to the other player
    player2 = "O" if player1 == "X" else "X"
    
    vs_ia = False                      # ← renamed to avoid conflict with function name
    if mode == "2":
        vs_ia = True                   # ← same here
    
    print("Player 1 joue", player1, ", Player 2 joue", player2, "!")
    
    player = player1
    
    #We're opening a loop
    while True:
        grid_show()
        
        if player == player1 or not vs_ia:  # ← updated variable name here
            try:
                line = int(input(f"Joueur {player}, choississez une ligne (1-2-3): ")) 
                colum = int(input(f"Joueur {player}, choississez une colonne (1-2-3): "))
                
                #We're cheking if the input is correct
                if line < 1 or line > 3 or colum < 1 or colum > 3:
                    print("Les valeurs doivent etre comprise entre 1 et 3")
                    continue
                
                #We're checking if the case is available or not
                test_case = (line - 1) * 3 + (colum - 1)
                if grid[test_case] != " ":
                    print("Case déjà prise, choisissez une autre.")
                    continue
            #We're checking if the value enter by the user is incorrect (If he enter anything but a number between 1 and 3)
            except ValueError:
                print("Entrée invalide. Tapez un nombre entre 1 et 3.")
                continue
        else:
            test_case = ia(grid, player) #The AI chooses its move using the new intelligent function
            print(f"L'IA joue en ligne {(test_case // 3)+1}, colonne {(test_case % 3)+1}")
        
        grid[test_case] = player
        
        #We're defining the final message depending if one of the player won or if it's a draw.
        winner = win_check()
        if winner:
            grid_show()
            print(f"Le joueur {winner} a gagné !")
            break
        if grid_full():
            grid_show()
            print("Match nul !")
            break

        #We're defining a tiny condition to change player each turn
        if player == player1:
            player = player2
        else:
            player = player1

game()
