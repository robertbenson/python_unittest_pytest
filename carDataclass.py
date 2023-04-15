from dataclasses import dataclass
from Exception7Wheel import Exception7Wheel

@dataclass
class Car:
    drive: str
    wheels: int
    color: str

    def __post_init__(self):
        if not isinstance(self.drive, str):
            raise TypeError('Drive should be of type str')

        if not isinstance(self.color, str):
            raise TypeError('Color should be of type str')

        if not isinstance(self.wheels, (int,float) ):
            msg = 'Wheels should be of type int or float: value passed was {}'.format(self.wheels)
            raise TypeError(msg)

        if self.wheels < 2 or self.wheels > 10:
            msg = 'Wheels must be 2 - 10: value passed was {}'.format(self.wheels)
            raise ValueError(msg)

        if self.wheels == 7:
            raise ValueError('Wheels must not be 7 !!!!!')

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

    make_car('manual', 7, 'red')  # will raise custom exception
    make_car('manual', '1a', 'yellow')  # will raise        exception , type error
    make_car('manual', 12, 'blue')      # will raise        exception , value error
    make_car('manual', 1, 'blue')       # will raise        exception , value error
    make_car('manual', 1, 1234)         # will raise        exception , type error

    make_car('auto', 4, 'grey')  # will make a valid car

if __name__ == '__main__':
    main()