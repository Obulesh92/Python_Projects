import random as rd
s="""Programming languages are emerging constantly and so are different methodologies 
Object oriented programming is one such methodology that has become quite popular 
over past few years"""
l=s.split(" ")
print(l)
original_value=rd.choice(l)
for i in range(0,len(original_value)):
    print("_\n")
n=input()
print("guess the letter:")
for j in range(0,len(original_value)):
    if original_value[j]==n:
        pass
print(original_value)