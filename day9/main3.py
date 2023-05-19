# Adding a dictionary to the list
travel_log = [
    {
        'country' : 'Lagos',
        'cities_visited' : ['Lagos', 'Ogun'],
        'total_visits' : 10,
    },
    {   
        'country' : 'France',
        'cities_visited' : ['Paris', 'Lille', 'Dijon'],
        'total_visits' : 12,
    },
    {   
        'country' : 'Germany',
        'cities_visited' : ['Berlin', 'Hamburg', 'Frankfurt'],
        'total_visits' : 5,
    }
]

def add_new_country(country_visted, cities_visited, times_visited):
    new_country = {}
    new_country['country'] = country_visted
    new_country['cities'] = cities_visited
    new_country['visits'] = times_visited
    travel_log.append(new_country)

add_new_country('Russia', ['Moscow', 'Saint Petersburg'], 2)
print(travel_log)