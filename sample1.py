def eq(a, b):
    return a == b

def gte(a, b):
    return a >= b


class Constraint (object):
    def __init__(self, constants, constraint_type, value):
        self.constants = constants
        self.constraint_type = constraint_type
        self.value = value


class Objective (object):
    def __init__(self, constants):
        self.constants = constants


def solve(constraints,objective):



    pass


c1 = Constraint([4, 3], eq, 20)  # we are passing in the eq function as data (just like 20 or [4, 3])
c2 = Constraint([1, -2], eq, 0)
c3 = Constraint([1, 0], gte, 0)

constraints = [c1, c2, c3]
objective = Objective([2, 3])

solve(constraints, objective)
# (2, 3)

