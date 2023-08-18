favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

names = ['jen', 'nick', 'phil', 'pat']
for name in names:
    if name in favorite_languages:
        print(f"Thank you {name.title()} for taking the poll!")
    else:
        print(f"Hey {name.title()} could you please take the poll?")