import random


names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")


num_items = len(names)
print(f"total number of people {num_items}")
random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal tomorrow")

