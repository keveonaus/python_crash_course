cities = {
        'milwaukee': {
            'country': 'usa',
            'population': 569330,
            'fact': 'i live here'
        },
        
        'barcelona': {
            'country': 'spain',
            'population': 1620000,
            'fact': 'was the capital of spain from 1937 to 1939'
        },
        
        'lagos': {
            'country': 'nigeria',
            'population': 15946000,
            'fact': 'it has the tallest building in west africa'
        },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    fact = f"{city_info['fact']}"

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")