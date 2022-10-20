import sys
import time

from constructive_algorithm import execute_constructive

# from local_search import execute_local_search
from readinstance import Instance

# filename = sys.argv[1]
# filename = f"500/{filename}"


# execution: python3 main.py 500/kpf_1.txt

alphas = {0.0, 1.0, 0.7}  # aleatory (0.0), greedy (1.0), semi-greedy(0.7)

for instance in range(1, 11):

    filename = f"500/kpf_{instance}.txt"
    result_filename = filename.replace("/", "_")
    problem_instance = Instance(filename)

    f = open(f"resultados/resultados_{result_filename}", "a")

    for alpha in alphas:

        for execution in range(1, 11):

            start_time = time.time()

            solution, cost, scost, sweights = execute_constructive(
                problem_instance.items,
                problem_instance.weights,
                problem_instance.profits,
                problem_instance.budget,
                problem_instance.forfeits_pairs,
                problem_instance.forfeits_costs,
                alpha,
            )

            end_time = time.time()
            wall_time = end_time - start_time

            f.write("----------")

            f.write(f"execucao_{execution} para {filename}:\n")
            f.write(f"-> alpha: {alpha}\n")
            f.write(f"-> custo solucao : {cost}\n")
            f.write(f"-> tempo: {wall_time}\n")
            f.write(f"\n")

            f.write("----------")

    f.close()

    # print(f"solution: {solution}")
    # print(f"cost: {cost}")
    # print(f"time: {wall_time}")
