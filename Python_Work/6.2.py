favorite_number = {
        'nickd': [8, 69],
        'garrett': [22, 69],
        'yunus': [69, 420],
        'justin': [4, 12],
        'sheb': [7, 25, 62]
        }

for name, numbers in favorite_number.items():
    print(f"\n{name.title()} favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")