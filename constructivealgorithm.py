import numpy as np
from numpy import argmax

from readinstance import Instance

# filename = sys.argv[1]

filename = "500/kpf_1.txt"
problem_instance = Instance(filename)


def greedyforfeits(X, W, P, b, F, D):
    S = np.a
    bres = b
    ratio = []

    while X != S:
        print(S)
        Xiter = []
        for i in X:
            if W[i] <= bres and i not in S:
                Xiter.append(i)

        if not Xiter:
            return S

        print(f"Xiter: {Xiter}")

        for i in Xiter:
            p_i = P[i]
            for pair in F:
                if pair[1] in S:
                    p_i = p_i - D[F.index(pair)]

            ratio_i = p_i / W[i]

            ratio.append(ratio_i)

        i_star = argmax(ratio)

        if ratio[i_star] < 0:
            return S

        S.append(Xiter[i_star])

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
