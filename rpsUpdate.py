import random

t = ["Rock", "Paper", "Scissors"]

computer = t.index(random.choice(t))

player = False

def wincheck(Option_, Option):
    return Option_ > Option

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    else:
        print("That's not a valid play. Check your spelling!")
    player_option = t.index(player)
    who_won = wincheck(player_option, computer)
    print(who_won)
    

player = False

computer = t[randint(0,2)]
