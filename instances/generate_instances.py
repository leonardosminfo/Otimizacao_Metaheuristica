import random

n = 500
l = n * 6
b = n * 3

# Items
X = []

for i in range(n):
    X.append(i)

# Forfeits Set Pairs
# Different values pair
F = []
for i in range(l):
    tpl = (random.randint(0, n), random.randint(0, n))

    while tpl in F:
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

# Write file with values
with open("kpf_500_2.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"l = {l}\n")
    f.write(f"b = {b}\n")
    f.write(f"X = {X}\n")
    f.write(f"F = {F}\n")
    f.write(f"W = {W}\n")
    f.write(f"P = {P}\n")
    f.write(f"D = {D}\n")
