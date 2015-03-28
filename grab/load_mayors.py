from models import *

with open('data/heads.txt') as f:
    for line in f:
        data = line.split('\t')
        city = City.get(City.id == data[0])
        city.mayor = data[1]
        city.save()