import pickle
import numpy as np
from matplotlib import pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

neuron_1 = data["neuron1"]
neuron_2 = data["neuron2"]
neuron_3 = data["neuron3"]
neuron_4 = data["neuron4"]
stim = data["stim"]

neuron_1_t = neuron_1.transpose()
neuron_2_t = neuron_2.transpose()
neuron_3_t = neuron_3.transpose()
neuron_4_t = neuron_4.transpose()

neurons_t = [neuron_1_t, neuron_2_t, neuron_3_t, neuron_4_t]
total_neurons = []
totals = []
total = 0
for neuron_t in neurons_t:
    for stimuli in neuron_t:
        for firing_rate in stimuli:
            total = total + firing_rate

        totals.append(total)
        total = 0
    
    for i in range(0, 24):
        totals[i] = totals[i] / 100
    
    total_neurons.append(totals)
    totals = []

x = stim
for total in total_neurons:
    plt.plot(x, total)
    plt.show()

i = 1
for neuron_t in neurons_t:
    for stimuli in neuron_t:
        mean = np.mean(stimuli)
        var = np.var(stimuli)
    
    i = i + 1

with open('pop_coding_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

r1 = np.mean(data["r1"])
r2 = np.mean(data["r2"])
r3 = np.mean(data["r3"])
r4 = np.mean(data["r4"])
c1 = data["c1"]
c2 = data["c2"]
c3 = data["c3"]
c4 = data["c4"]

r = [r1, r2, r3, r4]
c = [c1, c2, c3, c4]
R_div = []
i = 0
for total in total_neurons:
    R_div.append(r[i] / np.max(total))
    i = i + 1
    

vec_pop = np.sum([R_div[0]*c1, R_div[1]*c2, R_div[2]*c3, R_div[3]*c4], axis=0)
mod = np.linalg.norm(vec_pop)
theta = np.degrees(np.arctan(vec_pop[1] / vec_pop[0]))
