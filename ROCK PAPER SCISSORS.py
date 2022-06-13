import random

while True:
    choices = ["r","p","s"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors? (r for rock, p for paper, s for scissors): ").lower()

    if player == computer:
                print("computer: ", computer)
                print("player: ", player)
                print("Tie!")
    elif player =="r":
        if computer == "p":
                print("computer: ", computer)
                print("player: ", player)
                print("You Lose!")
        if computer == "s":
                print("computer: ", computer)
                print("player: ", player)
                print("You Win!")
    elif player =="s":
        if computer == "r":
                print("computer: ", computer)
                print("player: ", player)
                print("You Lose!")
        if computer == "p":
                print("computer: ", computer)
                print("player: ", player)
                print("You Win!")

    elif player =="p":
        if computer == "s":
                print("computer: ", computer)
                print("player: ", player)
                print("You Lose!")
        if computer == "r":
                print("computer: ", computer)
                print("player: ", player)
                print("You Win!")
        
    play_again = input("play again? (yes/no): ").lower()
    
    if play_again != "yes":     
        break

print("Bye! see you later")