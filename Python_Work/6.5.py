rivers = {
        'nile': 'egypt',
        'missippi': 'usa',
        'yangtze': 'china',
}
for river in rivers:
    print(f"{river.title()}.")

for country in rivers.values():
    print(f"{country.title()}")