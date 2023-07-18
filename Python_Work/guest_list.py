dinner = ['Trump', 'Sydney Sweeney', 'Giannis']

print(f"Hope all is well Mr. {dinner[0]}, would you like to have dinner tomorrow night?")

print(f"Please, please, please come to dinner with me {dinner[1]}. It would mean the world to me.")

print(f"Mr. {dinner[2]}, it would mean the world to me if you would come to my dinner party tomorrow night.")

print(f"Unfortunately Mr. {dinner[0]} can not make the dinner.")

dinner.remove('Trump')
dinner.insert(0, 'Avicii')

print(f"Hey {dinner[0]}, would you be able to make it to dinner tomorrow night?")

print(f"Hey, {dinner[1]}, Trump can no longer make the dinner party but are you still able to make it?")

print(f"Hey {dinner[2]}, Trump can no longer make the dinner party. Are you still able to?")

print("I have found a bigger table for the dinner party!")

dinner.insert(0, 'Nickd')
dinner.insert(3, 'Yunus')
dinner.insert(5, 'Garrett')

print(f"Hey {dinner[0]}, would you like to come to a dinner party tomorrow night at 7pm?")

print(f"Hey {dinner[1]}, would you like to come to a dinner party tomorrow night at 7pm?")

print(f"Hey {dinner[2]}, would you like to come to a dinner party tomorrow night at 7pm?")

print(f"Hey {dinner[3]}, would you like to come to a dinner party tomorrow night at 7pm?")

print(f"Hey {dinner[4]}, would you like to come to a dinner party tomorrow night at 7pm?")

print(f"Hey {dinner[5]}, would you like to come to a dinner party tomorrow night at 7pm?")

print("Sadly the table will not be making it in time for the party. I only have room for two people")

popped_guest1 = dinner.pop(0)
print(f"Sorry, {popped_guest1}, you are no longer invited")

popped_guest2 = dinner.pop(0)
print(f"Sorry, {popped_guest2}, you are no longer invited")

popped_guest3 = dinner.pop(0)
print(f"Sorry, {popped_guest3}, you are no longer invited")

popped_guest4 = dinner.pop(0)
print(f"Sorry, {popped_guest4}, you are no longer invited")

print(f"Hey {dinner[0]}, and {dinner[1]} you two are still invited to tomorrows dinner party")

dinner.remove('Giannis')
dinner.remove('Garrett')
print(dinner)

size = len(dinner)
print(size)