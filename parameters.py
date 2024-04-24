import numpy as np

# General parameters
f0 = 60 # Hz
n = 3 # number of Areas
m = 3 # number of Governor-Turbines in each Area

# Genertors numbers
# 30, 31, 32, 33, 34, 35, 36, 27, 28, 39

# Generator parameters
D = np.array([1, 1, 1])
H = np.array([45.27, 28.95, 26.3])*2/f0

# Turbine and governor parameters 
Tt = np.array([0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04])
Tg = np.array([0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08])

# Droop characteristic
R = np.array([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
R_sys_recipr = np.zeros(n)
for i in range(n):
    R_sys_recipr[i] = np.sum(R[i*m:i*m+m])

# Automatic Generation Control (AGC) parameters
# Alfa only if many Governor-Turibne in one Area, must sum to 1 in one Area
alpha = np.array([])
beta = np.zeros(n)
for i in range(n):
    beta[i] = D[i] + 1/R_sys_recipr[i]

# Tie-lines, matrix
Tij = np.array([[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]])