# Python dataclass unittest pytest example

This is a simple example that shows how to unittest, pytest a class.

It's a Car class that takes drive, wheels and color as attributes.

The Car factory can make cars with 2 to 10 wheels, but not 7 wheels. The owner had a bad experience in a 7 wheeler and has banned them.

The wheel attribute must be an integer or float.
The color attribute must be a string.

# Working code


main.py - how to use dataclass using car example

Car.py - car dataclass

CarTest.py - unittest and pytests

Exception7Wheel.py - custom exception

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
car made successfully Car(drive='auto', wheels=5, color='gold')
``` 
# Output - from TestCar.py
```
============================= test session starts =============================
collecting ... collected 8 items

TestCar.py::TestCar::test_PYTEST_invalid_wheels_7 
TestCar.py::TestCar::test_PYTEST_invalid_wheels_gt_10_valueError 
TestCar.py::TestCar::test_PYTEST_invalid_wheels_lt_2_valueError 
TestCar.py::TestCar::test_typeerror_wheels 
TestCar.py::TestCar::test_valid_car_wheels_float 
TestCar.py::TestCar::test_valid_car_wheels_int 
TestCar.py::TestCar::test_valueerror_wheels_1 
TestCar.py::TestCar::test_valueerror_wheels_11 

======================== 8 passed, 1 warning in 0.02s =========================