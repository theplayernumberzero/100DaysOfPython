#assume that you will die 90 years old 

age = int(input("How old are you:\n"))

years_left = 90 - age
weeks_left = years_left * 52

print(f"You have {weeks_left} weeks left.")