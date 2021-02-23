import math
from numpy.testing import assert_almost_equal
import unittest
import pytest

class tests(unittest.TestCase):
    T_HALF = 5730
    DECAY_CONSTANT = -0.693

    def get_age_carbon_14_dating(self,carbon_14_ratio):
        """Returns the estimated age of the sample in year.
        carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
        in the sample conpared to the amount in living 
        tissue (unitless)."""
        if isinstance(carbon_14_ratio, int) or isinstance(carbon_14_ratio, float):
            return math.log(carbon_14_ratio) / self.DECAY_CONSTANT * self.T_HALF 
        raise TypeError('value passed in must be of type "int" or "float"')

    # TODO: Write a unit test which feed 0.35 to the function. 
    # The result should be '8680.34'. Does the function handles 
    # every possible input correctly? What if the input is zero
    # or negative?
    # Add the necessary logic to make sure the function handle 
    # every possible input properly. Then write a unit test againt 
    # this special case.

    def test_compare_float(self):
        assert_almost_equal(self.get_age_carbon_14_dating(0.35), 8680.34,decimal=2)

    def test_get_assertion_error(self):
        with self.assertRaises(TypeError):
            self.get_age_carbon_14_dating('string')
