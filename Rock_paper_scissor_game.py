import random
items_list = ["rock","paper","scissors"]

user_choice = input("Enter your choice from(rock,paper,scissors): ")
comp_choice = random.choice(items_list)
print(f"your choice is {user_choice} and computer choice is {comp_choice}")

if user_choice == comp_choice:
    print("Both choices are same, it's a tie!")
elif user_choice =="rock":
    if comp_choice =="paper":
        print("Paper covers rock, computer wins!")
    else:
        print("Rock crushes scissors, you wins!")

elif user_choice =="paper":
    if comp_choice =="scissor":
        print("scissor cuts the paper so computer wins!")
    else:
        print("paper covers the rock so you wins!")

elif user_choice == "scissors":
    if comp_choice == "paper":
        print("scissors cuts the paper so you wins!")
    else:
        print("rock crushes scissors so computer wins!")