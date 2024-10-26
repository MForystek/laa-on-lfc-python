import numpy as np
import matplotlib.pyplot as plt

from utils import freq_per_unit_to_Hz
from matrices import MatrixA, MatrixB1, MatrixB2, MatrixC
from controller import PIDController
from area import Area


class StateInputOutputVectors:
    def __init__(self, n, m, T, time_step_sec, initial_loads_pu, attack_scenario):
        self._n = n
        self._m = m
        self._T = T
        self._time_step_sec = time_step_sec
        self._initial_loads_pu = initial_loads_pu
        self._attack_scenario = attack_scenario
        self._set_vectors()


    def get_x(self):
        return self._x
    
    
    def get_w(self):
        return self._w
    
    
    def get_u(self):
        return self._u
    
    
    def get_y(self):
        return self._y
    

    def _set_vectors(self):
        # State, input, output vectors
        self._define_state_input_output_vectors()

        # Initial conditions
        x0 = [np.zeros(shape=(2+2*self._m[i])) for i in range(self._n)] # n x 2+2*m
        for i in range(self._n):
            self._x[i][0, :] = x0[i]

        # Adding load changes    
        self._add_load_change(i)


    def _define_state_input_output_vectors(self):
        self._x = [np.zeros(shape=(len(self._T), 2+2*self._m[i])) for i in range(self._n)] # state vector
        self._w = np.zeros(shape=(len(self._T), self._n, 2)) # load change and tie-lines change
        self._u = np.zeros(shape=(len(self._T), self._n, 1)) # LFC controller output
        self._y = np.zeros(shape=(len(self._T), self._n, 1)) # Area Control Error (ACE)


    def _add_load_change(self, i):            
        altered_load = self._initial_loads_pu.copy()
        for i in range(self._n):
            for j in range(len(self._attack_scenario[i])):
                start_index = int(self._attack_scenario[i][j]["start"] / self._time_step_sec)
                end_index = int(self._attack_scenario[i][j]["end"] / self._time_step_sec)
                altered_load[i][start_index:end_index] = self._attack_scenario[i][j]["strength"]
        self._w[:, :, 0] = altered_load.T


