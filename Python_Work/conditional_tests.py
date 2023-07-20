age = 26
print("Is my age 25?")
print(age == 25)

print("\nIs my age 26?")
print( age == 26)

name = 'Keven'
print(name.lower() == 'keven')

number_0 = 20
number_1 = 25
print(number_0 >= 22 or number_1 <= 22)
print(number_0 >= 21 and number_1 <= 21)

players = ['nickd', 'garrett', 'deming', 'sheb']
print('sheb' in players)
player = 'keagan'
if player not in players:
    print(f"{player.title()}, you are not a player.")