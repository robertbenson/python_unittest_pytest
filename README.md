# Python dataclass unittest pytest example

This is a simple example that shows how to unittest, pytest a class.

It's a Car class that takes drive, wheels and color as attributes.

The Car factory can make cars with 2 to 10 wheels, but not 7 wheels. 

The owner had a bad experience in a 7 wheeler and has banned them.

The wheel attribute must be an integer or float.
The color must be a string.

# Working code


main.py - how to use dataclass using car example   
car.py - car dataclass
```python 
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
```

TestCar.py - unittest and pytests

## TDD - Test-driven development 

Red — think about what you want to develop, make a failing test

Green — think about how to make your tests pass

Refactor — think about how to improve your existing implementation
 

## pytest - a testing framework

note the use of pytest to detect actual ValueError message.

The unit testing is in the testClass.py file

    

```python
    def test_PYTEST_invalid_wheels_gt_10_valueError(self):
        with pytest.raises(ValueError, match="Wheels must be 10 or less: 11"):
            carWheelsInvalidlt1 = Car('manual', 11, 'blue')
```

## Exceptions  - wrap objects to detect exceptions

### ValueError and TypeError

```python
    try:
        car = Car(drive, wheels, color)
        print('car made successfully' , car)
    except ValueError as v:
        print('ValueError raised:', v)
    except TypeError as t:
        print('TypeError raised: ', t)
    except Exception7Wheel as e:
        print('No 7 wheel cars allowed!!! : ', e)
    
```

### Custom Exception (Exception7Wheel.py)

```python
    class Exception7Wheel(Exception):
    pass
```



# Output - from main.py
```
ValueError raised: Wheels must not be 7 !!!!!
TypeError raised:  Wheels should be of type int or float: value passed was 1a
ValueError raised: Wheels must be 2 - 10: value passed was 12
ValueError raised: Wheels must be 2 - 10: value passed was 1
TypeError raised:  Color should be of type str
car made successfully Car(drive='auto', wheels=4, color='grey')
car made successfully Car(drive='auto', wheels=3.0, color='purple')
``` 
# Output - from TestCar.py
```
============================= test session starts =============================
collecting ... collected 7 items

TestCar.py::TestCar::test_PYTEST_invalid_wheels_gt_10_valueError PASSED  [ 14%]
TestCar.py::TestCar::test_PYTEST_invalid_wheels_lt_2_valueError PASSED   [ 28%]
TestCar.py::TestCar::test_typeerror_wheels PASSED                        [ 42%]
TestCar.py::TestCar::test_valid_car_wheels_float PASSED                  [ 57%]
TestCar.py::TestCar::test_valid_car_wheels_int PASSED                    [ 71%]
TestCar.py::TestCar::test_valueerror_wheels_1 PASSED                     [ 85%]
TestCar.py::TestCar::test_valueerror_wheels_11 PASSED                    [100%]

======================== 7 passed, 1 warning in 0.02s =========================