import sys

from readinstance import Instance

filename = sys.argv[1]
problem_instance = Instance(filename)
problem_instance.convert_attributes_to_list()

print(problem_instance.budget)


def greedyforfeits(X, W, P, b, F, D):
    S = []
    bres = b
    # while X / S != 0:
    #     Xiter = []


greedyforfeits(
    problem_instance.items,
    problem_instance.weights,
    problem_instance.profits,
    problem_instance.budget,
    problem_instance.forfeits_pairs,
    problem_instance.forfeits_costs,
)

# terminal execution: python3 constructivealgorithm.py kpf_500_1.txt
