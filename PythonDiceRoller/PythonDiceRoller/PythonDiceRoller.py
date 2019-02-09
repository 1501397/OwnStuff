import random
import sys
import os

print("choose a die: \n 1 = d4 \n 2 = d6 \n 3 = d8 \n 4 = d10 \n 5 = d12 \n 6 = d20 \n 7 = d100 \n or 0 to quit program")

u_input = input()
  

while u_input != "0":

    

    if u_input == "1":
        print("rolled a: [", random.randrange(1, 5), "] on a d4")
        u_input = input()

    if u_input == "2":
        print("rolled a: [", random.randrange(1, 7), "] on a d6")
        u_input = input()

    if u_input == "3":
        print("rolled a: [", random.randrange(1, 9), "] on a d8")
        u_input = input()

    if u_input == "4":
        print("rolled a: [", random.randrange(1, 11), "] on a d10")
        u_input = input()

    if u_input == "5":
        print("rolled a: [", random.randrange(1, 13), "] on a d12")
        u_input = input()

    if u_input == "6":
        print("rolled a: [", random.randrange(1, 21), "] on a d20")
        u_input = input()

    if u_input == "7":
        print("rolled a: [", random.randrange(1, 101), "] on a d100")
        u_input = input()
    elif u_input >= "8" or u_input <= "-1":
        print ("---invalid input---")
        u_input = input()
    

