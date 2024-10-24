import numpy as np


class MatrixA:    
    def __init__(self, m, D, H, Tt, Tg, R, Tj) -> None:
        self._assign_params(m, D, H, Tt, Tg, R, Tj)
        self._define_sumbatrices_A()
        self._assign_submatrices_A()
        self._combine_submatrices_A_into_A()
    
    
    def _assign_params(self, m, D, H, Tt, Tg, R, Tj) -> None:
        self._m = m
        self._D = D
        self._H = H
        self._Tt = Tt
        self._Tg = Tg
        self._R = R
        self._Tj = Tj
    
        
    def _define_sumbatrices_A(self) -> None:        
        self._A11 = np.zeros([2, 2])
        self._A12 = np.zeros([2, self._m])
        self._A13 = np.zeros([2, self._m])
        self._A21 = np.zeros([self._m, 2])
        self._A22 = np.zeros([self._m, self._m])
        self._A23 = np.zeros([self._m, self._m])
        self._A31 = np.zeros([self._m, 2])
        self._A32 = np.zeros([self._m, self._m])
        self._A33 = np.zeros([self._m, self._m])
        self._A = np.zeros([2+2*self._m, 2+2*self._m])
        
        
    def _assign_submatrices_A(self) -> None:
        sumTj = np.sum(self._Tj) # -Tj - don't need to do this because Tii is always 0
        Hi_inv = 1/(2*self._H)

        for j in range(self._m):
            self._A22[j, j] = -1/self._Tt[j]                  # m x m diag
            self._A31[j] = [-1/(self._Tg[j] * self._R[j]), 0] # m x 2
            self._A33[j, j] = -1/self._Tg[j]                  # m x m diag

        self._A11[:, :] = [[-self._D*Hi_inv, -Hi_inv], # 2 x 2
                           [2*np.pi*sumTj, 0]]
        self._A12[:, :] = [[Hi_inv]*self._m,           # 2 x m
                           [0]*self._m]
        self._A13[:, :] = [[0]*self._m,                # 2 x m
                           [0]*self._m]
        self._A21 = np.transpose(self._A13)            # m x 2
        self._A23 = -self._A22.copy()
        self._A32 = np.full([self._m, self._m], 0)     # m x m


    def _combine_submatrices_A_into_A(self) -> None:
        rowsA = [0, 0, 0, 2, 2, 2, 2+self._m, 2+self._m, 2+self._m]
        colsA = [0, 2, 2+self._m, 0, 2, 2+self._m, 0, 2, 2+self._m]

        #A[i] = [[A11[i], A12[i], A13[i]],
        #        [A21[i], A22[i], A23[i]],
        #        [A31[i], A32[i], A33[i]]]
        self._A[rowsA[0]:rowsA[0]+self._A11.shape[0], colsA[0]:colsA[0]+self._A11.shape[1]] = self._A11
        self._A[rowsA[1]:rowsA[1]+self._A12.shape[0], colsA[1]:colsA[1]+self._A12.shape[1]] = self._A12
        self._A[rowsA[2]:rowsA[2]+self._A13.shape[0], colsA[2]:colsA[2]+self._A13.shape[1]] = self._A13
        self._A[rowsA[3]:rowsA[3]+self._A21.shape[0], colsA[3]:colsA[3]+self._A21.shape[1]] = self._A21
        self._A[rowsA[4]:rowsA[4]+self._A22.shape[0], colsA[4]:colsA[4]+self._A22.shape[1]] = self._A22
        self._A[rowsA[5]:rowsA[5]+self._A23.shape[0], colsA[5]:colsA[5]+self._A23.shape[1]] = self._A23
        self._A[rowsA[6]:rowsA[6]+self._A31.shape[0], colsA[6]:colsA[6]+self._A31.shape[1]] = self._A31
        self._A[rowsA[7]:rowsA[7]+self._A32.shape[0], colsA[7]:colsA[7]+self._A32.shape[1]] = self._A32
        self._A[rowsA[8]:rowsA[8]+self._A33.shape[0], colsA[8]:colsA[8]+self._A33.shape[1]] = self._A33
        
    
    def get_A(self) -> np.ndarray:
        return self._A
    
    
