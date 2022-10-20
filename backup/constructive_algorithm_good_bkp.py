import sys
import time

import numpy as np

from readinstance import Instance

filename = sys.argv[1]
alpha = float(sys.argv[2])

filename = f"500/{filename}"
problem_instance = Instance(filename)


def penalty(candidate, solution, forfeits_costs, forfeits):

    cost_pair = 0

    if candidate in forfeits:
        for j in solution:
            tpl = np.array((candidate, j))
            for pair in forfeits:
                if np.array_equal(pair, tpl):
                    index = np.where(forfeits == pair)[0][1]
                    cost_pair = forfeits_costs[index]

    print(cost_pair)

    return cost_pair


def greedyalgorithm(items, weights, profits, budget, forfeits_costs, forfeits, alpha):

    solution = np.array([])
    remaining_items = items
    cost = 0
    index = 0

    # print(f"pesos: {weights}")
    # print(f"lucros: {profits}")

    # budget = 25

    while budget > 0 and remaining_items.size != 0:
        # critério guloso ou custo benefício
        H = np.array([])

        # lista restrita de candidatos
        lcr = np.array([])

        # print(f"itens restantes:{remaining_items}")
        print(f"solucao: {solution}")
        for item in remaining_items:
            h_i = profits[item] / weights[item]
            H = np.append(H, h_i)

        i_max = np.argmax(H)
        i_min = np.argmin(H)

        H_zip = zip(H, remaining_items)

        # o cálculo dos limites da lcr
        ub = H[i_max] + alpha * (H[i_min] - H[i_max])
        lb = H[i_min]

        # print(f"custo benefícios: {H}")
        # print(f"bounds: {(lb,ub)}")

        if alpha == 0:  # aleatório

            candidate = int(np.random.choice(remaining_items))
            budget = budget - weights[candidate]
            cost = cost + profits[candidate]
            solution = np.append(solution, candidate)
            remaining_items = np.delete(
                remaining_items, np.argwhere(remaining_items == candidate)
            )
        elif alpha == 1:  # guloso

            for h_i, item in H_zip:
                if H[i_max] == h_i:
                    candidate = item

            budget = budget - weights[candidate]
            cost = cost + profits[candidate]
            solution = np.append(solution, candidate)
            remaining_items = np.delete(
                remaining_items, np.argwhere(remaining_items == candidate)
            )

        else:  # semi-guloso

            for h_i, item in H_zip:
                if h_i >= lb and h_i <= ub:
                    lcr = np.append(lcr, item)

            # print(f"lista de candidatos: {lcr}")

            candidate = int(np.random.choice(lcr))
            budget = budget - weights[candidate]
            cost = cost + profits[candidate]
            solution = np.append(solution, candidate)
            remaining_items = np.delete(
                remaining_items, np.argwhere(remaining_items == candidate)
            )

    print(cost)

    return solution


start_time = time.time()


solution = greedyalgorithm(
    problem_instance.items,
    problem_instance.weights,
    problem_instance.profits,
    problem_instance.budget,
    problem_instance.forfeits_costs,
    problem_instance.forfeits_pairs,
    alpha,
)

print(problem_instance.forfeits_pairs)

end_time = time.time()

wall_time = end_time - start_time


print(solution)
print(wall_time)
