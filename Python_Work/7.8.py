sandwich_orders = ['blt', 'club', 'pastrami', 'fish', 'italian', 'pastrami', 'pastrami']
finished_sandwichs = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich")
    finished_sandwichs.append(current_sandwich)

print("\nThe following sandwichs have been made:")
for finished_sandwich in finished_sandwichs:
    print(finished_sandwich.title())