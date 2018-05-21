from scipy import *
from scipy.optimize import curve_fit

## Input data (generated by simulation with random noise).}
L  = array([0.10, 0.16, 0.22, 0.28, 0.34, 0.40, 0.46, 0.52, 0.58, 0.64])
dL = array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
T  = array([0.71, 0.76, 0.91, 1.00, 1.20, 1.14, 1.44, 1.40, 1.53, 1.58])
dT = array([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])

Tsq = T**2           # Estimates for T^2}
Tsq_error = 2*T*dT   # Errors for T^2, from error propagation rules}

## Define a function, named f, that returns an order-1 polynomial.}
def f(x, b0, b1): return b0 + b1*x

## Use f to fit the L vs Tsq data}
est, covar = curve_fit(f, L, Tsq, sigma=Tsq_error)

## Estimators and their errors:}
b0, b1 = est              # Estimate of intercept and slope
db0 = sqrt(covar[0,0])     # Standard error of intercept}
db1 = sqrt(covar[1,1])     # Standard error of slope}

g  = 4*pi*pi/b1            # Estimate for g (computed from b1)}
dg = (g/b1)*db1            # Estimate for standard error of g}

## Plot the data points, with error bars}
import matplotlib.pyplot as plt
plt.errorbar(L, Tsq, xerr=dL, yerr=Tsq_error, fmt='o')
plt.xlabel('Pendulum length L (m)', fontsize=12)
plt.ylabel('Squared period T^2 (s^2)', fontsize=12)
## Include the fitted curve in the plot}
L2 = linspace(0, 0.7, 100)
plt.plot(L2, b0 + b1*L2)
## State fitted value of g in the figure title}
plt.title("g = {:.1f} +/- {:.1f} m/s^2".format(g, dg), fontsize=12)
plt.show()
