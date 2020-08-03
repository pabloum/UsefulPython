class Vector:
    def __init__(self, lst):
        self.vec  = lst
        self.size = len(lst)

    # Scalar product
    # _TODO

    # Dot Product
    def __mul__(self, param):
        if self.size == param.size:
            result = 0
            for i in range(self.size):
                result += self.vec[i]*param.vec[i]
        else:
            result = None
        return result

    # Cross product
    # _TODO

    def __rmul__(self, vec):
        return self * vec
