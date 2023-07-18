sports_teams = ['packers', 'bucks', 'brewers', 'badgers', 'marquette']

print(f"{sports_teams[4]} you suck and are off the list")

sports_teams.remove('marquette')

sports_teams.insert(4, 'milwaukee')

print(sports_teams)

print(sorted(sports_teams))

print(sorted(sports_teams, reverse=True))

badgers = sports_teams.pop(3)
print(badgers)