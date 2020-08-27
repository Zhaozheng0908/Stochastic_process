
import numpy as np

group = {}
seq = [i for i in range(19)]
print(seq)
for n in range(1, 4):
    name = 'group'+str(n)
    choice = (np.random.choice(seq, 5, replace=False)).tolist()
    group[name] = choice
    seq = [x for x in seq if x not in group[name]]

group['group4'] = seq

print(group)