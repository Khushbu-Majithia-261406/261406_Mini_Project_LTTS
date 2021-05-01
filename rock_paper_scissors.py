"""
ROCK_PAPER_SCISSORS GAME MINI PYTHON PROJECT"
"""

import random
import sys


def game():
 
    """
    Playing the game with the computer
    """

    winner = 0
    # 0:- user win, 1:- computer win, 2:- tie

    rules_win = {"rock":"scissor", "scissors":"paper", "paper":"rock"}
    rules_loose = {"rock":"paper", "scissors":"rock", "paper":"scissors"}

    userchoice = ["rock","paper","scissors"]

    print()
    userinput = input(" *** choose from 1. rock, 2. paper, 3. scissors:-  ")

    choices = ["rock", "paper", "scissors"]
    computerinput = random.choice(choices)

    #not converted to int as user may type any character other than digits also
    if(userinput not in ('1','2','3')):
        print("    enter from given choices only   ")
        game()

    else:
        userinput = int(userinput)
        userchoose = userchoice[userinput-1]
        print()
        print("   your input = ", userchoose)
        print()
        print("   computer input = ",computerinput)


        #valid choice
        if(userinput==1 or userinput==2 or userinput==3):
            if(computerinput==userchoose):
                winner = 2

            else:
                if(rules_win[userchoose]==computerinput):
                    winner = 0

                elif(rules_loose[userchoose]==computerinput):
                    winner = 1

        


        else:
            print()
            print("   *** invalid  ***  ")
            game()



        #declaring winner
        if(winner==0):
            print()
            print(" *** congrats you won *** ")


        elif(winner==1):
            print()
            print(" *** sorry you lost *** ")


        else:
            print()
            print(" *** it is a tie *** ")



        print()
        nextinput=input(" *** press 1 to play again and any other key to exit:-  ")

        if(nextinput=='1'):
            game()


        else:
            print()
            print("   HOPE YOU ENJOYED.  BYE!!!  ")
            sys.exit()



def login():
    
    """
    Logging into the system
    """

    print()
    print(" *** please enter your login credentials ***")
    print()
    username = input(" enter your username:- ")
    password = input(" enter your password:- ")


    #validate from txt file
    s=""
    s+=username
    s+=" "
    s+=password
    
    validate=0
    with open('users.txt') as f:
        lines = f.readlines()
        
        for l in lines:
            l = l.rstrip()
            if s==l:
                validate=1
                break


    if(validate==0):
        print("\n *** wrong credentials, login again  ")
        login()

    else:
        print("\n *** Logged in successfully  ")
        print()
        game()






def registration():
    
    """
    Registering into the systen
    """

    print()
    print(" *** please register yourself ***")
    print()
    username = input("    set a username:-  ")
    password = input("    set a password:-  ")

    #write into file
    f=open('users.txt','a')

    string=""
    string+=username
    string+=" "
    string+=password
    f.write(string+"\n") 
    f.close()


    print()
    print(" *** registered successfully ***")
    print()
    login()



def welcome():
    """
    Welcome page for the project
    """
    print("\n *** Welcome to rock_paper_scissors game ***\n")

    print("1. registration")
    print("2. login")
    print()

    choice = input()

    if(choice=='1'):
        registration()

    elif(choice=='2'):
        login()

    elif(choice==3):
        exit
    else:
        print()
        print("\n *** please select from above choices only ***\n")
        welcome()
   




welcome()


    





    
