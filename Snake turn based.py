#!/usr/bin/env python
# coding: utf-8

# In[1]:


debug=0
gip=1
#imports
import random
from IPython.display import clear_output

#Score board
score=0
length=5

#board 
board=[[[False, False, False, 0] for i in range(16)]for j in range(16)]
#pos 1: has food
#pos 2: has snake
#pos 3: is head
#pos 4: snake timer

if debug==1:
    print(board)
    
#print system
#print board
def print_board(board):
    top="|     |"
    for i in range(16):
        if i<9:
            top+=(" C"+str(i+1)+"  | ")
        else:
            top+=("C"+str(i+1)+"  | ")
    print(top)
    e1=0
    for i in range(16):
        if i<9:
            line="|  R"+str(e1+1)+" |"
        else:
            line="| R"+str(e1+1)+" |"
        e1+=1
        for e in range(16):
            if board[e][i][0]==False and board[e][i][1]==False:
                line+="     | "
                continue
            if board[e][i][0]==True:
                line+="  F  | "
                continue
            if board[e][i][1]==True and board[e][i][2]==True:
                line+="  H  | "
                continue
            if board[e][i][1]==True:
                line+="  S  | "
                continue
        
        print(line)
        
if debug==1:
    print_board(board)
    
def print_score(score):
    print("Score:"+str(score))
    
if debug==1:
    print_score(score)
    
#start up
sixteen=[i for i in range(16)]
if debug==1:
    print(sixteen)
snake_strat_pos_x=random.choice(sixteen)
snake_strat_pos_y=random.choice(sixteen)
snake_head_pos_x=snake_strat_pos_x
snake_head_pos_y=snake_strat_pos_y
if debug==1:
    print(snake_strat_pos_x,snake_strat_pos_y)

#arry for direction randomization
news=[8,6,2,4] #the numbers corrospond to the numpad

while True:
    tail_direction=random.choice(news)
    if snake_strat_pos_x<4 and tail_direction==4:
        continue
    if snake_strat_pos_y<4 and tail_direction==8:
        continue
    if snake_strat_pos_x>11 and tail_direction==6:
        continue
    if snake_strat_pos_y>11 and tail_direction==2:
        continue
    break
if debug==1:
    print("tail direction:"+str(tail_direction))
    
board[snake_strat_pos_x][snake_strat_pos_y][1]=True
board[snake_strat_pos_x][snake_strat_pos_y][2]=True
board[snake_strat_pos_x][snake_strat_pos_y][3]=5

for i in range(1,5):
    if tail_direction==8:
        board[snake_strat_pos_x][snake_strat_pos_y-i][1]=True
        board[snake_strat_pos_x][snake_strat_pos_y-i][3]=5-i
        continue
    if tail_direction==2:
        board[snake_strat_pos_x][snake_strat_pos_y+i][1]=True
        board[snake_strat_pos_x][snake_strat_pos_y+i][3]=5-i
        continue
    if tail_direction==4:
        board[snake_strat_pos_x-i][snake_strat_pos_y][1]=True
        board[snake_strat_pos_x-i][snake_strat_pos_y][3]=5-i
        continue
    if tail_direction==6:
        board[snake_strat_pos_x+i][snake_strat_pos_y][1]=True
        board[snake_strat_pos_x+i][snake_strat_pos_y][3]=5-i
        continue
if debug==1:
    print(board)
    print_board(board)
    
# food placment 
def gen_food(board):
    food_pos_x=random.choice(sixteen)
    food_pos_y=random.choice(sixteen)
    while board[food_pos_x][food_pos_y][1]==True or board[food_pos_x][food_pos_y][0]==True:
        food_pos_x=random.choice(sixteen)
        food_pos_y=random.choice(sixteen)
    board[food_pos_x][food_pos_y][0]=True
        
gen_food(board)

if debug==1:
    print(board)
    print_board(board)
    
#movement    
def play_move(board,tail_direction,snake_head_pos_x,snake_head_pos_y,length,score):
    wasd=["w","a","s","d"]
    tdc=0
    while True:
        move=input("Press W,A,S or D to move: ")
        if move not in wasd:
            print("Invalid move: ")
            continue
        if tdc==1:  #This section is not working remove tdc to work on tail direction 
            if tail_direction==8 and move=="w":
                print("Invalid move: ")
                continue
            if tail_direction==4 and move=="a":
                print("Invalid move: ")
                continue
            if tail_direction==2 and move=="s":
                print("Invalid move: ")
                continue
            if tail_direction==6 and move=="d":
                print("Invalid move: ")
                continue
        break
            
            
            
    board[snake_head_pos_x][snake_head_pos_y][2]=False
    if move=="w":
        
        if board[snake_head_pos_x][snake_head_pos_y-1][0]==True:
            board[snake_head_pos_x][snake_head_pos_y-1][0]=False
            score==1
            length+=1
            gen_food(board)
            
        board[snake_head_pos_x][snake_head_pos_y-1][1]=True
        board[snake_head_pos_x][snake_head_pos_y-1][2]=True
        board[snake_head_pos_x][snake_head_pos_y-1][3]=length+1
        
        snake_head_pos_y-=1
        tail_direction=2
        
        
    if move=="s":
        
        if board[snake_head_pos_x][snake_head_pos_y+1][0]==True:
            board[snake_head_pos_x][snake_head_pos_y+1][0]=False
            score==1
            length+=1
            gen_food(board)
            
        board[snake_head_pos_x][snake_head_pos_y+1][1]=True
        board[snake_head_pos_x][snake_head_pos_y+1][2]=True
        board[snake_head_pos_x][snake_head_pos_y+1][3]=length+1
        
        snake_head_pos_y+=1
        tail_direction=8
        
    if move=="a":
        
        if board[snake_head_pos_x-1][snake_head_pos_y][0]==True:
            board[snake_head_pos_x-1][snake_head_pos_y][0]=False
            score==1
            length+=1
            gen_food(board)
            
        board[snake_head_pos_x-1][snake_head_pos_y][1]=True
        board[snake_head_pos_x-1][snake_head_pos_y][2]=True
        board[snake_head_pos_x-1][snake_head_pos_y][3]=length+1
        
        snake_head_pos_x-=1
        tail_direction=6
        
    if move=="d":
        
        if board[snake_head_pos_x+1][snake_head_pos_y][0]==True:
            board[snake_head_pos_x+1][snake_head_pos_y][0]=False
            score==1
            length+=1
            gen_food(board)
            
        board[snake_head_pos_x+1][snake_head_pos_y][1]=True
        board[snake_head_pos_x+1][snake_head_pos_y][2]=True
        board[snake_head_pos_x+1][snake_head_pos_y][3]=length+1
        
        snake_head_pos_x+=1
        tail_direction=4
        
    for i in range(16):
        for e in range(16):
            if board[i][e][2]==True:
                snake_head_pos_x=i
                snake_head_pos_y=e
            
            if board[i][e][3]!=0:
                board[i][e][3]-=1
            if board[i][e][3]==0:
                board[i][e][1]=False
    return [length,score]
                
                
#game loop
gip=1
while gip==1:
    for i in range(16):
        for e in range(16):
            if board[i][e][2]==True:
                snake_head_pos_x=i
                snake_head_pos_y=e
                print(i,e)
    
    print_score(score)
    print_board(board)
    x=play_move(board,tail_direction,snake_head_pos_x,snake_head_pos_y,length,score)
    length,score=x[0],x[1]
    clear_output(wait=True)




