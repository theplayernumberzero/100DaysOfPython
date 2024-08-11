import random

friends = ["Uzay", "Ertan", "Çağrı", "İbo", "Meltem", "Yüsra", "Bahadir"]
random_number = random.randint(0, (len(friends)-1))

print(f"The name of the person who will pay bill is: {friends[random_number]}")
print(f"The name of the person who will take photo of event: {random.choice(friends)}")