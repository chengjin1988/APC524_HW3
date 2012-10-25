APC524_HW3
==========
* funcitons.py
	// ApproximateJacobian:	numerical Jacobian matrix calculator
        // Polynomial:		polynomial constructor
        // AnalyticalJacobian (for single variable polynomial)
				analytical Jacobian matrix constructor for polynomial
	// function2D:		construct a 2D function (2 variables used)
 	// function2DJacobian:	construct the Jacobian matrix for the 2D function analytically 	

* newton.py
	// class Newton
	   member function:
		__init__:	f, tol, maxiter, dx, Df
		solve:		solver with Newtor method
		step:		one step forward with Newton method

* testFunctions.py
	// testApproxJacobian1: test accuracy of ApproximateJacobian 
        			in f = kx + b

        // testApproxJacobian2: test accuracy of ApproximateJacobian 
			        in f = A*x (A is a 2*2 matrix)

	// testPolynomial:	test whether Polynomial workd correctly

        // testHighDimension1:	test accuracy of ApproximateJacobian
			        in f = A*x (A is a n*n matrix, n can be altered)

	// testHighDimension2:	test accuracy of ApproximateJacobian
			        in f[i] = ((A*x)[i])**2 (A is a n*n matrix. n can be altered)

	// testAnalyticalJacobian (for single variable polynomial):
			        test accuracy of Analytical Jacobian in a Polynomial case 
			        compared to ApproximateJacobian result

	// test2D:		test accuracy of analytical Jacobian matrix (in 2D case)
				compared to ApprocimateJacobian result
* testNewton.py
	// testLinear:	test accuracy of Newtown solver in a linear case

	// testStep:	test whether step works correctly

	// testRoot1:	test accuracy of root finder in a polynomial case, 
			raise exception when it reaches maximun iteration number

	// testRoot2:	test accuracy of root finder in A*x-b case.

	// testRootAnaly:
			test accuracy of root with AnalyticalJacobian in the same
			case as in testRoot1

APC524_HW3