class Simulation:
    def __init__(self, f0, base_MV, n, m, D, H, Tt, Tg, R, alpha, beta, Tij, K, setpoint, time_step_sec, T, indices, x, w, u, y):
        self._f0 = f0
        self._base_MV = base_MV
        self._n = n
        self._m = m
        self._D = D
        self._H = H
        self._Tt = Tt
        self._Tg = Tg
        self._R = R
        self._alpha = alpha
        self._beta = beta
        self._Tij = Tij
        self._K = K
        self._setpoint = setpoint
        self._time_step_sec = time_step_sec
        self._T = T
        self._indices = indices
        self._x = x
        self._w = w
        self._u = u
        self._y = y
        
    
    def run_and_plot_results(self, print_continuous_matrices,
                                   print_discrete_matrices,
                                   plot_only_frequency):        
        # Getting areas
        self._Areas: list[Area] = []
        for i in range(self._n):
            matrixA = MatrixA(self._m[i], self._D[i], self._H[i], self._Tt[i], self._Tg[i], self._R[i], self._Tij[i]).get_A()
            matrixB1 = MatrixB1(self._m[i], self._H[i]).get_B1()
            matrixB2 = MatrixB2(self._m[i], self._Tg[i], self._alpha[i]).get_B2()
            matrixC = MatrixC(self._m[i], self._beta[i]).get_C()
            controller = PIDController(self._K[i], self._setpoint, self._time_step_sec)
            
            self._Areas.append(Area(i+1, self._m[i], matrixA, matrixB1, matrixB2, matrixC, controller, self._time_step_sec))
            if (print_continuous_matrices):
                self._Areas[i].print_continuous_matrices()
            if (print_discrete_matrices):
                self._Areas[i].print_discrete_matrices()
                
        # Running simulation, plotting and printing results
        self._simulate_LFC_power_system() 
        self._plot_LFC_power_system_results(plot_only_frequency)
        self._print_final_frequencies()


    def _simulate_LFC_power_system(self):    
        for t in self._indices[1:]:
            for i in range(self._n):
                self._w[t-1, i, 1] = np.sum([self._Tij[i][j]*self._x[j][t-1, 0] for j in range(self._n)]) # v_i calculation
                # w[t-1, i, 1] = np.sum(Tij[i]*np.concatenate([x[t-1, :, 0], real_inputs[t-1, :]])
                # Additional entries in Tij for inputs from real areas
                self._x[i][t] = self._Areas[i].Ad @ self._x[i][t-1] + self._Areas[i].B1d @ self._w[t-1, i] + self._Areas[i].B2d @ self._u[t-1, i]
                self._y[t-1, i] = self._Areas[i].Cd @ self._x[i][t-1]
                self._u[t, i] = self._Areas[i].controller.update(self._y[t-1, i], self._u[t-1, i]) # Delta P_Ci calculation 


    def _plot_LFC_power_system_results(self, only_freq=False):
        legend = []
        types = ['solid', 'dashed', 'dashdot', 'dotted']
        plt.figure()
        for i in range(self._n):
            legend.append(f"Area{i+1}")
            if (only_freq):
                plt.subplot(2, 1, 1)
            else:
                plt.subplot(4, 1, 1)
            plt.title("Response for Areas")
            plt.plot(self._T, freq_per_unit_to_Hz(self._x[i][:, 0], self._f0), linestyle=types[i])
            plt.xlim(self._T[0], self._T[-1])
            plt.ylabel("Freq [Hz]")
            
            if (only_freq):
                plt.subplot(2, 1, 2)
                plt.plot(self._T[1:], np.diff(freq_per_unit_to_Hz(self._x[i][:, 0], self._f0))/self._time_step_sec, linestyle=types[i])
                plt.xlim(self._T[0], self._T[-1])
                plt.ylabel("RoCoF [Hz/s]")
            
            if (not only_freq):
                plt.subplot(4, 1, 2)
                plt.plot(self._T, self._w[:, i, 1], linestyle=types[i])
                plt.xlim(self._T[0], self._T[-1])
                plt.ylabel("Tie-lines")
                
                plt.subplot(4, 1, 3)
                plt.plot(self._T, self._y[:, i], linestyle=types[i])
                plt.xlim(self._T[0], self._T[-1])
                plt.ylabel("ACE")
                
                plt.subplot(4, 1, 4)
                plt.plot(self._T, self._u[:, i], linestyle=types[i])
                plt.xlim(self._T[0], self._T[-1])
                plt.ylabel("LFC output")
        if (only_freq):
            plt.subplot(2, 1, 1)
        else:
            plt.subplot(4, 1, 1)
        # Nominal frequency
        plt.axhline(y=self._f0, color='r', linestyle=types[0], linewidth=0.5)
        # Safe operating frequency ranges
        plt.axhline(y=58.8, color='b', linestyle=types[1], linewidth=0.5)
        plt.axhline(y=60.5, color='b', linestyle=types[1], linewidth=0.5)
        plt.axhline(y=57.5, color='g', linestyle=types[2], linewidth=0.5)
        plt.axhline(y=61.5, color='g', linestyle=types[2], linewidth=0.5)
        plt.axhline(y=57.0, color='r', linestyle=types[3], linewidth=0.5)
        plt.axhline(y=62.5, color='r', linestyle=types[3], linewidth=0.5)
        plt.legend(legend, loc="upper right")
        if (not only_freq):
            plt.tight_layout()
        plt.show()


    def _print_final_frequencies(self):
        print("Final frequencies for each area:")
        for i in range(self._n):
            print(f"Area {i+1}: {round(freq_per_unit_to_Hz(self._x[i][-1, 0], self._f0), 4)} Hz")