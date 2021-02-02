import time
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

#//create dictonary with each sqauare as entry
 
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
    return 1      

main = {}
for i in range(9):
    for j in range(9):
        main[str(i)+str(j)] = [i for i in range(1,10)]
      
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] != 0:
            main[str(i)+str(j)] = [board[i][j]]
                            
def engine(list,dict):
    for i in main.keys():
        x = []
        if len(main[i]) != 1: 
            pos = (int(i[0]),int(i[1])) 
            for ele in main[i]:
    #for rows
                for p in range(len(board[0])):
                    if board[pos[0]][p] == ele:
                        x.append(ele)
                        break
            main[i] = [q for q in main[i] if q not in x]                    
    print(main)       
    #for columns  
    for i in main.keys():
        y = []
        if len(main[i]) != 1:  
            pos = (int(i[0]),int(i[1])) 
            for elem in main[i]:
                for j in range(len(board)):
                    if board[j][pos[1]] == elem:
                        y.append(elem)
                        break 
            main[i] = [e for e in main[i] if e not in y]                  
                    
    #for boxes                                 
    for t in main.keys():
        z = []
        if len(main[t]) != 1:    
            pos = (int(t[0]),int(t[1])) 
            x = pos[1]//3
            y = pos[0]//3
            for elemn in main[t]:
                for i in range(y * 3,(y * 3) + 3):
                    for j in range(x * 3,(x * 3) + 3):
                        if board[i][j] == elemn:
                            z.append(elemn)
                            break
            main[t] = [r for r in main[t] if r not in z]  
    for i in main.keys():
        if len(main[i]) == 1:
            board[int(i[0])][int(i[1])] = main[i][0]      
    unsol = empty_sq(board)
    if unsol == 1:
        return board
    else:
        return engine(board,main)
                        
print_board(engine(board,main))