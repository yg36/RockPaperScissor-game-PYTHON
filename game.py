import random

def main():
    print("lets play rock, paper, scissors")

    while True:
        user_choice= get_user_choice()
        computer_choice=get_computer_choice()

        print("you chose "+ user_choice)
        print("the computer chose " + computer_choice)
        result= winner(user_choice, computer_choice)
        print(result + "\n would you like to play again")
        continue_game = input("yes/no")
        if continue_game=="no":
            break
        else:
            main()

def get_user_choice():
    while True:
        user_choice= input ("rock, paper, scissors: ")
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("invalid choice")

def get_computer_choice():
    choices=["rock", "paper", "scissors"]
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if(user_choice==computer_choice):
        return "its a tie"
    elif((user_choice=="rock" and computer_choice=="scissors") or
         (user_choice=="scissors" and computer_choice=="paper") or 
         (user_choice=="paper" and computer_choice=="rock")):
        return "you win!"
    else:
        return "computer wins!"
    
main()
