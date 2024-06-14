print("Welcome to the rollercoaster")
height = int(input("Enter your height in cm: "))

bill = 0
if height > 120:
    print("You can hop in!")
    age = int(input("What is your age: "))
    if age<12:
        bill=10
        print("Child tickets are 10₺")
    elif age<=18:
        bill=15
        print("Youth tickets are 15₺")
    else:
        bill=20
        print("Adult tickets are 20₺")

    wants_photo = input("Do you want a photo taken (Y/N): ")

    if wants_photo == "Y" or wants_photo == "y":
        bill += 5
    
    print(f"Your bill is {bill} $")
else:
    print("Sorry you need to be taller :( ")