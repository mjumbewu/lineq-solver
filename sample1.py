#!/usr/bin/env python3
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
    ...

def scale_row(matrix, r, factor):
    ...

def add_rows(matrix, addend_row, sum_row, factor=1):
    ...


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

    def get_intersection(self, other):
        """
        Find the intersection point of n n-dimensional surfaces.
        """
        # TODO: Fill the rest of this out. Look up an intersection of lines
        # algorithm. Gaussian elimination will do.
        ...

    def is_satisfied_by(self, point):
        """
        Determine wether the given point satifies the condition of this
        constraint.
        """
        ...


class Objective (object):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def calculate(self, point):
        """
        Get the value of the optimization function at the given point.
        """
        ...


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
        ...

    # 2. Discard any intersections outside of the feasible set
    feasible_intersections = []
    for intersection in intersections:
        ...

    # 3. Find the intersection that maximizes the objective
    ...

    return optimal_intersection


c1 = Constraint([4, 3], gte, 20)  # we are passing in the eq function as data (just like 20 or [4, 3])
c2 = Constraint([1, -2], gte, 0)
c3 = Constraint([1, 0], gte, 0)

constraints = [c1, c2, c3]
objective = Objective([2, 3])

solve(constraints, objective)
