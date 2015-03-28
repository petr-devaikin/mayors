from peewee import *

db = SqliteDatabase('mayors.db')


class Region(Model):
    name = CharField(unique=True)

    class Meta:
        database = db


class City(Model):
    name = CharField()
    region = ForeignKeyField(Region, related_name='cities')
    population_2013 = IntegerField()
    population_2014 = IntegerField()
    population_avg_2013 = IntegerField()
    mayor = CharField(null=True)

    class Meta:
        database = db
        indexes = (
            (('name', 'region'), True),
        )


if __name__ == '__main__':
    print 'Create tables'
    Region.create_table()
    City.create_table()