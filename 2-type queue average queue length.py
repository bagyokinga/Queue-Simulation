# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:34:59 2022

@author: kinga
"""

import numpy as np
from ________ import Simulation


# Design 1

# mean service rates
m1 = np.linspace(1, 3, 21)
mu1 = []
for i in range(len(m1)-1):
    mu1.append(np.random.uniform(m1[i], m1[i+1]))
m2 = np.linspace(1, 3, 21)
mu2 = []
for i in range(len(m2)-1):
    mu2.append(np.random.uniform(m2[i], m2[i+1]))
m3 = np.linspace(1, 3, 21)
mu3 = []
for i in range(len(m3)-1):
    mu3.append(np.random.uniform(m3[i],m3[i+1]))

# Find average queue length for different dependencies
# u ~ U[0,1]
L=0
for i in mu1:
    for j in mu2:
        for k in mu3:
            s = Simulation([8,5], np.array([[i,j,k], 
                                            [np.random.random()*i,
                                            np.random.random()*j,
                                            np.random.random()*k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1)/len(mu2)/len(mu3))

# u ~ U[0.15, 0.85]
L=0
for i in mu1:
    for j in mu2:
        for k in mu3:
            var1 = np.random.random() * 0.7 + 0.15
            var2 = np.random.random() * 0.7 + 0.15
            var3 = np.random.random() * 0.7 + 0.15
            s = Simulation([8,5], np.array([[i,j,k], [var1*i, var2*j, var3*k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1)/len(mu2)/len(mu3))

# u ~ U[0.25, 0.75]
L=0
for i in mu1:
    for j in mu2:
        for k in mu3:
            var1 = np.random.random() * 0.5 + 0.25
            var2 = np.random.random() * 0.5 + 0.25
            var3 = np.random.random() * 0.5 + 0.25
            s = Simulation([8,5], np.array([[i,j,k], [var1*i, var2*j, var3*k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1)/len(mu2)/len(mu3))

# u ~ U[0.375, 0.625]
L=0
for i in mu1:
    for j in mu2:
        for k in mu3:
            var1 = np.random.random() * 0.25 + 0.375
            var2 = np.random.random() * 0.25 + 0.375
            var3 = np.random.random() * 0.25 + 0.375
            s = Simulation([8,5], np.array([[i,j,k], [var1*i, var2*j, var3*k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1)/len(mu2)/len(mu3))

# u ~ U[0.45, 0.55]
L=0
for i in mu1:
    for j in mu2:
        for k in mu3:
            var1 = np.random.random() * 0.1 + 0.45
            var2 = np.random.random() * 0.1 + 0.45
            var3 = np.random.random() * 0.1 + 0.45
            s = Simulation([8,5], np.array([[i,j,k], [var1*i, var2*j, var3*k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1)/len(mu2)/len(mu3))

# u = 0.5
L=0
for i in mu1:
    for j in mu2:
        for k in mu3:
            s = Simulation([8,5], np.array([[i,j,k], [0.5*i,0.5*j,0.5*k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1)/len(mu2)/len(mu3))


###

# Design 2

# Bounds to split mu_i1 into 20 intervals of equal area

bounds = np.array([[1.        , 1.1       , 1.2       , 1.3       , 1.4       ,
        1.5       , 1.6       , 1.7       , 1.8       , 1.9       ,
        2.        , 2.1       , 2.2       , 2.3       , 2.4       ,
        2.5       , 2.6       , 2.7       , 2.8       , 2.9       ,
        3.        ],
       [1.        , 1.10682983, 1.208     , 1.307     , 1.406     ,
        1.505     , 1.604     , 1.703     , 1.802     , 1.901     ,
        2.        , 2.099     , 2.198     , 2.297     , 2.396     ,
        2.495     , 2.594     , 2.693     , 2.792     , 2.89317017,
        3.        ],
       [1.        , 1.11580885, 1.22428068, 1.32665513, 1.424     ,
        1.52      , 1.616     , 1.712     , 1.808     , 1.904     ,
        2.        , 2.096     , 2.192     , 2.288     , 2.384     ,
        2.48      , 2.576     , 2.67334487, 2.77571932, 2.88419115,
        3.        ],
       [1.        , 1.12446712, 1.23951212, 1.34699742, 1.44824241,
        1.54422221, 1.636     , 1.727     , 1.818     , 1.909     ,
        2.        , 2.091     , 2.182     , 2.273     , 2.364     ,
        2.45577779, 2.55175759, 2.65300258, 2.76048788, 2.87553288,
        3.        ],
       [1.        , 1.1326665 , 1.25327217, 1.36460858, 1.46853229,
        1.56635217, 1.65903201, 1.74730583, 1.832     , 1.916     ,
        2.        , 2.084     , 2.168     , 2.25269417, 2.34096799,
        2.43364783, 2.53146771, 2.63539142, 2.74672783, 2.8673335 ,
        3.        ],
       [1.        , 1.14017543, 1.26491106, 1.37840488, 1.4832397 ,
        1.58113883, 1.67332005, 1.76068169, 1.84390889, 1.92353841,
        2.        , 2.07646159, 2.15609111, 2.23931831, 2.32667995,
        2.41886117, 2.5167603 , 2.62159512, 2.73508894, 2.85982457,
        3.        ],
       [1.        , 1.14657277, 1.27331263, 1.38659176, 1.48996124,
        1.58564065, 1.67512711, 1.7594871 , 1.84      , 1.92      ,
        2.        , 2.08      , 2.16      , 2.2405129 , 2.32487289,
        2.41435935, 2.51003876, 2.61340824, 2.72668737, 2.85342723,
        3.        ],
       [1.        , 1.15099933, 1.27635609, 1.3859006 , 1.48443534,
        1.57473401, 1.66      , 1.745     , 1.83      , 1.915     ,
        2.        , 2.085     , 2.17      , 2.255     , 2.34      ,
        2.42526599, 2.51556466, 2.6140994 , 2.72364391, 2.84900067,
        3.        ],
       [1.        , 1.15136195, 1.26932802, 1.36941536, 1.46      ,
        1.55      , 1.64      , 1.73      , 1.82      , 1.91      ,
        2.        , 2.09      , 2.18      , 2.27      , 2.36      ,
        2.45      , 2.54      , 2.63058464, 2.73067198, 2.84863805,
        3.        ],
       [1.        , 1.14058773, 1.24      , 1.335     , 1.43      ,
        1.525     , 1.62      , 1.715     , 1.81      , 1.905     ,
        2.        , 2.095     , 2.19      , 2.285     , 2.38      ,
        2.475     , 2.57      , 2.665     , 2.76      , 2.85941227,
        3.        ],
       [1.        , 1.1       , 1.2       , 1.3       , 1.4       ,
        1.5       , 1.6       , 1.7       , 1.8       , 1.9       ,
        2.        , 2.1       , 2.2       , 2.3       , 2.4       ,
        2.5       , 2.6       , 2.7       , 2.8       , 2.9       ,
        3.        ]])

# Choose uniform samples of mu-s from sub-intervals
mu1 = np.zeros((11,20))
mu2 = np.zeros((11,20))
mu3 = np.zeros((11,20))

for i in range(len(bounds)):
    for j in range(len(bounds[0])-1):
        mu1[i][j] = np.random.uniform(bounds[i][j], bounds[i][j+1])
        mu2[i][j] = np.random.uniform(bounds[i][j], bounds[i][j+1])
        mu3[i][j] = np.random.uniform(bounds[i][j], bounds[i][j+1])


# Find average queue length for different dependencies
L=0
for i in mu1[0]:
    for j in mu2[0]:
        for k in mu3[0]:
            s = Simulation([8,5], np.array([[i,j,k],
                                            [3 + np.random.uniform(1,3),
                                            3 + np.random.uniform(1,3),
                                            3 + np.random.uniform(1,3)]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[1]:
    for j in mu2[1]:
        for k in mu3[1]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-1.8), min(3, i+1.8)),
                  3 + np.random.uniform(max(1, j-1.8), min(3, j+1.8)),
                  3 + np.random.uniform(max(1, k-1.8), min(3, k+1.8))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[2]:
    for j in mu2[2]:
        for k in mu3[2]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-1.6), min(3, i+1.6)),
                  3 + np.random.uniform(max(1, j-1.6), min(3, j+1.6)),
                  3 + np.random.uniform(max(1, k-1.6), min(3, k+1.6))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[3]:
    for j in mu2[3]:
        for k in mu3[3]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-1.4), min(3, i+1.4)),
                  3 + np.random.uniform(max(1, j-1.4), min(3, j+1.4)),
                  3 + np.random.uniform(max(1, k-1.4), min(3, k+1.4))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))


L=0
for i in mu1[4]:
    for j in mu2[4]:
        for k in mu3[4]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-1.2), min(3, i+1.2)),
                  3 + np.random.uniform(max(1, j-1.2), min(3, j+1.2)),
                  3 + np.random.uniform(max(1, k-1.2), min(3, k+1.2))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))


L=0
for i in mu1[5]:
    for j in mu2[5]:
        for k in mu3[5]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-1), min(3, i+1)),
                  3 + np.random.uniform(max(1, j-1), min(3, j+1)),
                  3 + np.random.uniform(max(1, k-1), min(3, k+1))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[6]:
    for j in mu2[6]:
        for k in mu3[6]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-0.8), min(3, i+0.8)),
                  3 + np.random.uniform(max(1, j-0.8), min(3, j+0.8)),
                  3 + np.random.uniform(max(1, k-0.8), min(3, k+0.8))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[7]:
    for j in mu2[7]:
        for k in mu3[7]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-0.6), min(3, i+0.6)),
                  3 + np.random.uniform(max(1, j-0.6), min(3, j+0.6)),
                  3 + np.random.uniform(max(1, k-0.6), min(3, k+0.6))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[8]:
    for j in mu2[8]:
        for k in mu3[8]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-0.4), min(3, i+0.4)),
                  3 + np.random.uniform(max(1, j-0.4), min(3, j+0.4)),
                  3 + np.random.uniform(max(1, k-0.4), min(3, k+0.4))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[9]:
    for j in mu2[9]:
        for k in mu3[9]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + np.random.uniform(max(1, i-0.2), min(3, i+0.2)),
                  3 + np.random.uniform(max(1, j-0.2), min(3, j+0.2)),
                  3 + np.random.uniform(max(1, k-0.2), min(3, k+0.2))]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))

L=0
for i in mu1[10]:
    for j in mu2[10]:
        for k in mu3[10]:
            s = Simulation([8,5], np.array([[i,j,k], 
                [3 + i,
                  3 + j,
                  3 + k]]))
            s.run()
            L += s.total_wait / s.t_termination
print(L/len(mu1[0])/len(mu2[0])/len(mu3[0]))