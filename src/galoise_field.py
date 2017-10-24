def ext_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    if b == 0:
        return (a, 1, 0)
    q, r = divmod(b, a)
    d, xp, yp = ext_gcd(r, a)
    return (d, yp-q*xp, xp)


def invmod(a, n):
    d, x, y = ext_gcd(a, n)
    if abs(d) != 1:
        raise ValueError("modulo must be coprime with the element")
    return x * d


class GaloisFieldElement(object):
    def is_operation_valid(self, other):
        if isinstance(other, GaloisFieldElement) and self.modulus == other.modulus:
            return True
        else:
            raise ValueError("Elements are from different fields")
    
    def __init__(self, modulus, value):
        self.modulus = modulus
        self.value = value%self.modulus

    def __eq__(self, other):
        return isinstance(other, GaloisFieldElement) and (self.value == other.value) and (self.modulus == other.modulus) 

    def __add__(self, other):
        if self.is_operation_valid(other):
            return GaloisFieldElement(self.modulus, self.value + other.value)

    def __sub__(self, other):
        if self.is_operation_valid(other):
            return GaloisFieldElement(self.modulus, self.value - other.value)

    def __mul__(self, other):
        if self.is_operation_valid(other):
            return GaloisFieldElement(self.modulus, self.value * other.value)

    def __div__(self, other):
        if self.is_operation_valid(other):
            return GaloisFieldElement(self.modulus, self.value / other.value)

    def __pow__(self, other):
        if self.is_operation_valid(other):
            return GaloisFieldElement(self.modulus, self.value ** other.value)

    def __neg__(self):
        return GaloisFieldElement(self.modulus, -self.value)

    def __repr__(self):
        return "%d" % self.value

    def inverse(self):
        return GaloisFieldElement(self.modulus, invmod(self.value, self.modulus))


class GaloisFieldGenerator(object):
    
    def __init__(self, modulus):
        self.modulus = modulus

    def generate(self, value):
        return GaloisFieldElement(self.modulus, value)
