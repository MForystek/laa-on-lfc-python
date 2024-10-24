import numpy as np


class GenParams:
    def __init__(self, f0, base_MV, n, m, D, H, Tt_general, Tg_general, R_general, alpha, Tij) -> None:
        self.f0 = f0
        self.base_MV = base_MV
        self.n = n
        self.m = m
        self.D = D
        self.H = H
        self.alpha = alpha
        self.Tij = Tij
        self._reshape_Tt_Tg_and_R_to_match_num_of_generators_in_areas(Tt_general, Tg_general, R_general)    
        self._set_beta()
        

    def _reshape_Tt_Tg_and_R_to_match_num_of_generators_in_areas(self, Tt_general, Tg_general, R_general):
        self.Tt = []
        self.Tg = []
        self.R = []
        index = 0
        for i in self.m:
            self.Tt.append(np.array(Tt_general[index:index+i]))
            self.Tg.append(np.array(Tg_general[index:index+i]))
            self.R.append(np.array(R_general[index:index+i]))
            index += i
            
    
    def _set_beta(self):
        R_sys_recipr = np.zeros(self.n)
        for i in range(self.n):
            R_sys_recipr[i] = np.sum(self.R[i])
            
        self.beta = np.zeros(self.n)
        for i in range(self.n):
            self.beta[i] = self.D[i] + 1/R_sys_recipr[i]
