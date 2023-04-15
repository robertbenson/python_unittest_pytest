from unittest import TestCase
import pytest

from Car import Car


class TestCar(TestCase):

    def test_typeerror_wheels(self):
        with self.assertRaises(TypeError):
            car = Car('auto', '1a', 'blue')

    def test_valueerror_wheels_1(self):
        with self.assertRaises(ValueError):
            car = Car('auto', 1, 'blue')

    def test_valueerror_wheels_11(self):
        with self.assertRaises(ValueError):
            car = Car('auto', 11, 'blue')
    def test_PYTEST_invalid_wheels_lt_2_valueError(self):
        # check the actual message thrown by valueError
        with pytest.raises(ValueError, match="Wheels must be 2 - 10: value passed was 1"):
            carWheelsInvalidlt1 = Car('manual', 1, 'blue')

    def test_PYTEST_invalid_wheels_gt_10_valueError(self):
        # check the actual message thrown by valueError
        with pytest.raises(ValueError, match="Wheels must be 2 - 10: value passed was 11"):
            carWheelsInvalidlt1 = Car('manual', 11, 'blue')

    def test_valid_car_wheels_float(self):
        carBlue = Car('manual', 3.0, 'blue')
        # print(carRed.colour)
        # carRed.car_details()
        self.assertEqual(carBlue.drive, 'manual')
        self.assertEqual(carBlue.color, 'blue')
        self.assertEqual(carBlue.wheels, 3)
    def test_valid_car_wheels_int(self):
        carBlue = Car('manual', 4, 'blue')
        # print(carRed.colour)
        # carRed.car_details()
        self.assertEqual(carBlue.drive, 'manual')
        self.assertEqual(carBlue.color, 'blue')
        self.assertEqual(carBlue.wheels, 4)
