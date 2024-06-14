# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is *z*."

print("The Love Calculator is calculating your score...")
name1 = input("What is girl name: ")
name2 = input("What is boy name: ")

count1 = 0
count2 = 0
girl = name1.lower()
boy = name2.lower()

count1 += girl.count("t")
count1 += girl.count("r")
count1 += girl.count("u")
count1 += girl.count("e")
count1 += boy.count("t")
count1 += boy.count("r")
count1 += boy.count("u")
count1 += boy.count("e")

count2 += boy.count("l")
count2 += boy.count("o")
count2 += boy.count("v")
count2 += boy.count("e")
count2 += girl.count("l")
count2 += girl.count("o")
count2 += girl.count("v")
count2 += girl.count("e")

number = int(str(count1)+str(count2))
if number < 10 or number>90:
  print(f"Your score is {number}, you go together like coke and mentos.")
elif number>40 and number<50:
  print(f"Your score is {number}, you are alright together.")
else:
  print(f"Your score is {number}.")