import numpy as np
from numpy import argmax

filename = "500/kpf_1.txt"
problem_instance = Instance(filename)

def greedyforfeits(X, W, P, b, F, D):
    S = np.array([])
    bres = b
    ratio = np.array([])
    #forfeits=0
    while np.array_equal(S, X) == False:        
        Xiter = []
        
        print(S)  # print solution
        print(f"bres {bres}")
        for i in X:
            if W[i] <= bres and i not in S:
                Xiter = np.append(Xiter, i)
                
                
        #print(f"Xiter {Xiter}")
        if (len(Xiter)) == 0:
            return S

         H=np.array([])
        for i in Xiter:
            i = int(i)
            p_i = P[i]
            # print(p_i)
            h_i = p_i / W[i]
            H = np.append(H, h_i)

        i_max = argmax(H)

          
        if H[i_max] < 0:
            return S
        
        
        S = np.append(S, Xiter[i_max])

        bres = bres - W[i_max]

    return S


solution = greedyforfeits(
    problem_instance.items,
    problem_instance.weights,
    problem_instance.profits,
    problem_instance.budget,
    problem_instance.forfeits_pairs,
    problem_instance.forfeits_costs,
)

print(solution)