
class GaloisFieldElement(object):
    """implementation"""
    
    def __init__(self, modulus, value):
        self.modulus = modulus
        self.value = value%self.modulus

    def __eq__(self, other):
        return isinstance(other, GaloisFieldElement) and (self.value == other.value) and (self.modulus == other.modulus) 


class GaloisFieldGenerator(object):
    
    def __init__(self, modulus):
        self.modulus = modulus

    def generate(self, value):
        return GaloisFieldElement(self.modulus, value)
