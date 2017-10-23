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
    
