# This is a sample Python script.
from Exception7Wheel import Exception7Wheel

class Car:
    # A car object has drive, wheel and colour attributes                                                   v
    def __init__(self, drive, wheel, color):
        self.drive= drive
        if type(wheel) not in [int, float]:
            msg = "Wheels must be integers or floats, wheel value passed: " + str(wheel)
            raise TypeError(msg)
        if wheel < 2:
            msg = "Wheels must be 2 or more, #wheels : " + str(wheel)
            raise ValueError(msg)
        if wheel > 10:
            msg = "Wheels must be 10 or less, #wheels :  " + str(wheel)
            raise ValueError(msg)
        if wheel == 7:
            msg = "Wheels must not be 7, #wheels : " + str(wheel)
            raise Exception7Wheel(msg)
        self.wheels = int(wheel)
        self.color = color

    def getCarDetails(self):
        print(f"Car was made: Drive is {self.drive} ",f"#Wheels : {self.wheels} ",f"Color : {self.color} ")
            # print(f"Employee ID  : {self.id}")
    def number_wheels(self):
        return self.wheels


def make_car(drive, wheels , color='gold'):
    try:
        car = Car(drive, wheels, color)
        car.getCarDetails()
    except ValueError as v:
        print('ValueError raised:', v)
    except TypeError as t:
        print('TypeError raised: ', t)
    except Exception7Wheel as e:
        print('No 7 wheel cars allowed!!! : ', e)


def main():
    make_car('manual',7,'red')          # will raise custom exception
    make_car('manual','1a','yellow')    # will raise        exception , type error
    make_car('manual',12,'blue')        # will raise        exception , value error
    make_car('manual',1,'blue')         # will raise        exception , value error


    make_car('manual',4,'grey')         # will make a valid car

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

