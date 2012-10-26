#!/usr/bin/env python

import newton
import functions
import unittest
import numpy as N
import random
from numpy import *

class TestNewton(unittest.TestCase):
    def testLinear(self):
        f = lambda x : 3.0 * x + 6.0
        solver = newton.Newton(f, tol=1.e-15, maxiter=3)
        x = solver.solve(2.0)
        self.assertEqual(x, -2.0)

    def testStep(self):
        p = functions.Polynomial([1, 2, 3])
        def f(x):
            return p(x)
        solver = newton.Newton(f, tol=1.e-15, maxiter=2)
        x0 = 1.0
        x = solver.step(x0)
        N.testing.assert_array_almost_equal(x, -0.5)     

    def testRoot1(self):
        p = functions.Polynomial([1, 3, 2])
        def f(x):
            return p(x)
        maxiter = 20
        solver = newton.Newton(f, tol=1.e-15, maxiter=20)
        x0 = -1.5
        self.assertRaises(RuntimeError, solver.solve, x0)

    def testRoot2(self):
        n = 5
        A = N.matrix(N.zeros((n,n)))
        for i in range(n):
            A[i,:] = random.random(n)
        b = N.matrix(N.zeros(n))
        b = random.random((n,1))
        def f(x):
            return A * x - b
        solver = newton.Newton(f, tol=1.e-15, maxiter=20)
        x0 = N.matrix(N.zeros(n))
        x0 = random.random((n,1))
        x = solver.solve(x0)
        solution = A.I * b
        N.testing.assert_array_almost_equal(x, solution)


    def testRoot1Analy(self):
        p = functions.Polynomial([1, 3, 2])
        def f(x):
            return p(x)
        maxiter=20
        J = functions.AnalyticalJacobian([1, 3, 2])
        def Jacobian(x):
            return J(x)
        solver = newton.Newton(f, tol=1.e-15, maxiter=20, Df=Jacobian)
        x0 = 0 
        x = solver.solve(x0)[0]
        N.testing.assert_array_almost_equal(x, -1.0)

    def testRange(self):
        p = functions.Polynomial([1, 3, 2])
        def f(x):
            return p(x)
        solver = newton.Newton(f, tol=1e-15, maxiter=20, r=1.e-2)
        x0 = -50
        self.assertRaises(RuntimeError, solver.solve, x0)
if __name__ == "__main__":
    unittest.main()
