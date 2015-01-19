#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

from itertools import combinations


# Inequality constraints
def eq(a, b):
    return a == b

def gte(a, b):
    return a >= b

def lte(a, b):
    return a <= b


# Elementary matrix row operations
def swap_rows(matrix, r1, r2):
    matrix[r1], matrix[r2] = matrix[r2], matrix[r1]

def scale_row(matrix, r, factor):
    map(matrix[r], lambda e: e * factor)

def add_rows(matrix, addend_row, sum_row, factor=1):
    row_a = matrix[addend_row]
    row_s = matrix[sum_row]

    l = len(row_s)
    for i in range(l):
        row_s[i] += row_a[i] * factor


class Constraint (object):
    """
    A class that represents a linear constraint. Genrally, a contraint can be
    represented as:

        c₀x₀ + c₁x₁ + c₂x₂ + ... >= v

    or:

        c₀x₀ + c₁x₁ + c₂x₂ + ... <= v

    These constraints can be constructed respectively as the following objects:

        Constraint([c₀, c₁, c₂, ...], gte, v)
        Constraint([c₀, c₁, c₂, ...], lte, v)

    """

    def __init__(self, coefficients, constraint_type, value):
        self.coefficients = coefficients
        self.constraint_type = constraint_type
        self.value = value

    def is_parallel(self, other):
        """
        Return True if the surface representing the boundary for this
        inequality is parallel to (never intersects with) the `other` surface.
        Return False if they do intersect.

        NOTE:
        Since this solution only works in two-dimensional spaces, this function
        need only determine whether two lines are parallel.

        """
        coeff1 = self.coefficients
        coeff2 = other.coefficients
        return coeff1[0] / coeff2[0] == coeff1[1] / coeff2[1] and \
               coeff1[1] / coeff2[1] == self.value / other.value

    def get_intersection(self, other):
        """
        Find the intersection point of n n-dimensional surfaces.

        NOTE:
        Since this solution only works in two-dimensional spaces, this function
        need only find the intersection of two lines.

        """
        if self.is_parallel(other):
            return None

        i = 0
        if self.coefficients[i] == 0: pass

        # TODO: Fill the rest of this out. Look up an intersection of lines
        # algorithm. Gaussian elimination will do.

    def is_satisfied_by(self, point):
        """
        Determine wether the given point satifies the condition of this
        constraint.

        """
        result = 0
        for (c, x) in zip(self.coefficients, point):
            result += c*x

        test_func = self.constraint_type
        return test_func(result, self.value)


class Objective (object):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def calculate(self, point):
        result = 0
        for(c, x) in zip(self.coefficients, point):
            result += c*x
        return result


def solve(constraints, objective, opt=max):
    """
    Optimize a set of constraints against an objective function.

    Arguments
    ---------
    * constraints: A list or set of constraint objects.

    * objective:   An objective function object.

    * opt:         An optimization function. This will either be max, min, or
                   some other function that has a similar signature.

    """
    intersections = []

    # 1. Find the pairwise intersections
    for c1, c2 in combinations(constraints, 2):
        intersection = c1.get_intersection(c2)
        if intersection:
            intersections.append(intersection)

    # 2. Discard any intersections outside of the feasible set
    feasible_intersections = []
    for intersection in intersections:
        is_feasible = True
        for constraint in constraints:
            if not constraint.is_satisfied_by(intersection):
                is_feasible = False
                break
        if is_feasible:
            feasible_intersections.append(intersection)

    # 3. Find the intersection that maximizes the objective
    optimal_intersection = opt(feasible_intersections, key=objective.calculate)

    return optimal_intersection


c1 = Constraint([4, 3], gte, 20)  # we are passing in the eq function as data (just like 20 or [4, 3])
c2 = Constraint([1, -2], gte, 0)
c3 = Constraint([1, 0], gte, 0)

constraints = [c1, c2, c3]
objective = Objective([2, 3])

solve(constraints, objective)
# (2, 3)

