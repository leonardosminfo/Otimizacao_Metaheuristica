import sys
import time

import numpy as np

from constructive_algorithm import execute_constructive

# from local_search import execute_local_search
from readinstance import Instance

# from results import generate_results

# filename = sys.argv[1]
# filename = f"500/{filename}"


# execution: python3 main.py --> alterar na mão o grupo de instâncias (500,700,800,1000)


alphas = {0.0, 1.0, 0.7}  # aleatory (0.0), greedy (1.0), semi-greedy(0.7)

for instance in range(1, 11):

    filename = f"500/kpf_{instance}.txt"
    result_filename = filename.replace("/", "_")
    problem_instance = Instance(filename)

    f = open(f"resultados/resultados_{result_filename}", "a")
    f_cons = open(f"resultados_consolidados/resultados_consolidados.txt", "a")
    f_cons.write(f"{filename}\n")

    f.write("#### ALGORITMO CONSTRUTIVO ####\n\n")

    for alpha in alphas:
        f_cons.write("----\n")
        f_cons.write(f"alpha: {alpha}\n")

        cost_list = []
        time_list = []

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

            f.write("----------\n")

            f.write(f"execucao_{execution} para {filename}:\n")
            f.write(f"-> alpha: {alpha}\n")
            f.write(f"-> custo solucao : {cost}\n")
            f.write(f"-> tempo: {wall_time}\n")
            f.write(f"\n")

            cost_list.append(cost)
            time_list.append(wall_time)

        media_custo = np.mean(cost_list)
        dp_custo = np.std(cost_list)
        coef_va_custo = dp_custo / media_custo
        media_tempo = np.mean(time_list)
        dp_tempo = np.std(time_list)
        coef_va_tempo = dp_tempo / media_tempo

        f_cons.write(f"{media_custo}\n")
        f_cons.write(f"{dp_custo}\n")
        f_cons.write(f"{coef_va_custo}\n")
        f_cons.write(f"{media_tempo}\n")
        f_cons.write(f"{dp_tempo}\n")
        f_cons.write(f"{coef_va_tempo}\n")
        f_cons.write("----\n")

    f.write("#### FIM ALGORITMO CONSTRUTIVO ####\n\n")
    f.close()

    # print(f"solution: {solution}")
    # print(f"cost: {cost}")
    # print(f"time: {wall_time}")

# (função gera consolidado)
# gerar tabela consolidada de execução do algoritmo construtivo
# gerar tabela consolidada de execução do algoritmo construtivo + busca local -> melhor construtivo com busca local
# gerar tabela consolidada de execução do algoritmo construtivo + busca local + grasp
