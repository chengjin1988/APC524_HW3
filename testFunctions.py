#!/usr/bin/env python

import functions as F
import numpy as N
import unittest
import random
from numpy import *

class TestFunctions(unittest.TestCase):
    def testApproxJacobian1(self):
        slope = 3.0
        def f(x):
            return slope * x + 5.0
        x0 = 2.0
        dx = 1.e-3
        Df_x = F.ApproximateJacobian(f, x0, dx)
        self.assertEqual(Df_x.shape, (1,1))
        self.assertAlmostEqual(Df_x, slope)

    def testApproxJacobian2(self):
        A = N.matrix("1. 2.; 3. 4.")
        def f(x):
            return A * x
        x0 = N.matrix("5; 6")
        dx = 1.e-6
        Df_x = F.ApproximateJacobian(f, x0, dx)
        self.assertEqual(Df_x.shape, (2,2))
        N.testing.assert_array_almost_equal(Df_x, A)

    def testPolynomial(self):
        # p(x) = x^2 + 2x + 3
        p = F.Polynomial([1, 2, 3])
        for x in N.linspace(-2,2,11):
            self.assertEqual(p(x), x**2 + 2*x + 3)
  
    def testHighDimension1(self):
        n = 5
        A = N.matrix(N.zeros((n,n)))
        for i in range(n):
            A[i,:] = random.random(n)
        def f(x):
            return A * x
        x0 = N.matrix(N.zeros(n))
        x0 = random.random((n,1))
        dx = 1.e-6
        Df_x = F.ApproximateJacobian(f, x0, dx)
        self.assertEqual(Df_x.shape, (n,n))
        N.testing.assert_array_almost_equal(Df_x, A)
 
    def testHighDimension2(self):
        n = 5
        A = N.matrix(N.zeros((n,n)))
        for i in range(n):
            A[i,:] = random.random(n)
        def f(x):
            return N.square( A * x )
        x0 = N.matrix(N.zeros(n))
        x0 = random.random((n,1))
        dx = 1.e-6
        Df_x = F.ApproximateJacobian(f, x0, dx)
        self.assertEqual(Df_x.shape, (n,n))
        exact = N.matrix(N.zeros((n,n)))
        for i in range(n):
            for j in range(n):
                exact[i,j] = 2*A[i,j]*((A*x0)[i])
        N.testing.assert_array_almost_equal(Df_x, exact)
if __name__ == '__main__':
    unittest.main()



