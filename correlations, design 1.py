# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:38:59 2022

@author: kinga
"""

# Design 1

from scipy.stats import pearsonr
import numpy as np
import matplotlib.pyplot as plt

# Estimate the correlations using pearsonr
m1 = np.linspace(1, 3, 1001)
mu1 = []
for i in range(len(m1)-1):
    mu1.append(np.random.uniform(m1[i], m1[i+1]))

corr = np.zeros(6)

for i in range(100):
    mu2 = []
    for i in range(len(mu1)):
        mu2.append(mu1[i]*np.random.random())
    corr[0] += pearsonr(mu1,mu2)[0]

    mu2 = []
    for i in range(len(mu1)):
        mu2.append(mu1[i]*np.random.uniform(0.15, 0.85))
    corr[1] += pearsonr(mu1,mu2)[0]
    
    mu2 = []
    for i in range(len(mu1)):
        mu2.append(mu1[i]*np.random.uniform(0.25, 0.75))
    corr[2] += pearsonr(mu1,mu2)[0]
    
    mu2 = []
    for i in range(len(mu1)):
        mu2.append(mu1[i]*np.random.uniform(3/8, 5/8))
    corr[3] += pearsonr(mu1,mu2)[0]
    
    mu2 = []
    for i in range(len(mu1)):
        mu2.append(mu1[i]*np.random.uniform(0.45, 0.55))
    corr[4] += pearsonr(mu1,mu2)[0]
    
    mu2 = []
    for i in range(len(mu1)):
        mu2.append(mu1[i]*0.5)
    corr[5] += pearsonr(mu1,mu2)[0]

r_est = corr/100


# Calculate true correlations
bounds = [[0, 1], [0.15, 0.85], [0.25, 0.75], [3/8, 5/8], [0.45, 0.55], [0.4999, 0.5001]]

r_true = []

for i in range(len(bounds)):
    u_sq_exp = (bounds[i][1]**3 - bounds[i][0]**3) /3 / (bounds[i][1]-bounds[i][0])
    sigma = np.sqrt(u_sq_exp*13/3 - 1)
    r_true.append(np.sqrt(3)/6/sigma)
    

# Graph L-corr with true correlations
L_1stcome1 = [7.321271129999955,
7.219784684578419,
7.167987564171929,
7.15303306580968,
7.14509118617425,
7.12898191755242]

L_random1 = [7.359659139631293,
7.2641499537522565,
7.223325376801822,
7.201955193021691,
7.189842284057741,
7.181768031757221]

L_longerq1 = [7.181874998081911,
7.09106417974319,
7.042875810501167,
7.000691683075959,
6.995039801398681,
6.986955045987339]

L_1stcome2 = [7.303388256454551,
7.205905433597238,
7.175115243906795,
7.13494629289076,
7.130695873597605,
7.145878298394985]

L_random2 = [7.367817620766305,
7.263835541886974,
7.230139075252559,
7.201252159675573,
7.193838155414793,
7.194856351304077]

L_longerq2 = [7.169199742761596,
7.059573055227425,
7.035349626123211,
6.999245752339627,
6.992858463200825,
6.99729713494992]

L_1stcome3 = [7.3230639387124175,
7.221115150267747,
7.174796918252012,
7.147641815958835,
7.130339053533651,
7.12831187893249]

L_random3 = [7.3656731773893025,
7.268933797794095,
7.214447133420984,
7.201531487738146,
7.183617305237024,
7.180545391871358]

L_longerq3 = [7.191429674287358,
7.066558120029754,
7.028010175876359,
7.00253637590126,
6.990638980961083,
6.991089657617245]

L_1stcome = []
L_random = []
L_longerq = []
for i in range(6):
    L_1stcome.append((L_1stcome1[i] + L_1stcome2[i] + L_1stcome3[i])/3)
    L_random.append((L_random1[i] + L_random2[i] + L_random3[i])/3)
    L_longerq.append((L_longerq1[i] + L_longerq2[i] + L_longerq3[i])/3)
    

fig, ax = plt.subplots()
ax.plot(r_true, L_1stcome, marker = 'o', label = '1st come, 1st served')
ax.plot(r_true, L_random, marker = 'o', label = 'Random choice of next customer type')
ax.plot(r_true, L_longerq, marker = 'o', label = 'Serve next customer from longer queue')
ax.legend()
ax.set(xlabel = r'Correlation between $\mu_{i1}$ and $\mu_{i2}$', ylabel = r'$L_{avg}$')