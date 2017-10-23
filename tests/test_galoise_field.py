import pytest
from KiSD_projekt1.src.galoise_field import *

def test_create_field_element():
    element1 = GaloisFieldElement(5, 4)
    element2 = GaloisFieldElement(5, 4)
    element3 = GaloisFieldElement(4, 4)
    element4 = GaloisFieldElement(5, 3)
    element5 = 4

    assert element1 == element2
    assert element1 != element3
    assert element1 != element4
    assert element1 != element5

#def test_elements_generator():
    
