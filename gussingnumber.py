#Number guessing game in python
import random as rd
print("Let's start the game!!")
a=int(input("enter the starting value:"))
b=int(input("enter the ending value:"))
print("---Only the 5 guess!---")
original_number=rd.randrange(a,b)
i=0
while i<=5:
    guess_number=int(input(f"\nEnter the {i} guessing number: "))
    if (guess_number==original_number):
        print("WOW! You guess the correct answer.")
        break
    elif (guess_number>original_number):
        print("Oops! You guess is higher")
        i+=1
    elif (guess_number<original_number):
        print("Oops! You guess is lower")
        i+=1

print("============================")
print(f"the number is {original_number}")

#print(b,a,"\n",original_number)