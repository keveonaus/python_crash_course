pizzas = ['bbq chicken', 'smoky', 'pepperoni', 'cheese', 'everything', 'sausage']
for pizza in pizzas:
    print(f"I really really like {pizza}, espically after the bars.")

print("I really love pizza")

print("Here are the first three items:")
for pizza in pizzas[:3]:
    print(pizza)

print("Here are the three items in the middle:")
for pizza in pizzas[1:3]:
    print(pizza)

print("Here are the last three items:")
for pizza in pizzas[3:]:
    print(pizza)

friend_pizza = pizzas[:]

pizzas.append('chicken')
friend_pizza.append('puke')

print(f"My favorite pizzas are: ")
print(pizzas)

print("My friends favorite pizzas are: ")
print(friend_pizza)