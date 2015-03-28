from models import *

citi_files = ['cities.csv', 'cities2.csv', 'cities3.csv', 'cities4.csv']

for city_file in citi_files:
    with open('data/' + city_file) as f:
        for line in f:
            city_data = line.split('\t')
            region = Region.get_or_create(name=city_data[2])
            try:
                City.create(
                    name=city_data[1].split(' ')[1],
                    region=region,
                    population_2013=int(city_data[3].replace(',', '')),
                    population_2014=int(city_data[4].replace(',', '')),
                    population_avg_2013=int(city_data[5].replace(',', '')),
                )
                print '%s added' % city_data[1]
            except peewee.IntegrityError:
                print '%s already exists' % city_data[1]