import numpy as np

forfeits = np.array([[1, 6], [3, 9], [3, 5]])
forfeits_cost = np.array([4, 5, 8])

print(forfeits.size)

solution = np.array([1, 3, 4, 5, 6, 9])

candidate = 3

cartesian_sol = np.transpose(
    [np.tile(solution, len(solution)), np.repeat(solution, len(solution))]
)

test = np.array([])


if candidate in forfeits:
    for j in solution:
        tpl = np.array((candidate, j))
        for pair in forfeits:
            if np.array_equal(pair, tpl):
                index = np.where(forfeits == pair)[0][1]
                print((pair, index))
                print(forfeits_cost[index])

    # # solution_cartesian_product = np.transpose(
    # #     [np.tile(solution, len(solution)), np.repeat(solution, len(solution))]
    # # )

    # for pair in solution_cartesian_product:
    #     if pair in forfeits_costs:
    #         pass

    # if candidate in solution:
    #     pair = candidate
