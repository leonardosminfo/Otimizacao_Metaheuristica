import numpy as np
from numpy import argmax

from readinstance import Instance

# filename = sys.argv[1]

filename = "500/kpf_1.txt"
problem_instance = Instance(filename)

print(problem_instance.forfeits_pairs)


def greedyalgorithm(X, W, P, b, F, D):
    S = np.array([])
    bres = b

    # critério guloso ou custo benefício
    H = np.array([])

    # lista restrita de candidatos
    lcr = np.array([])

    while np.array_equal(S, X) == False:
        Xiter = np.array([])

        print(S)  # print solution
        # print(Xiter)

        for i in X:
            if W[i] <= bres and i not in S:
                Xiter = np.append(Xiter, i)

        if len(Xiter) == 0:
            return S

        # for i in Xiter:
        #     i = int(i)
        #     p_i = P[i]
        #     for pair in F:
        #         if pair[1] in S:
        #             p_i = p_i - D[int(pair[1])]

        for i in Xiter:
            i = int(i)
            p_i = P[i]
            # print(p_i)
            h_i = p_i / W[i]
            H = np.append(H, h_i)

        i_max = argmax(H)
        # i_min = argmin(H)

        if H[i_max] < 0:
            return S

        S = np.append(S, Xiter[i_max])

        bres = bres - W[i]

    return S


solution = greedyalgorithm(
    problem_instance.items,
    problem_instance.weights,
    problem_instance.profits,
    problem_instance.budget,
    problem_instance.forfeits_pairs,
    problem_instance.forfeits_costs,
)

print(solution)
