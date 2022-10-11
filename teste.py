import sys
import time

import numpy as np

from readinstance import Instance

filename = sys.argv[1]
alpha = float(sys.argv[2])

filename = f"500/{filename}"
problem_instance = Instance(filename)


def greedyalgorithm(X, W, P, b, F, D, alpha):
    S = np.array([])
    bres = b = 25

    print(X)
    print(b)
    print(f"Pesos item: {W}")
    print(f"Custos item: {P}")

    f = {}
    keys = []

    values = range(3000)

    for pair in F:
        keys.append(pair[0])

    for i in keys:
        i = int(i)
        f[i] = values[i]

    print(f)

    while np.array_equal(S, X) == False:
        # elementos a serem adicionados na lista
        Xiter = np.array([])

        # critério guloso ou custo benefício
        H = np.array([])
        H_aux = []

        # lista restrita de candidatos
        lcr = np.array([])

        print("################")
        print()

        print(f"Solution: {S}")  # print solution

        for i in X:
            if W[i] <= bres and i not in S:
                Xiter = np.append(Xiter, i)

        print(f"A ser adicionado {Xiter}")

        if len(Xiter) == 0:
            return S

        # for i in Xiter: # forfeit costs
        #     i = int(i)
        #     p_i = P[i]
        #     for pair in F:
        #         if pair[1] in S:
        #             p_i = p_i - D[int(pair[1])]

        # f = {182: [(224, 15), (277, 8)]}

        # for par in f[i]:
        #     if par[0] in S:
        #         pi = pi - par[1]

        for i in Xiter:
            i = int(i)
            p_i = P[i]
            h_i = p_i / W[i]

            tpl_cost = (i, h_i)

            H = np.append(H, h_i)
            H_aux.append(tpl_cost)

        print(f"Custos benefícios: {H}")

        i_max = np.argmax(H)
        i_min = np.argmin(H)

        # o cálculo dos limites da lcr
        ub = H[i_max] + alpha * (H[i_min] - H[i_max])
        lb = H[i_min]

        if round(ub, 5) == round(lb, 5):  # guloso

            i_max = np.argmax(H)

            S = np.append(S, Xiter[i_max])

            bres = bres - W[i_max]
        else:  # semi-guloso ou aleatório
            for h_i in H:
                if h_i >= lb and h_i <= ub:
                    for item, j in H_aux:
                        if item not in lcr:
                            lcr = np.append(lcr, item)

            print(f"lista de candidatos: {lcr}")

            candidate = int(np.random.choice(lcr))

            S = np.append(S, candidate)

            bres = bres - W[candidate]

    return S


start_time = time.time()

solution = greedyalgorithm(
    problem_instance.items[:6],
    problem_instance.weights[:6],
    problem_instance.profits[:6],
    problem_instance.budget,
    problem_instance.forfeits_pairs,
    problem_instance.forfeits_costs,
    alpha,
)

end_time = time.time()

wall_time = end_time - start_time

cost = 0
weight = 0
for sol in solution:
    sol = int(sol)
    cost = cost + problem_instance.profits[sol]
    weight = weight + problem_instance.weights[sol]


print(cost)
print(weight)

# f = open(f"resultados/resultados_500_3.txt", "a")

# f.write(f"execucao_{i} para {filename}:\n")
# f.write(f"-> alpha: {alpha}\n")
# f.write(f"-> custo solucao : {cost}\n")
# f.write(f"-> tempo: {wall_time}\n")
# f.write(f"\n")

# f.close()
