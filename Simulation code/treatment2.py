## Run Treatment 2

import numpy as np
import pickle
from functions import choice

N = 1000
n = 10
w_mean = 30
w_vars = [0.5, 1, 2, 3]
v_vars_ratio = np.array([0.5, 1, 2, 3, 4, 5])
costs = [0.01, 0.3, 0.6, 0.9, 1.2, 1.5]

collections = dict()

for w_var in w_vars:
    print("Starting w_var = ", w_var)
    v_vars = v_vars_ratio * w_var
    for v_var in v_vars:
        print("\tStarting v_var = ", v_var)
        for cost in costs:
            print('\t\tStarting cost = ', cost)
            data = np.zeros((N, 5))
            for i in range(N):
                print('\t\t\t\tCurrent Index =', i)
                data[i] = choice(n, w_mean, w_var, v_var, cost, 6)
            with open('../Data/collections_w' + str(w_var) + 'v' + str(v_var) + 'c' + str(cost) + '.pkl', "wb") as file:
                pickle.dump(data, file)
            print('\t\t\tFinished!')