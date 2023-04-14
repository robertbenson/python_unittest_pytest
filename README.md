# Python unittest pytest example

This is a simple example that shows how to unittest, pytest a class.
It's a Car class that takes drive, wheels and color as attributes.

The factory can make cars with 2 to 10 wheels, but not 7 wheels. 

The owner had a bad experience in a 7 wheeler and has banned them.

The wheel parameter must be an integer or float.
 

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
        car.getCarDetails()
    except ValueError as v:
        print('ValueError raised:', v)
    except TypeError as t:
        print('TypeError raised: ', t)
    
```

### Custom Exception

#### define it (Exception7Wheel.py)

```python
    class Exception7Wheel(Exception):
    pass
```

#### raise it
```python
    if wheel == 7:
        msg = "Wheels must not be 7, number wheels: " + str(wheel)
        raise Exception7Wheel(msg)
```
#### catch it

```python
    try:
        car = Car('manual', 7, 'red')
    except Exception7Wheel:
        print('No 7 wheel cars allowed!!!')
```
# Output - from main.py
```
No 7 wheel cars allowed!!! :  Wheels must not be 7, #wheels : 7
TypeError raised:  Wheels must be integers or floats, wheel value passed: 1a
ValueError raised: Wheels must be 10 or less, #wheels :  12
ValueError raised: Wheels must be 2 or more, #wheels : 1
Car was made: Drive is manual  #Wheels : 4  Color : grey 
``` 
# Output - from testClass.py
```
============================= test session starts =============================
collecting ... collected 9 items

testClass.py::TestCar::test_PYTEST_invalid_wheels_gt_10_valueError PASSED [ 11%]
testClass.py::TestCar::test_PYTEST_invalid_wheels_lt_2_valueError PASSED [ 22%]
testClass.py::TestCar::test_blue_car_float PASSED                        [ 33%]
testClass.py::TestCar::test_get_number_wheels PASSED                     [ 44%]
testClass.py::TestCar::test_invalid_7_wheels PASSED                      [ 55%]
testClass.py::TestCar::test_invalid_wheels_gt_10_valueError PASSED       [ 66%]
testClass.py::TestCar::test_invalid_wheels_invalid_type_error PASSED     [ 77%]
testClass.py::TestCar::test_invalid_wheels_lt_2_pytest_message PASSED    [ 88%]
testClass.py::TestCar::test_manual_red_4_car PASSED                      [100%]

============================== 9 passed in 0.01s ==============================