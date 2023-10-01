""" configuration test file """

import pytest

from clasepython.model.car import Car

@pytest.fixture()
def car():
    return Car('BMW', 2003, 4)



