
class GaloisFieldElement(object):
    """implementation"""
    
    def __init__(self, modulus, value):
        self.modulus = modulus
        self.value = value%self.modulus

    def __eq__(self, other):
        return isinstance(other, GaloisFieldElement) and (self.value == other.value) and (self.modulus == other.modulus) 

    def __add__(self, other):
        if isinstance(other, GaloisFieldElement) and self.modulus == other.modulus:
            return GaloisFieldElement(self.modulus, self.value + other.value)

    def __sub__(self, other):
        if isinstance(other, GaloisFieldElement) and self.modulus == other.modulus:
            return GaloisFieldElement(self.modulus, self.value - other.value)


class GaloisFieldGenerator(object):
    
    def __init__(self, modulus):
        self.modulus = modulus

    def generate(self, value):
        return GaloisFieldElement(self.modulus, value)
