
class GaloisFieldElement(object):
    """implementation"""
    
    def __init__(self, value, modulus):
        self.modulus = modulus
        self.value = value%self.modulus

    def __eq__(self, other):
        return isinstance(other, GaloisFieldElement) and (self.value == other.value) and (self.modulus == other.modulus) 
