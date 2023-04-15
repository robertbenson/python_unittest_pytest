from dataclasses import dataclass
from Exception7Wheel import Exception7Wheel
from Car import Car


def make_car(drive, wheels , color='gold'):
    # make car using attributes provided
    try:
        car = Car(drive, wheels, color)
        print('car made successfully' , car)
    except ValueError as v:
        print('ValueError raised:', v)
    except TypeError as t:
        print('TypeError raised: ', t)
    except Exception7Wheel as e:
        print('No 7 wheel cars allowed!!! : ', e)


def main():

    make_car('manual', 7, 'red')        # will raise custom exception
    make_car('manual', '1a', 'yellow')  # will raise        exception , type error
    make_car('manual', 12, 'blue')      # will raise        exception , value error
    make_car('manual', 1, 'blue')       # will raise        exception , value error
    make_car('manual', 1, 1234)         # will raise        exception , type error

    make_car('auto', 4, 'grey')  # will make a valid car

if __name__ == '__main__':
    main()