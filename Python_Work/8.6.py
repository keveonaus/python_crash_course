def get_city_country(city, country):
    """Returning the city and country"""
    location = f"{city}, {country}"
    return location.title()

while True:
    print("\nGive me a city and the country it is in.")
    print("(enter 'q' at any time to quit)")

    city = input("City: ")
    if city == 'q':
        break

    country = input("Country: ")
    if country == 'q':
        break

    city_country = get_city_country(city, country)
    print(city_country)