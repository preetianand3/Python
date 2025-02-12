from IPython.display import clear_output
clear_output()

#main matrix

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
reserve = []

def display(mat):
    for r in mat:
        print(r)

def user_input(p):
    row = 'wrong'
    col = 'wrong'
    
    print(f"Enter the row and column that you want to insert the {p} mark in")
    
    while True:       
    #assuming 1st player chooses 'X'
        while row not in ['1', '2', '3']:   
            row = input("Row (1-3): ")
            if row not in ['1', '2', '3']:
                clear_output()
                print("Invalid choice!") 
            
        clear_output()
        
        while col not in ['1', '2', '3']:    
            col = input("Col (1-3): ") 
            if col not in ['1', '2', '3']:
                clear_output()
                print("Invalid choice!")  
                
        reserve.append([row, col])              
        
        if [row, col] in reserve:
            print("Place Already Occupied")
            row, col = '', ''
        else:
            break
        
            
    clear_output()
    print(f"Row :{row}    Col :{col}")
        
    
    row = int(row)-1
    col = int(col)-1
    
    return [row, col]


def insert(position, element):
    
    board[position[0]][position[1]] = element
    hori = [element, element, element]
    res = False
    
    for i in [0, 1, 2]:
        if board[i] == hori:
            res = True
            break
    
    for i in [0, 1, 2]:
        if board[0][i]==element and board[1][i]==element and board[2][i]==element :
            res = True
            break
    
    if board[0][0]==element and board[1][1]==element and board[2][2]==element:
        res = True
            
    return res


def play():
    turn = 0 
    match = False
    pos = []
    x = 'X'
    y = 'O'
    #check
    
    while match == False:
        if turn%2==0:
            pos = user_input(x)
            match = insert(pos, x)
        else:
            pos = user_input(y)
            match = insert(pos, y)
        display(board)    
        turn+=1
    
    if match == True:
        winner = ((turn-1)%2)+1
        print(f"Player {winner} WON!!!")


play()
