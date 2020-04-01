# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:53:11 2020

@author: Supriyo
"""
import random
import os
os.system("cls")

class player():
    def __init__(self):
        #Tossing for choosing the first player
        toss = random.randint(0,1)
        if toss == 0:
            self.currentPlayer = 'X'
        else:
            self.currentPlayer = 'O'
    
    def changePlayer(self,current):
        if current == "X":
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'
    
    def __str__(self):
        return self.currentPlayer

 
        
    
    
    
class Board():
    def __init__(self):
        self.cells = [' ']*9
        self.available = [str(num) for num in range(1,10)]
        
    def display(self):
        print(" %s | %s | %s "%(self.cells[0],self.cells[1],self.cells[2]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[3],self.cells[4],self.cells[5]))
        print("-----------")
        print(" %s | %s | %s "%(self.cells[6],self.cells[7],self.cells[8]))
        print("\nAvailable moves!\n")
        print(" %s | %s | %s "%(self.available[0],self.available[1],self.available[2]))
        print("-----------")
        print(" %s | %s | %s "%(self.available[3],self.available[4],self.available[5]))
        print("-----------")
        print(" %s | %s | %s "%(self.available[6],self.available[7],self.available[8]))
    
    def place_marker(self,cell_number,currentPlayer):
        if(self.cells[cell_number-1]==" "):    
            self.cells[cell_number-1] = currentPlayer
            self.available[cell_number-1] = " "

    def check_winner(self):
            #1st Row Check
            if (self.cells[0]==self.cells[1]==self.cells[2] != ' '):
                print("%s is the winner"%(self.cells[0]))
                return True 
            #2nd Row Check
            elif(self.cells[3]==self.cells[4]==self.cells[5] != ' '):
                print("%s is the winner"%(self.cells[3]))
                return True
            #3rd Row Check
            elif(self.cells[6]==self.cells[7]==self.cells[8] != ' '):
                print("%s is the winner"%(self.cells[6]))
                return True
            #1st Column Check
            elif(self.cells[0]==self.cells[3]==self.cells[6] != ' '):
                print("%s is the winner"%(self.cells[0]))
                return True
            #2nd Column Check
            elif(self.cells[1]==self.cells[4]==self.cells[7] != ' '):
                print("%s is the winner"%(self.cells[1]))
                return True
            #3rd Column Check
            elif(self.cells[2]==self.cells[5]==self.cells[8] != ' '):
                print("%s is the winner"%(self.cells[2]))
                return True
            #2ndary Diagonal Check
            elif(self.cells[0]==self.cells[4]==self.cells[8] != ' '):
                print("%s is the winner"%(self.cells[0]))
                return True
            #Principal Diagonal Check
            elif(self.cells[2]==self.cells[4]==self.cells[6] != ' '):
                print("%s is the winner"%(self.cells[2]))
                return True
            #Tie and continue playing check
            else:
                if ' ' not in self.cells:
                    print("Board is full!! and the game tied!!!")
                    return True
                else:
                    return False


def print_header():
    print("Welcome to TIC TAC TOE\n")
 

def refresh_screen(board):
    #clear the screen
    os.system("cls")
    #print the header 
    print_header()
    #display the board 
    board.display()

def Replay():
    x = input("Do you want to replay (yes or no)? ")
    return x[0].lower() == 'y'
        
    

board = Board()
Player = player()
currentPlayer = Player.__str__()

    
while True:

    while not board.check_winner():
        refresh_screen(board)
        while True:
            try:    
                cell_no = int(input("Enter the availabel cell no : "))
            except:
                print("Please enter a integer value!!!")
                continue
            else:
                break
        board.place_marker(cell_no, currentPlayer)
        Player.changePlayer(currentPlayer)
        currentPlayer = Player.__str__()

    refresh_screen(board)
    board.check_winner()
    del board
    del Player 

    if not Replay():
        print("Thanks for playing!!")
        break

    board = Board()
    Player = player()
    currentPlayer = Player.__str__()   