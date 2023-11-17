import random
import math
import colorama
from colorama import Fore,Back,Style 



def new_number(board,size):#añadimos un 2 o 4 a alguna de las casillas que sea 0
    possible=[]
    for i in range(size):
        row=board[i]
        for j in range(size):
            square=row[j]
            if square==0:
                possible+=[(i,j)]
    choice=random.choice(possible)
    new=random.choice([2,4])
    board[choice[0]][choice[1]]=new 
    for n in range(size):
        print(board[n])
    return(board)
def play_move1(move,board,size):#primera parte del movimiento, antes de juntar los números iguales
    if move=="left":
        T=[[board[n][m] for n in range(size)] for m in range(size)]#Hemos hecho la transpuesta,ahora será como hacer "up"
        for i in range(size):
            for j in range(size-1):
                if T[j][i]==0:
                    l=1
                    while l<size-1-j and T[j+l][i]==0:
                        l+=1
                    T[j][i]=T[j+l][i]
                    T[j+l][i]=0
        board=[[T[j][i] for j in range(size)] for i in range(size)]#volvemos a transponer  




    elif move=="right":
        T=[[board[j][i] for j in range(size)] for i in range(size)]
        for i in range(size):
            for j in range(size-1):
                if T[size-1-j][i]==0:
                    l=1
                    while l<size-1-j and T[size-1-j-l][i]==0:
                        l+=1
                    T[size-1-j][i]=T[size-j-1-l][i]
                    T[size-j-1-l][i]=0
        board=[[T[j][i] for j in range(size)] for i in range(size)]



    elif move=="down":
        for i in range(size):#fijamos columna
            for j in range(size-1):#fijamos fila
                if board[size-1-j][i]==0:#miramos de la casilla más alta a la más baja
                    l=1
                    while l<size-1-j and board[size-1-j-l][i]==0:#encontramos la primera casilla distinta de 0
                        l+=1
                    board[size-1-j][i]=board[size-j-1-l][i]
                    board[size-j-1-l][i]=0





    elif move=="up":
        for i in range(size):
            for j in range(size-1):
                if board[j][i]==0:
                    l=1
                    while l<size-1-j and board[j+l][i]==0:
                        l+=1
                    board[j][i]=board[j+l][i]
                    board[j+l][i]=0
                
    return(board)
def play_move2(move,board,size):#segunda parte del movimiento, juntamos los números iguales
    if move=="left":
        for i in range(size):
            for j in range(size-1):
                if board[i][j]==board[i][j+1]:
                    board[i][j]=board[i][j]*2
                    board[i][j+1]=0



    elif move=="right": 
        for i in range(size):
            for j in range(size-1):
                if board[i][size-1-j]==board[i][size-1-j-1]:
                    board[i][size-1-j]=board[i][size-1-j]*2
                    board[i][size-1-j-1]=0

        
        

    elif move=="up":
        for i in range(size):
            for j in range(size-1):
                if board[j][i]==board[j+1][i]:
                    board[j][i]=board[j][i]*2
                    board[j+1][i]=0


    elif move=="down":
        for i in range(size):
            for j in range(size-1):
                if board[size-1-j][i]==board[size-1-j-1][i]:
                     board[size-1-j][i]=board[size-1-j-1][i]*2
                     board[size-1-j-1][i]=0

   
    return(board)
def play_move(move,board,size):#El movimiento total se puede descomponer en la composición: move1(move2(move3(board)))
    board=play_move1(move,play_move2(move,play_move1(move,board,size),size),size)
    return(board)
def play_2048(goal=2048,size=4):
    board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    values=[]
    board=new_number(board,size)#Hacemos el primer paso fuera para tener un new_board que comparar con board
    move=input("next move: ")#primer paso
    new_board=play_move(move,board,size)#primer paso
    for i in range(size):#primer paso
        for j in range(size):#primer paso
            values.append(board[i][j])#primer paso
    while goal not in values and 0 in values:#Comprobamos que no se haya bloqueado el tablero o se haya llegado al objetivo.
        if not new_board==board:#Comprobamos que el movimiento haya hecho algo de verdad, si no, no generaremos un nuevo número.
            board=new_number(new_board,size)
        else:
            for n in range(size):
                print(board[n])
        values=[]
        move=input("next move: ")
        new_board=play_move(move,board,size)
        for i in range(size):
            for j in range(size):
                values.append(new_board[i][j])
    if goal in values:
        print(Fore.GREEN+("You win!"))
        for n in range(size):
            print(new_board[n])
        return()
    else:
        print(Fore.RED+("You loose"))
        for n in range(size):
            print(new_board[n])
        return()




