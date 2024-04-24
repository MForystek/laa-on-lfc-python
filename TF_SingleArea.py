import control
import matplotlib.pyplot as plt

s = control.tf('s')

# generator
D = 0.8
M = 10
generator = 1 / (D + M*s)

# load
load = 0.2 # MW

# turbine
Tt = 0.5
turbine = 1 / (1 + Tt*s)

# governor
Tg = 0.2
governor = 1 / (1 + Tg*s)

# droop
R = 0.05
droop = 1 / R

# AGC
beta = 50 # 20.6
K = 30 # 0.3
D = 10
N = 100
AGC = beta + (K / s) + (D*N / (1 + N/s))

gov_turb = control.series(governor, turbine)
droop_AGC = -control.parallel(droop, AGC)

sys = control.series(droop_AGC, gov_turb)
sys_load = control.parallel(sys, load)
single_area = control.feedback(generator, -sys)

t, y = control.step_response(single_area)
plt.plot(t, y+60)
plt.title("single_area step response")
plt.grid()
# plt.show()
print(single_area)