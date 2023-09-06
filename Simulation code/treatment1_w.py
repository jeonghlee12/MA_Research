## Run Treatment 1 case with fixed sigma_v

import numpy as np
import pickle
from functions import choice

N = 1000
n = 10
w_mean = 30
w_vars = [1,2,3,4,5]
v_var = 3
costs = [0.01, 0.3, 0.6, 0.9, 1.2, 1.5]

collections = dict()

print("v_var = ", v_var)
for w_var in w_vars:
    print("\tStarting w_var = ", w_var)
    for cost in costs:
        print('\t\tStarting cost = ', cost)
        data = np.zeros((N, 5))
        for i in range(N):
            print('\t\t\t\tCurrent Index =', i)
            data[i] = choice(n, w_mean, w_var, v_var, cost, 4)
        with open('../Data/collections_x' + str(w_var) + 'c' + str(cost) + '.pkl', "wb") as file:
            pickle.dump(data, file)
        print('\t\t\tFinished!')