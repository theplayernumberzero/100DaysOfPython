print("Welcome to the math island")

choice1 = int(input("Which number is bigger: 25, 43, 24\n"))

if choice1 == 43:
    print("That is true!!")
    choice2 = input("Is 5 time 6 equal to 30. Type 'yes' or 'no'\n").lower()
    if choice2 == "yes":
        print("That is true!!")
        choice3 = input("Is 0 equal to natural number. Type 'yes' or 'no'\n").lower()
        if choice3 == "no":
            print("That is true!!")
            print("YOU WON THE GAME!!")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")