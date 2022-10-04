import sys

from readinstance import Instance

filename = sys.argv[1]
problem_instance = Instance(filename)
problem_instance.convert_attributes_to_list()

def greedyforfeits(X, W, P, b, F, D):
    S = []
    bres = b
    ratio = []

    while X != S:
        Xiter = []
        for i in X:
            if W[i] <= bres and i not in S:
                Xiter.append(i)

        if len(Xiter) == 0:
            return S

        for i in Xiter:
            p_i_line = P[i]
            for pair in F:
                if pair[1] in S:
                    p_i_line = p_i_line - D[F.index(pair)]
        
            ratio_i = p_i_line / W[i]
            
            ratio.append(ratio_i)
            i_star = max(ratio)
            index_i_star = ratio.index(i_star)

      
        if ratio[index_i_star] < 0:
            return S
                
        S.append(index_i_star)
        bres = bres - W[index_i_star]

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
