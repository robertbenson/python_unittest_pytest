import main
from Exception7Wheel import Exception7Wheel
from main import Car
import unittest
import pytest

class TestCar(unittest.TestCase):
    def test_get_number_wheels(self):
        carWheelsInvalidlt1 = Car('manual', 4, 'blue')
        assert carWheelsInvalidlt1.number_wheels() == 4

    def test_invalid_wheels_gt_10_valueError(self):
        with self.assertRaises(ValueError):
            carWheelsInvalidlt1 = Car('manual', 11, 'blue')

    def test_invalid_7_wheels(self):
        with self.assertRaises(Exception7Wheel):
            carWheelsInvalidlt1 = Car('manual', 7, 'blue')

    def test_invalid_wheels_lt_2_pytest_message(self):
        # check same attributes, but this time check message produced
        with pytest.raises(ValueError, match="Wheels must be 2 or more, #wheels : 1"):
            carWheelsInvalidlt1 = Car('manual', 1, 'blue')


    def test_PYTEST_invalid_wheels_lt_2_valueError(self):
        # check the actual message thrown by valueError
        with pytest.raises(ValueError, match="Wheels must be 2 or more, #wheels : 1"):
            carWheelsInvalidlt1 = Car('manual', 1, 'blue')

    def test_PYTEST_invalid_wheels_gt_10_valueError(self):
        # check the actual message thrown by valueError
        with pytest.raises(ValueError, match="Wheels must be 10 or less, #wheels :  11"):
            carWheelsInvalidlt1 = Car('manual', 11, 'blue')

    def test_invalid_wheels_invalid_type_error(self):
        # check TypeError: number wheels must be integer or float
        with self.assertRaises(TypeError):
            carWheelsInvalidlt1 = Car('manual', '23d', 'blue')

    def test_manual_red_4_car(self):
        carRed = Car('manual', 4, 'red')
        # print(carRed.colour)
        # carRed.car_details()
        self.assertEqual(carRed.drive,'manual')
        self.assertEqual(carRed.color,'red')
        self.assertEqual(carRed.wheels,4)


    def test_blue_car_float(self):
        carBlue = Car('manual', 3.0, 'blue')
        # print(carRed.colour)
        # carRed.car_details()
        self.assertEqual(carBlue.drive, 'manual')
        self.assertEqual(carBlue.color, 'blue')
        self.assertEqual(carBlue.wheels, 3)

