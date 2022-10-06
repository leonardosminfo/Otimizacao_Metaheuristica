import random

# number of items set
num_item = {500, 700, 800, 1000}

# Write file with values
for n in num_item:
    l = n * 6
    b = n * 3

    # Items
    X = []

    for i in range(n):
        X.append(i)

    for j in range(1, 6):

        # Forfeits Set Pairs
        # Different values pair
        F = []
        for i in range(l):
            tpl = (random.randint(0, n), random.randint(0, n))

            while tpl in F:
                rd1 = random.randint(0, n)
                rd2 = random.randint(0, n)
                if rd1 != rd2:
                    tpl = (random.randint(0, n), random.randint(0, n))

            F.append(tpl)

        # Weight and Profit Item Set
        W = []
        P = []
        for i in range(n):
            W.append(random.randint(3, 20))
            P.append(random.randint(5, 25))

        # Forfeit costs set
        D = []
        for i in range(l):
            D.append(random.randint(2, 15))

        with open(f"kpf_{n}_{j}.txt", "w") as f:
            f.write(f"n = {n}\n")
            f.write(f"l = {l}\n")
            f.write(f"b = {b}\n")
            f.write(f"X = {X}\n")
            f.write(f"F = {F}\n")
            f.write(f"W = {W}\n")
            f.write(f"P = {P}\n")
            f.write(f"D = {D}\n")
