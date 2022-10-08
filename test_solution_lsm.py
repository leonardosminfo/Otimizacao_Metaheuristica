import numpy as np
from numpy import argmax

from readinstance import Instance

# filename = sys.argv[1]

filename = "500/kpf_1.txt"
problem_instance = Instance(filename)

def greedyforfeits(X, W, P, b, F, D):
    S = np.array([])
    bres = b
    ratio = np.array([])
    while np.array_equal(S, X) == False:        
        Xiter = []
        
        print(S)  # print solution
        print(f"bres {bres}")
        for i in X:
            if W[i] <= bres and i not in S:
                Xiter = np.append(Xiter, i)
                
                

        if (len(Xiter)) == 0:
            return S


        ratio = np.array([])
        for i in Xiter:
            i = int(i)
            p_i = P[i]

            lD=D[np.intersect1d(np.where(problem_instance.forfeits_pairs[:,[1]]==s)[0],np.where(problem_instance.forfeits_pairs[:,[0]]==i)[0])]
            for minus in lD:
                p_i=p_i-minus

            ratio_i = p_i / W[i]

            ratio = np.append(ratio, ratio_i)


        i_star = np.argmax(ratio)
        print(f"ratioi {ratio[i_star]}")
        print(f"i_star {i_star}")

        if ratio[i_star] < 0:
            return S
        

        S = np.append(S, Xiter[i_star])

        bres = bres - W[i_star]

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