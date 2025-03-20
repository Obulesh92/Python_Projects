'''-------------------------Rock,Paper,Sessior---------------------------'''
#some basic game wining and losing rules given below:
''' 
    First_person    second_person       first_person win/lose
    (user_choice)   (computer_choice)   user_choice win/lose

    rock            rock                ->Draw
    paper           paper               ->Draw
    sessior         sessior             ->Draw
    rock            paper               ->you lose
    rock            sessior             ->you win
    paper           sessior             ->you lose
    paper           rock                ->you win
    sessior         rock                ->you lose
    sessior         paper               ->you lose
'''

import random as rd 
#random module for second person

user_choice=int(input("0 is rock,1 is paper,2 is sessior:"))
#user_choice is a input for first person
computer_choice=rd.randint(0,2)
#computer_choice is for second person.second person in program is random

print(f"computer choice  is {computer_choice}")

if user_choice == computer_choice:
    print("It is Draw")
    #rock            rock                ->Draw
    # paper           paper               ->Draw
    # sessior         sessior             ->Draw
elif user_choice==0:
    if computer_choice==2:
        print("You Win")
    else:
        print("You Lose")
elif user_choice==1:
    if computer_choice==0:
        print("You Win")
    else:
        print("You Lose")
elif user_choice==2:
    print("You Lose")
