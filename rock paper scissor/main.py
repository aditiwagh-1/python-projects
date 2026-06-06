import random

opt_list = ["Rock","Paper","Scissor"]
user_choice = input("Enter your move = (Rock, Paper, Scissor) = ").capitalize()
comp_choice = random.choice(opt_list)

print("you choose = {} and computer choosed = {}".format(user_choice,comp_choice))

if(user_choice == comp_choice):
    print(f"your choice = {user_choice} \ncomputer choice = {comp_choice}")
    print("match is tie ....")
elif user_choice == "Rock":
    if(comp_choice == "Paper"):
        print("paper covers rock = computer wins")
    else:
        print("Rock smashes scissor = you win")

elif(user_choice == "Paper"):
    if(comp_choice == "Scissor"):
        print("Scissor cuts paper =  computer wins")
    else:
        print("you win")

elif(user_choice == "Scissor"):
    if(comp_choice == "Rock"):
        print("computer win")
    else:
        print("you win") 