# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 22:51:37 2019

@author: SOOMRO
"""
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])
    
def check_result(board,player_Tag):
    if board[9]==board[8]==board[7]==player_Tag or board[4]==board[5]==board[6]==player_Tag or board[1]==board[2]==board[3]==player_Tag or board[7]==board[4]==board[1]==player_Tag or board[8]==board[5]==board[2]==player_Tag or board[9]==board[6]==board[3]==player_Tag or board[7]==board[5]==board[3]==player_Tag or board[1]==board[5]==board[9]==player_Tag:
        return "Congratulations! "+ player_Tag + " has won the game!"
    elif " " in board:
        return " "
    else:
        return "It's a tie!"
        
print("Welcome to Tic Toe!")
start=input("Would you like to play? Yes or no?:" )
Player1_Tag=input("Player 1: Choose between X and 0: ")

while Player1_Tag != "X" and Player1_Tag != "0":
    print("Invalid input")
    Player1_Tag=input("Player 1: Choose between X and 0: ")
else:
    if Player1_Tag=="X":
        Player2_Tag="0"
    else:
        Player2_Tag="X"

board=["#"]+[" "]*9


while start=="Yes":
    board=["#"]+[" "]*9
    for i in range(9):
        if i%2==0:
           marker=Player1_Tag
        else:
           marker=Player2_Tag
        board_input=int(input("Choose a position (1-9): "))
        board[board_input]=marker ##depending on i
        display_board(board)        ##need to somehow find a way to stop this when the game has been won
        if i>=4 and check_result(board,marker)!=" ":
           print(check_result(board,marker))
           break
    start=input("Would you like to play? Yes or no?:" )
        
    
    
    
    
    
    

    
    
