import random as rd
import sys
import time

import numpy as np

from readinstance import Instance

filename = sys.argv[1]
alpha = float(sys.argv[2])

filename = f"500/{filename}"
problem_instance = Instance(filename)


def calculate_penalty(items, forfeits_pairs, forfeits_costs):
    mD = np.zeros((int(len(items)), int(len(items))))

    for index, pair in enumerate(forfeits_pairs):
        mD[int(pair[0]), int(pair[1])] = forfeits_costs[index]
    return mD


def greedyalgorithm(items, weights, profits, budget, alpha, mD):

    # print(sorted_items)
    solution = []
    scost = []  # solution cost
    sweights = []  # solution weights
    cost = 0

    if alpha == 0:  # totalmente aleatório
        remaining_items = zip(items, weights, profits)
        sorted_items = sorted(
            remaining_items, key=lambda x: x[2] / (x[1] + 1), reverse=True
        )
        # print(tuple(items))

        rd_index = rd.choice(range(0, len(sorted_items)))
        candidate = sorted_items[rd_index][0]

        while budget - weights[candidate] > 0:
            budget = budget - weights[candidate]
            solution.append(candidate)

            penalidade = sum(mD[candidate][solution])
            # if penalidade>0: print(f"Penalidade do Item {sorted_items[rd_index][0]} é {penalidade}")

            cost = cost + profits[candidate] - penalidade

            scost.append(profits[candidate] - penalidade)

            sweights.append(weights[candidate])

            sorted_items.remove(sorted_items[rd_index])
            rd_index = rd.choice(range(0, len(sorted_items)))
            candidate = sorted_items[rd_index][0]

    else:
        if alpha == 1:  # totalmente guloso
            remaining_items = zip(items, weights, profits)
            # print(tuple(items))
            sorted_items = sorted(
                remaining_items, key=lambda x: x[2] / (x[1] + 1), reverse=True
            )
            # sorted_items=sorted(remaining_items, key= lambda x:x[2]/x[1], reverse=True)
            # print(sorted_items)
            candidate = sorted_items[0][0]
            while budget - weights[candidate] > 0:

                # calcula a nova penalidade para o item a ser inserido no conjunto e reordena
                # sorted_items=sorted(sorted_items, key= lambda x:(x[2]/x[1])-sum(mD[x[0]][solution]), reverse=True)

                budget = budget - weights[candidate]
                solution.append(candidate)

                penalidade = sum(mD[candidate][solution])
                # if penalidade>0: print(f"Penalidade do Item {sorted_items[0][0]} é {penalidade}")

                # cost=cost+sorted_items[0][2]
                cost = cost + profits[candidate] - penalidade
                # cost=cost+sorted_items[index][2]-sum(mD[sorted_items[index][0]][solution])

                scost.append(profits[candidate] - penalidade)

                sweights.append(weights[candidate])

                # sorted_items=sorted(sorted_items, key= lambda x:(x[2]-sum(mD[x[0]][solution]))/(x[1]+1), reverse=True)
                sorted_items.remove(sorted_items[0])

                if len(sorted_items) >= 0:
                    # sorted_items=sorted(sorted_items, key= lambda x:(x[2]-sum(mD[x[0]][solution]))/(x[1]+1), reverse=True)
                    candidate = sorted_items[0][0]
                # sorted_items.remove(sorted_items[index])
                # index=index+1

        else:  # semi-guloso
            remaining_items = zip(items, weights, profits, profits / weights)
            sorted_items = sorted(
                remaining_items, key=lambda x: x[2] / (x[1] + 1), reverse=True
            )

            # o cálculo dos limites da lcr
            hmax = sorted_items[0][3]
            hmin = sorted_items[-1][3]

            # ub = hmax + alpha * (hmin - hmax)
            lb = hmin
            ub = hmax + alpha * (hmin - hmax)

            # lista restrita de candidatos
            # lcr=list(filter(lambda x: x[3]<=ub and x[3] >= lb, sorted_items))
            lcr = list(filter(lambda x: x[3] >= ub, sorted_items))
            rd_index = rd.choice(range(0, len(lcr)))
            candidate = lcr[rd_index][0]

            # print(candidate)
            while budget - weights[candidate] > 0:

                budget = budget - weights[candidate]
                solution.append(candidate)
                # print(f" Solution: {solution}")

                # penalidade
                penalidade = sum(mD[candidate][solution])
                # if penalidade>0: print(f"Penalidade do Item {sorted_items[rd_index][0]} é {penalidade}")

                cost = cost + profits[candidate] - penalidade

                scost.append(profits[candidate] - penalidade)

                sweights.append(weights[candidate])

                # removendo o item já inserido
                sorted_items.remove(sorted_items[sorted_items.index(lcr[rd_index])])

                # sorted_items.sort(key= lambda x:(x[2]-sum(mD[x[0]][solution]))/(x[1]+1), reverse=True)

                # o cálculo dos limites da lcr
                hmax = sorted_items[0][3]
                hmin = sorted_items[-1][3]

                # ub = hmax + alpha * (hmin - hmax)
                lb = hmin
                ub = hmax + alpha * (hmin - hmax)

                # lista restrita de candidatos
                lcr = list(filter(lambda x: x[3] >= ub, sorted_items))

                # print(f"LCR: {lcr}")
                rd_index = rd.choice(range(0, len(lcr)))
                candidate = lcr[rd_index][0]

    return solution, cost, scost, sweights


start_time = time.time()

mD = calculate_penalty(
    problem_instance.items,
    problem_instance.forfeits_pairs,
    problem_instance.forfeits_costs,
)


solution, cost, scost, sweights = greedyalgorithm(
    problem_instance.items,
    problem_instance.weights,
    problem_instance.profits,
    problem_instance.budget,
    alpha,
    mD,
)

end_time = time.time()

wall_time = end_time - start_time


print(f"solution: {solution}")
print(f"cost: {cost}")
print(f"time: {wall_time}")