class MatrixB1:
    def __init__(self, m, H) -> None:
        self._assign_params(m, H)
        self._define_sumbatrices_B1()
        self._assign_submatrices_B1()
        self._combine_submatrices_B1_into_B1()
        
        
    def _assign_params(self, m, H) -> None:
        self._m = m
        self._H = H
        
    
    def _define_sumbatrices_B1(self) -> None: 
        self._B11 = np.zeros([2, 2])
        self._B12 = np.zeros([self._m, 2])
        self._B13 = np.zeros([self._m, 2])
        self._B1 = np.zeros([2+2*self._m, 2])
        
    def _assign_submatrices_B1(self) -> None:
        Hi_inv = 1/(2*self._H)
            
        self._B11[:, :] = [[-Hi_inv, 0], # 2 x 2
                          [0, -2*np.pi]]
        self._B12[:, :] = [[0, 0]]*self._m  # m x 2
        self._B13 = self._B12.copy()         # m x 2
        
        
    def _combine_submatrices_B1_into_B1(self) -> None:
        rowsB1 = [0, 2, 2+self._m]; colsB1 = 0
        
        #B1[i] = [B11[i],
        #         B12[i],
        #         B13[i]]
        self._B1[rowsB1[0]:rowsB1[0]+self._B11.shape[0], colsB1:colsB1+self._B11.shape[1]] = self._B11
        self._B1[rowsB1[1]:rowsB1[1]+self._B12.shape[0], colsB1:colsB1+self._B12.shape[1]] = self._B12
        self._B1[rowsB1[2]:rowsB1[2]+self._B13.shape[0], colsB1:colsB1+self._B13.shape[1]] = self._B13
        
    
    def get_B1(self) -> np.ndarray:
        return self._B1
    
    
class MatrixB2:
    def __init__(self, m, Tg, alpha) -> None:
        self._assign_params(m, Tg, alpha)
        self._define_sumbatrices_B2()
        self._assign_submatrices_B2()
        self._combine_submatrices_B2_into_B2()
     
     
    def _assign_params(self, m, Tg, alpha) -> None:
        self._m = m
        self._Tg = Tg
        self._alpha = alpha
           
        
    def _define_sumbatrices_B2(self) -> None:
        self._B21 = np.zeros([2, 1])
        self._B22 = np.zeros([self._m, 1])
        self._B23 = np.zeros([self._m, 1])
        self._B2 = np.zeros([2+2*self._m, 1])
        
        
    def _assign_submatrices_B2(self) -> None:
        self._B21[:, :] = [[0],         # 2 x 1         
                          [0]]
        self._B22[:, :] = [[0]]*self._m # m x 1
        for j in range(self._m):
            self._B23[j] = [self._alpha[j] / self._Tg[j]] # m x 1
                
        
    def _combine_submatrices_B2_into_B2(self) -> None:
        rowsB2 = [0, 2, 2+self._m]; colsB2 = 0
        
        #B2[i] = [B21[i],
        #         B22[i],
        #         B23[i]]
        self._B2[rowsB2[0]:rowsB2[0]+self._B21.shape[0], colsB2:colsB2+self._B21.shape[1]] = self._B21
        self._B2[rowsB2[1]:rowsB2[1]+self._B22.shape[0], colsB2:colsB2+self._B22.shape[1]] = self._B22
        self._B2[rowsB2[2]:rowsB2[2]+self._B23.shape[0], colsB2:colsB2+self._B23.shape[1]] = self._B23
        
    
    def get_B2(self) -> np.ndarray:
        return self._B2
    
    
class MatrixC:
    def __init__(self, m, beta) -> None:
        self._assign_params(m, beta)
        self._define_matrix_C()
        self._assign_matrix_C()
        
        
    def _assign_params(self, m, beta) -> None:
        self._m = m
        self._beta = beta
        
        
    def _define_matrix_C(self) -> None:
        self._C = np.zeros([2+2*self._m]) # n x 2+2*m


    def _assign_matrix_C(self) -> None:
        self._C = np.concatenate([[self._beta, 1], [0]*self._m, [0]*self._m]) # 1 x 2+2*m
        

    def get_C(self) -> np.ndarray:
        return self._C