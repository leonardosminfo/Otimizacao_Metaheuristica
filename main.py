import time

import numpy as np

from constructive_algorithm import execute_constructive
from local_search import execute_local_search
from readinstance import Instance

# execution: python3 main.py --> alterar na mão o grupo de instâncias (500,700,800,1000)


alphas = {0.0, 1.0, 0.7}  # aleatory (0.0), greedy (1.0), semi-greedy(0.7)

for instance in range(1, 11):

    filename = f"500/kpf_{instance}.txt"
    result_filename = filename.replace("/", "_")
    problem_instance = Instance(filename)

    f = open(f"resultados_ls/resultados_{result_filename}_ls", "a")

    for alpha in alphas:

        for execution in range(1, 11):

            start_time = time.time()

            solution, cost, scost, sweights, sorted_items = execute_constructive(
                problem_instance.items,
                problem_instance.weights,
                problem_instance.profits,
                problem_instance.budget,
                problem_instance.forfeits_pairs,
                problem_instance.forfeits_costs,
                alpha,
            )

            execute_local_search(solution, cost, scost, sweights1, sorted_items, cap)

            end_time = time.time()
            wall_time = end_time - start_time

            f.write("----------\n")

            f.write(f"execucao_{execution} para {filename}:\n")
            f.write(f"-> alpha: {alpha}\n")
            f.write(f"-> custo solucao : {cost}\n")
            f.write(f"-> tempo: {wall_time}\n")
            f.write(f"\n")

    f.close()


# gerar tabela consolidada de execução do algoritmo construtivo + busca local -> melhor construtivo com busca local
# gerar tabela consolidada de execução do algoritmo construtivo + busca local + grasp
