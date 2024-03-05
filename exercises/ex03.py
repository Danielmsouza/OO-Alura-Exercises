'''Implement a class called Car with basic attributes such as model, color, and year'''
class Car:
    def __init__(self, model, collor, year):
        self.model = model
        self.collor = collor
        self.year = year

my_car = Car(model='Fusca', collor='Blue', year='1970')