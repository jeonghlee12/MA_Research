import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pickle

#######################################################################################
##################################### Treatment 1 #####################################
#######################################################################################

# Plot choice prob for each alternative for when w_var changes
def plot_w_var_t1(x_var, costs):
    # set width of bar
    barWidth = 0.12
    
    fig = plt.subplots(figsize =(10, 3))
    
    # set height of bar
    bars = []
    for cost in costs:
        with open('Data/collections_x' + str(x_var) + 'c' + str(cost) + '.pkl', "rb") as f:
            data = pickle.load(f)
        c_p = dict(Counter([i[0] for i in data]))
        for keys in c_p.keys():
            c_p[keys] = c_p[keys] / 1000.
        other_sum = round(sum(v for k, v in c_p.items() if k > 10), 3)
        c_p10 = np.zeros(10)
        for k, v in c_p.items():
            if k <= 10:
                c_p10[int(k) - 1] = v
        bars.append(np.append(c_p10, [other_sum]))

    # Make the plot
    for i in range(len(costs)):
        cost = costs[i]
        plt.bar([x + i * barWidth for x in np.arange(len(bars[0]))], bars[i], width = barWidth,
            edgecolor ='grey', label = cost)
    
    # Adding Xticks
    plt.xlabel('Order of alternatives', fontsize = 12)
    plt.ylabel('Choice Probability', fontsize = 12)
    plt.xticks([r + 2.5 * barWidth for r in range(len(bars[0]))], [str(i) for i in range(1,11)] + ['10 >'])
    plt.title(r"$\sigma_w^2$ = " + str(x_var))
    plt.legend(title = "Cost")
    plt.show()

# Plot choice prob for each alternative for when v_var changes
def plot_v_var_t1(v_var, costs):
    # set width of bar
    barWidth = 0.12
    
    fig = plt.subplots(figsize =(10, 3))
    
    # set height of bar
    bars = []
    for cost in costs:
        with open('Data/collections_v' + str(v_var) + 'c' + str(cost) + '.pkl', "rb") as f:
            data = pickle.load(f)
        c_p = dict(Counter([i[0] for i in data]))
        for keys in c_p.keys():
            c_p[keys] = c_p[keys] / 1000.
        other_sum = round(sum(v for k, v in c_p.items() if k > 10), 3)
        c_p10 = np.zeros(10)
        for k, v in c_p.items():
            if k <= 10:
                c_p10[int(k) - 1] = v
        bars.append(np.append(c_p10, [other_sum]))

    # Make the plot
    for i in range(len(costs)):
        cost = costs[i]
        plt.bar([x + i * barWidth for x in np.arange(len(bars[0]))], bars[i], width = barWidth,
            edgecolor ='grey', label = cost)

    # Adding Xticks
    plt.xlabel('Order of alternatives', fontsize = 12)
    plt.ylabel('Choice Probability', fontsize = 12)
    plt.xticks([r + 2.5 * barWidth for r in range(len(bars[0]))], [str(i) for i in range(1,11)] + ['10 >'])
    plt.title(r"$\sigma_v^2$ = " + str(v_var))
    plt.legend(title = "Cost")
    plt.show()

# Plot choice prob for each alternative by cost for when w_var changes
def plot_cost_x_t1(cost, w_vars):
    # set width of bar
    barWidth = 0.1
    fig = plt.figure(figsize =(8, 3))

    # set height of bar
    bars = []
    for x_var in w_vars:
        with open('Data/collections_x' + str(x_var) + 'c' + str(cost) + '.pkl', "rb") as f:
            data = pickle.load(f)
        c_p = dict(Counter([i[0] for i in data]))
        for keys in c_p.keys():
            c_p[keys] = c_p[keys] / 1000.
        other_sum = round(sum(v for k, v in c_p.items() if k > 10), 3)
        c_p10 = np.zeros(10)
        for k, v in c_p.items():
            if k <= 10:
                c_p10[int(k) - 1] = v
        bars.append(np.append(c_p10, [other_sum]))

    # Make the plot
    for i in range(len(w_vars)):
        x_var = w_vars[i]
        plt.bar([x + i * barWidth for x in np.arange(len(bars[0]))], bars[i], width = barWidth,
            edgecolor ='grey', label = x_var)

    # Adding Xticks
    plt.xlabel('Order of alternatives', fontsize = 12)
    plt.ylabel('Choice Probability', fontsize = 12)
    plt.xticks([r + 2 * barWidth for r in range(len(bars[0]))], [str(i) for i in range(1,11)] + ['10 >'])
    plt.title(r"Cost = " + str(cost))
    plt.legend(title = r"$\sigma_w^2$")
    plt.show()

# Plot choice prob for each alternative by cost for when v_var changes
def plot_cost_v_t1(cost, v_vars):
    # set width of bar
    barWidth = 0.1
    fig = plt.figure(figsize =(8, 3))

    # set height of bar
    bars = []
    for v_var in v_vars:
        with open('Data/collections_v' + str(v_var) + 'c' + str(cost) + '.pkl', "rb") as f:
            data = pickle.load(f)
        c_p = dict(Counter([i[0] for i in data]))
        for keys in c_p.keys():
            c_p[keys] = c_p[keys] / 1000.
        other_sum = round(sum(v for k, v in c_p.items() if k > 10), 3)
        c_p10 = np.zeros(10)
        for k, v in c_p.items():
            if k <= 10:
                c_p10[int(k) - 1] = v
        bars.append(np.append(c_p10, [other_sum]))

    # Make the plot
    for i in range(len(v_vars)):
        v_var = v_vars[i]
        plt.bar([x + i * barWidth for x in np.arange(len(bars[0]))], bars[i], width = barWidth,
            edgecolor ='grey', label = v_var)

    # Adding Xticks
    plt.xlabel('Order of alternatives', fontsize = 12)
    plt.ylabel('Choice Probability', fontsize = 12)
    plt.xticks([r + 2 * barWidth for r in range(len(bars[0]))], [str(i) for i in range(1,11)] + ['10 >'])
    plt.title(r"Cost = " + str(cost))
    plt.legend(title = r"$\sigma_v^2$")
    plt.show()
    
#######################################################################################
##################################### Treatment 2 #####################################
#######################################################################################

# Plot choice prob of first alternative for each w_var at each cost and v_var ratio
def plot_w_var_t2(w_var, costs, v_vars_ratio):
    # set width of bar
    barWidth = 0.12
    
    fig = plt.subplots(figsize =(10, 3))
    
    # set height of bar
    bars = []
    for cost in costs:
        bar = np.array([])
        for ratio in v_vars_ratio:
            with open('Data/collections_w' + str(w_var) + 'v' + str(float(w_var * ratio)) + 'c' + str(cost) + '.pkl', "rb") as f:
                data = pickle.load(f)
            c_p = dict(Counter([i[0] for i in data]))
            for keys in c_p.keys():
                c_p[keys] = c_p[keys] / 1000.
            bar = np.append(bar, c_p[1])
        bars.append(bar)

    # Make the plot
    for i in range(len(costs)):
        cost = costs[i]
        plt.bar([x + i * barWidth for x in np.arange(len(bars[0]))], bars[i], width = barWidth,
            edgecolor ='grey', label = cost)

    # Adding Xticks
    plt.xlabel('Ratio', fontsize = 12)
    plt.ylabel('Choice Probability', fontsize = 12)
    plt.xticks([r + 2.5 * barWidth for r in range(len(bars[0]))], [str(i) for i in range(1,7)])
    plt.title(r"$w$ variance = " + str(w_var))
    plt.legend(title = "Cost")
    plt.show()