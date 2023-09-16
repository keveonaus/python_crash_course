def describe_city(city, country='italy'):
    """Naming a city and the country it's in"""
    print(f"\n{city.title()} is in {country.title()}.")

describe_city('rome')
describe_city('naples')
describe_city(city='geneva', country='switzerland')