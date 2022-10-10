B=        #capacidade da mochila
S=[]           #  Estes dois devem receber a mesma solução viável inicial
S2=[]          #  vinda do construtivo quando se inicia o programa.
s_mudou=True
while s_mudou==True:
    s_mudou=False
    for i in S:                              #
        i = int(i)                           #   Esta parte do algoritmo
        p_i = P[i]                           #   desempenha a função de 
        for pair in F:                       #   calcular a densidade dos
            if pair[1] in S:                 #   itens da solução corrente
                p_i = p_i - D[int(pair[1])]  #   S.
        h_i = p_i / W[i]                     #
        H = np.append(H, h_i)                #
    lista_itens=                  #Esta lista é S organizado em ordem crescente de densidades. Eu não sei como fazer isso.
    num_itens_lista=len(lista_itens)  #Calcula número de itens da solução
    i=1            #Esse i serve apenas para o while loop seguinte
    while i<=num_itens_lista and s_mudou==False:
        pior_item=lista_itens[i]       #Iem com pior valor de densidade
        Saux=S            #variável auxiliar
        S=S-(pior_item)           #Retira-se da solução S o pior item
        X=I-S                #Defini-se como X os itens que não estão na solução S
        for i in X:                                #
            i = int(i)                             #   Esta parte do algoritmo
            p_i2 = P[i]                            #   desempenha a função de 
            for pair in F:                         #   calcular a densidade dos
                if pair[1] in S:                   #   itens que NÃO estão dentro da solução corrente
                    p_i2 = p_i2 - D[int(pair[1])]  #   S.
            h_i2 = p_i2 / W[i]                     #
            H2 = np.append(H, h_i2)                #
        for i in S:           #   Esta parte calcula Bres que
            Bres=B-W[i]         #   é a capacidade restante.
        for i in X:
            while H2[i]>0 and W[i]<=Bres:   #
                if H2[i]==max(H2):          # Identifica o item fora da solução (X) com maior densidade
                    melhor_item=X[i]        # e acrescenta este item na solução S.
                    S=S+(melhor_item)       #
        if S!=Saux:
            s_mudou=True
            if V(S)>V(S2):      #V(S) é o valor da solução S
                S2=S            #
        i=i+1         #Repete-se o loop com i+1
return S
return S2