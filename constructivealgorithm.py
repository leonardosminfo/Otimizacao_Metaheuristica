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
        for i in X:
            if W[i] <= bres and i not in S:
                Xiter = np.append(Xiter, i)

        if len(Xiter) == 0:
            return S

        # print(Xiter) # print valores a serem adicionados na mochila

        for i in Xiter:
            i = int(i)
            p_i = P[i]
            for pair in F:
                if pair[1] in S:
                    # print(np.argwhere(F == pair))
                    # print(F)
                    # print(S)
                    # p_i = p_i - D[F.index(pair)]
                    # p_i = p_i - D[np.argwhere(F == pair)]
                    p_i = p_i - D[int(pair[1])]

            ratio_i = p_i / W[i]

            ratio = np.append(ratio, ratio_i)

        i_star = np.argmax(ratio)

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
