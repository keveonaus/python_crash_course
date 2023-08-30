age = input("\nHow old are you? ")
age = int(age)

if age < 4:
    print("\nYou're ticket is free!")
elif age < 13:
    print("\nYou're ticket is $10.")
else:
    print("\nYou're ticket is $12.")