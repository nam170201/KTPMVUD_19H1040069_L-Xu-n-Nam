import pytest
a = [2,5,7,8]
def nguyento(A):
    T = True
    F = False
    prime = True
    C = 0
    B = len(A)
    
    for i in range(B):
        if (A[i] == 2 ):
            C = C + 1
        elif (A[i] < 2):
            prime = False
        elif (A[i] % 2 == 0):
            prime = False
        else    :
            for n in range(2,A[i]):
                
                if (A[i] % n == 0 ):
                    prime = False
                else : 
                    C = C + 1
    if (C >= 2):
        return T
    if (C < 2 ):
        return F
                
                    
print(nguyento(a))