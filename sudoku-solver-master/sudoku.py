import datetime
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

#check validity of number
def valid(bo,pos,num):
    #for rows
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #for column
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False

    #for box
    x = pos[1]//3
    y = pos[0]//3
    
    for i in range(y * 3,(y * 3) + 3):
        for j in range(x * 3,(x * 3) + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
            
    return True        
   
#backtracing algorithm to solve puzzle         
def solver(bo):
    unsol = empty_sq(board)
    if not unsol:
        return True
    else:
        row, col = unsol
        
        
    for i in range(1,10):
        if valid(bo,(row, col),i):
            bo[row][col] = i
            
            if solver(bo):
                return True
            
            bo[row][col] = 0
            
            
    return False

  
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - ')
            
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print('|',end = '')        
                
            if  j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + '  ',end='') 
                               
def empty_sq(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)                    
    return None        

print_board(board)
print('_______________________________________________')        
solver(board)
print_board(board)