# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:51:29 2022

@author: kinga
"""

import numpy as np
from ________ import Simulation

# mean service rates
# Try different variances: mu ~ U[1,3] or U[1.5, 2.5] or U[1.9, 2.1]

Lambda = np.linspace(1,8,10)

m1 = np.linspace(1.9, 2.1, 21)
mu1 = []
for i in range(len(m1)-1):
    mu1.append(np.random.uniform(m1[i], m1[i+1]))
m2 = np.linspace(1.9, 2.1, 21)
mu2 = []
for i in range(len(m2)-1):
    mu2.append(np.random.uniform(m2[i], m2[i+1]))
m3 = np.linspace(1.9, 2.1, 21)
mu3 = []
for i in range(len(m3)-1):
    mu3.append(np.random.uniform(m3[i],m3[i+1]))

for l in Lambda:
    L=0
    for i in range(len(mu1)):
        for j in range(len(mu2)):
            for k in range(len(mu3)):
                s = Simulation(l, np.array([mu1[i], mu2[j], mu3[k]]), 2)
                s.run()
                L += s.total_wait / s.t_termination
            
    print(L/len(mu1)/len(mu2)/len(mu3))