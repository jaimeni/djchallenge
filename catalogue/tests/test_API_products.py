from django.test import TestCase

from catalogue.utils import validate_range_price


class BaseUnityTest(TestCase):

    def test_validate_range_correct(self):
        validate = validate_range_price(value_min=25, value_max=55)
        self.assertEqual(validate, True)

    def test_validate_range_incorrect_decimals(self):
        validate = validate_range_price(value_min=25, value_max=5)
        self.assertEqual(validate, False)

    def test_validate_range_incorrect_type_value(self):
        validate = validate_range_price(value_min='cuatro', value_max=55)
        self.assertEqual(validate, False)
