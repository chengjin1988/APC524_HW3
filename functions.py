import numpy as N

def ApproximateJacobian(f, x, dx=1e-6):
    """Return an approximation of the Jacobian Df(x) as a numpy matrix"""
    try:
	n = len(x)
    except TypeError:
        n = 1
    fx = f(x)
    Df_x = N.matrix(N.zeros((n,n)))
    for i in range(n):
        v = N.matrix(N.zeros((n,1)))
        v[i,0] = dx
        Df_x[:,i] = (f(x + v) - fx)
    return Df_x/dx

class Polynomial(object):
    """Callable polynomial object.

    Example usage: to construct the polynomial p(x) = x^2 + 2x + 3,
    and evaluate p(5):

    p = Polynomial([1, 2, 3])
    p(5)"""

    def __init__(self, coeffs):
        self._coeffs = coeffs

    def __repr__(self):
        return "Polynomial(%s)" % (", ".join([str(x) for x in self._coeffs]))

    def f(self,x):
        ans = self._coeffs[0]
        for c in self._coeffs[1:]:
            ans = x*ans + c
        return ans

    def __call__(self, x):
        return self.f(x)

class AnalyticalJacobian(object):
    """Callable analytical Jacobian object (only for polynomial).

    Example usage: to construct the Jacobian for polynomial p(x) = x^2 + 2x + 3,
    and evaluate p(5):

    p = Analytical([1, 2, 3]) ( = 2x + 2)
    p(5)"""

    def __init__(self, coeffs):
        self._coeffs = coeffs

    def __repr__(self):
        return "Polynomial(%s)" % (", ".join([str(x) for x in self._coeffs]))

    def f(self,x):
        print "AnalyticalJacobian is used...."        
        try:
            n = len(self._coeffs)
        except TypeError:
            ans = 0
        ans = N.matrix(N.zeros((1,1)))
        for i in range(n-1):
            ans = x*ans + (n-i-1)*self._coeffs[i]
        return ans

    def __call__(self, x):
        return self.f(x)

def function2D(x):
    f = N.matrix(N.zeros((2,1))) 
    f[0] = N.sin(x[0]) + N.cos(x[1])
    f[1] = N.exp(x[0]) + N.exp(-x[1])
    return f

def function2DJacobian(x):
    A = N.matrix(N.zeros((2,2)))
    A[0,0] = N.cos(x[0])
    A[0,1] = -N.sin(x[1])
    A[1,0] = N.exp(x[0])
    A[1,1] = -N.exp(-x[1])
    return A
