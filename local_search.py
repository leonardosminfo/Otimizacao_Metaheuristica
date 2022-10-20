def execute_local_search(solution, cost, scost, sweights1, sorted_items, cap):
    # cap capacidade restante
    # sorted_items  items que nao foram incluidos na solucao anterior
    s1 = solution
    scost1 = scost
    cost1 = cost
    scap1 = cap

    s_mudou = False
    s1_items = zip(s1, sweights1, scost1)

    s1_items = sorted(s1_items, key=lambda x: x[2] / (x[1] + 1), reverse=True)

    size_s1 = len(s1_items)

    size_items = len(sorted_items)
    cont_solucao = size_s1 - 1

    # enquanto nao encontrar melhoria e nao percorrer toda a solucao original
    while s_mudou == False and cont_solucao >= 0:

        # pegando o proximo item (do pior beneficio custo na solucao em diante)
        bad_item = s1_items[cont_solucao][0]

        # verificando a capacidade da mochila que deverá ser ocupada
        scapaux = scap1 + s1_items[cont_solucao][1]

        # ordenando os itens restantes da mochila, a partir do critério guloso
        sorted_items = sorted(
            sorted_items,
            key=lambda x: (x[2] - sum(mD[x[0]][s1])) / (x[1] + 1),
            reverse=True,
        )
        j = 0
        # percorrendo os itens que nao entraram na mochila, para verificar se algum pode substituir
        while scapaux - sorted_items[0][1] > 0 and j < len(sorted_items):

            sweights1.append(sweights1[s1.index(s1_items[cont_solucao][0])])

            penalidade = sum(mD[sorted_items[0][0]][s1])
            # if penalidade>0: print(f"Penalidade do Item {sorted_items[0][0]} é {penalidade}")

            cost1 = cost + sorted_items[0][2] - penalidade

            # fazer o teste para verificar se o resultado da solucao anterior é melhor que resultado da solucao antiga
            if cost1 > cost:
                s_mudou = True

                # print(f"COST Anterior:{cost}\n Novo COST {cost1}\n Novo Item{sorted_items[j][0]} \n Item Retirado{s1[s1.index(s1_items[cont_solucao][0])]}")

                print(
                    f" Novo Item: {sorted_items[0][0]} \n Item Retirado: {s1[s1.index(s1_items[cont_solucao][0])]}"
                )
                # print(f" Novo Item: {sorted_items[j][0]} \n Item Retirado: {s1[s1.index(s1_items[cont_solucao][0])]}")

                # adiciona na nova solucao o item
                s1.append(sorted_items[0][0])

                scapaux = scapaux - sorted_items[0][1]
                scost1.append(sorted_items[0][2] - penalidade)
                sweights1.append(sorted_items[0][1])

                sorted_items.remove(sorted_items[0])
                scost1.remove(scost1[s1.index(s1_items[cont_solucao][0])])
                s1.remove(s1[s1.index(s1_items[cont_solucao][0])])
                cost = cost1
                scap1 = scapaux
                break

            sorted_items = sorted(
                sorted_items,
                key=lambda x: (x[2] - sum(mD[x[0]][s1])) / (x[1] + 1),
                reverse=True,
            )
            j = j + 1

        # verifica se a solução proposta é melhor que a atual
        if s_mudou == True:
            return s1, cost1, scost1, scap1, sweights1, sorted_items
        else:
            cont_solucao = cont_solucao - 1
            # if cont_solucao<214:
            # s_mudou==True

    if s_mudou == False:
        return solution, cost, scost, cap, sweights1, sorted_items
    else:
        return s1, cost1, scost1, scap1, sweights1, sorted_items
