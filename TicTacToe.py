board=[[' ',' ',' '],
       [' ',' ',' '],
       [' ',' ',' ']]

move ='x'
winner=''

def display(b):
    print('-----------------')
    print('0',b[0])
    print('1',b[1])
    print('2',b[2])
    print('    0    1    2')

def legal(x,y):
    if (x in range(3))and(y in range(3))and(board[x][y]==' '):
        return True
    else:
        return False 

def evaluate(bd):
    global winner
    if ['x','x','x']in bd:
        winner = 'x'
        return -10
    elif ['o','o','o']in bd:
        winner = 'o'
        return 10
    elif ['x','x','x'] in [[bd[i][j] for i in range(3)] for j in range(3)]:
        winner = 'x'
        return -10
    elif ['o','o','o'] in [[bd[i][j] for i in range(3)] for j in range(3)]:
        winner = 'o'
        return 10
    elif (['o','o','o']==[bd[0][0],bd[1][1],bd[2][2]])or(['o','o','o']==[bd[2][0],bd[1][1],bd[0][2]]):
        winner = 'o'
        return 10
    elif (['x','x','x']==[bd[0][0],bd[1][1],bd[2][2]])or(['x','x','x']==[bd[2][0],bd[1][1],bd[0][2]]):
        winner = 'x'
        return -10
    elif (' ' not in bd[0])and(' ' not in bd[1])and(' ' not in bd[2]):
        winner="draw"
        return 0
    else:
        return 1
    
def minimax(b,depth,alpha,beta,isMax):
    if evaluate(b)!=1:
        return evaluate(b)
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if b[i][j]==' ':
                    b[i][j]='o'
                    best = max(best, minimax(board, depth+1, alpha, beta, False))
                    alpha = max(alpha, best)
                    b[i][j]=' '
                    if alpha >= beta:
                        break
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if b[i][j]==' ':
                    b[i][j]='x'
                    best = min(best, minimax(b, depth+1, alpha, beta, True))
                    beta = min(beta, best)
                    b[i][j]=' '
                    if beta <= alpha:
                        break
        return best
    
def ai_play(b):
    bestVal=-1000
    h=k=-1
    for i in range(3):
        for j in range(3):
            if b[i][j]==' ':
                b[i][j]='o'
                moveVal = minimax(b, 0, -1000, +1000, False)
                b[i][j]=' '
                if moveVal>bestVal:
                    h=i
                    k=j
                    bestVal=moveVal
    board[h][k]='o'             
    
if input('enter y to move first: ')=='y':
    move = 'x'
else:
    move='o'
    
while (evaluate(board)==1):
    if move=='x':
        display(board)
        i=int(input("row: "))
        j=int(input("column: "))
        if legal(i,j):
            board[i][j]=move
            move='o'
    else:
        ai_play(board)
        move='x'
            
display(board)            
print("winner is: ",winner)
