import pytest
from KiSD_projekt1.src.galoise_field import *


def test_create_field_element():
    element1 = GaloisFieldElement(5, 9)
    element2 = GaloisFieldElement(5, 4)
    element3 = GaloisFieldElement(4, 4)
    element4 = GaloisFieldElement(3, 4)
    element5 = 4

    assert element1 == element2
    assert element1 != element3
    assert element1 != element4
    assert element1 != element5


def test_elements_generator():
    modulus = 2**8
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(7)
    element2 = generator.generate(256)
    element3 = generator.generate(261)

    assert element1.modulus == modulus
    assert element1.value == 7
    assert element2.modulus == modulus
    assert element2.value == 0
    assert element3.modulus == modulus
    assert element3.value == 5
    
def test_add_two_positive_elements():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(7)
    element2 = generator.generate(3)
    element3 = generator.generate(11)

    element4 = element1 + element2

    element1 += element3

    assert element4.value == 10
    assert element4.modulus == modulus
    assert element1.value == 2
    assert element1.modulus == modulus


def test_subtract_two_positive_elements():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(7)
    element2 = generator.generate(3)
    element3 = generator.generate(11)

    element4 = element1 - element2

    element1 -= element3

    assert element4.value == 4
    assert element4.modulus == modulus
    assert element1.value == 12
    assert element1.modulus == modulus


def test_element_is_not_from_the_same_field():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    modulus2 = 2**5
    generator2 = GaloisFieldGenerator(modulus2)
    element1 = generator.generate(7)
    element2 = generator2.generate(7)
    element3 = 7

    with pytest.raises(ValueError):
        element4 = element1 + element2
    with pytest.raises(ValueError):
        element4 = element1 - element2
    with pytest.raises(ValueError):
        element4 = element1 * element2
    with pytest.raises(ValueError):
        element4 = element1 + element3
    with pytest.raises(ValueError):
        element4 = element1 - element3
    with pytest.raises(ValueError):
        element4 = element1 * element3


def test_multiplying_two_positive_elements():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(7)
    element2 = generator.generate(3)
    element3 = generator.generate(11)

    element4 = element1 * element2

    element1 *= element3

    assert element4.value == 5
    assert element4.modulus == modulus
    assert element1.value == 13
    assert element1.modulus == modulus


def test_dividing_two_positive_elements():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(6)
    element2 = generator.generate(3)
    element3 = generator.generate(6)

    element4 = element1 / element2

    element1 /= element3

    assert element4.value == 2
    assert element4.modulus == modulus
    assert element1.value == 1
    assert element1.modulus == modulus


def test_power_two_positive_elements():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(2)
    element2 = generator.generate(3)
    element3 = generator.generate(5)

    element4 = element1 ** element2
    element5 = element1 ** element3

    assert element4.value == 8
    assert element4.modulus == modulus


def test_negate_element():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(9)
    element2 = generator.generate(3)
    element3 = (-element1) + element2
    element4 = (-element1) - element2
    element5 = (-element1) * element2
    element6 = (-element1) / element2

    assert element3.value == 10 
    assert element4.value == 4
    assert element5.value == 5
    assert element6.value == 2
    assert element3.modulus == modulus
    assert element4.modulus == modulus
    assert element5.modulus == modulus
    assert element6.modulus == modulus


def test_inverse_element():
    modulus = 2**4
    generator = GaloisFieldGenerator(modulus)
    element1 = generator.generate(9)
    element2 = element1.inverse()
    
    assert element1*element2 == GaloisFieldElement(modulus, 1)
