import random
 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
 
repeat = "Y"
myScore = 0
computerScore = 0
while repeat == "Y":
    print('Welcome to Rock, Paper, Scissors')
    userChoice = int(input('Choose 1 for Rock, 2 for Paper, and 3 for Scissors: '))-1
    rockPaperScissors = [rock, paper, scissors]
    computerChoice = random.randint(0,2)
    print(f"You chose:\n {rockPaperScissors[userChoice]}.")
    print(f'The computer chose:\n {rockPaperScissors[computerChoice]}.')
    if userChoice == 0:
        if computerChoice == 0:
            print("It's a tie. Two rocks!")
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
        elif computerChoice == 1:
            print("You lose. Paper covers rock.")
            computerScore = computerScore + 1
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
        elif computerChoice == 2:
            print("You win. Rock bashes scissors.")
            myScore = myScore + 1
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
    elif userChoice == 1:
        if computerChoice == 0:
            print("You win. Paper covers rock.")
            myScore = myScore + 1
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
        elif computerChoice == 1:
            print("It's a draw. Two sheets of paper.")
        elif computerChoice == 2:
            print("You lose. Scissors cuts paper.")
            computerScore = computerScore + 1
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
    elif userChoice == 2:
        if computerChoice == 0:
            print("You lose. Rock bashes scissors!")
            computerScore = computerScore + 1
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
        elif computerChoice == 1:
            print("You win. Scissors cut paper!")
            myScore = myScore + 1
            print(f"Your score: {myScore}    | Computer's score: {computerScore}")
        elif computerChoice == 2:
            print("It's a draw. Two pairs of scissors!")
    repeat = input("Do you want to play again? Y | N : ").upper()
print("Thank you for playing!")
exit()