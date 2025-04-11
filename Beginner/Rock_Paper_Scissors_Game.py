import random

option = ["Paper", "Scissor", "Rock"]

User_choice = input("Choose any option from Paper, Scissor, Rock = ")
Comp_choice = random.choice(option)

if User_choice == Comp_choice:
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("Match tie")

elif User_choice == "Rock" and Comp_choice == "Scissor":
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("User Win")

elif User_choice == "Rock" and Comp_choice == "Paper":
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("Computer Win")

elif User_choice == "Scissor" and Comp_choice == "Rock":
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("Computer Win")

elif User_choice == "Scissor" and Comp_choice == "Paper":
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("User Win")  

elif User_choice == "Paper" and Comp_choice == "Rock":
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("User Win")  

elif User_choice == "Paper" and Comp_choice == "Scissor":
    print(f"User Choice = {User_choice}, Computer Choice = {Comp_choice}")
    print("Computer Win")                