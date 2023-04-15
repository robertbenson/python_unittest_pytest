from dataclasses import dataclass

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