import numpy as np
import scipy.signal


class Area:
    def __init__(self, area_num, m, matrixA, matrixB1, matrixB2, matrixC, controller, time_step_sec) -> None:
        self._area_num = area_num
        self._m = m
        self._A = matrixA
        self._B1 = matrixB1
        self._B2 = matrixB2
        self._C = matrixC
        self._time_step_sec = time_step_sec
        self.controller = controller
        self._set_discrete_matrices_from_const_matrices()
        
        
    def _set_discrete_matrices_from_const_matrices(self) -> None:
        B = np.concatenate([self._B1, self._B2], 1)
        
        Ad = np.zeros([2+2*self._m, 2+2*self._m])
        Bd = np.zeros([2+2*self._m, 3])
        Cd = np.zeros([2+2*self._m])
        #Dd = np.zeros([1]) # always 0
        #dt = np.zeros([1]) # the same as time_step

        Ad, Bd, Cd, _, _ = scipy.signal.cont2discrete(
                                (self._A, B, self._C, 0), self._time_step_sec, method='zoh')
        self.Ad = Ad
        self.B1d = Bd[:, 0:2]
        self.B2d = Bd[:, 2:]
        self.Cd = Cd
    
    def print_continuous_matrices(self) -> None:
        print("CONTINUOUS FORM MATRICES.\n")
        self._print_matrices(self._A, self._B1, self._B2, self._C)
        
        
    def print_discrete_matrices(self) -> None:
        print("DISCRETE FORM MATRICES.\n")
        self._print_matrices(self.Ad, self.B1d, self.B2d, self.Cd)
        
    
    def _print_matrices(self, A, B1, B2, C) -> None:
        with np.printoptions(precision=4, suppress=True):
            print(f"Matrix A, area {self._area_num}:\n{A}\n")
            print(f"Matrix B1, area {self._area_num}:\n{B1}\n")
            print(f"Matrix B2, area {self._area_num}:\n{B2}\n")
            print(f"Matrix C, area {self._area_num}:\n{C}\n")