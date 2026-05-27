#Max Rubenstein
#Rock Paper Scissors Game

#Func
global computer_pick
global choice_number
global wins
global losses
global ties
import random
wins = 0
losses = 0
ties = 0
def rock_paper_scissors():
    print("Welcome to ROCK PAPER SCISSORS!!!")
    decision()
    random_decision()
    who_wins()
    scoreboard()
def tie():
    global ties
    ties += 1
    print("There is a tie!")
def lose1():
    global losses
    losses +=1
    print("ROCK beats SCISSORS")
    print("You lose!")
def lose2():
    global losses
    losses +=1
    print("PAPER beats ROCK")
    print("You lose!")
def lose3():
    global losses
    losses +=1
    print("SCISSORS beats PAPER")
    print("You lose!")
def win1():
    global wins
    wins += 1
    print("ROCK beats SCISSORS")
    print("You win!")
def win2():
    global wins
    wins += 1
    print("PAPER beats ROCK")
    print("You win!")
def win3():
    global wins
    wins += 1
    print("SCISSORS beats PAPER")
    print("You win!")
def decision():
    global choice_number
    choice = input("Choose ROCK PAPER OR SCISSORS:  ")
    if choice == "ROCK":
        choice_number = 1
    elif choice == "PAPER":
        choice_number = 2
    elif choice == "SCISSORS":
        choice_number = 3
    else:
        print("Please try again and use all caps")
        decision()

def random_decision():
    global computer_pick
    computer_pick = random.randint(1,3) # 1 is rock 2 is paper 3 is scissors

def who_wins():
    global choice_number
    global computer_pick
    if computer_pick == choice_number:
        tie()
    elif computer_pick == 1 and choice_number == 2:
        win2()
    elif computer_pick == 1 and choice_number == 3:
        lose1()
    elif computer_pick == 2 and choice_number == 1:
        lose2()
    elif computer_pick == 2 and choice_number == 3:
        win3()
    elif computer_pick == 3 and choice_number == 1:
        win1()
    elif computer_pick == 3 and choice_number == 2:
        lose3()
def scoreboard():
    global wins
    global losses
    global ties
    print(wins, losses, ties)
#Main
while True:
    rock_paper_scissors()
    quit_or_not = input("Would you like to continue? Yes or No: ")
    if quit_or_not == "No":
        break
