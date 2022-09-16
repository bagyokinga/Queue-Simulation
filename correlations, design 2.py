# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:46:05 2022

@author: kinga
"""

# Design 2 - full range of correlaitons

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from sympy.solvers import solve
from sympy import Symbol
from scipy.stats import pearsonr
x = Symbol('x')


# Create boundaries

# Establishing bounds for sampling from uniformly distributed region
# i.e. splitting up region into 20 equal subregions, setting x values for each

# Create array to store splitting points
bounds = np.zeros((9,21))
for i in range(9):
    bounds[i][0] = 1
    bounds[i][10] = 2
    
# 0.2
bounds[0][1] = 1 + solve((1.8*x + 0.5*x**2)-99/500, x)[1]
for i in range(8):
    bounds[0][9-i] = bounds[0][10]-0.099*(i+1)
    
# 0.4
for i in range(1,4):
    bounds[1][i] = 1 + solve((1.6*x + 0.5*x**2)-96/500*(i), x)[1]
for i in range(6):
    bounds[1][9-i] = bounds[1][10]-0.096*(i+1)

# 0.6
for i in range(1,6):
    bounds[2][i] = 1 + solve((1.4*x + 0.5*x**2)-91/500*(i), x)[1]
for i in range(4):
    bounds[2][9-i] = bounds[2][10]-0.091*(i+1)

# 0.8
for i in range(1,8):
    bounds[3][i] = 1 + solve((1.2*x + 0.5*x**2)-84/500*(i), x)[1]
for i in range(2):
    bounds[3][9-i] = bounds[3][10]-0.084*(i+1)

# 1
for i in range(1,10): 
    bounds[4][i] = 1 + solve((1*x + 0.5*x**2)-75/500*(i), x)[1]

# 1.2
for i in range(1,8):
    bounds[5][i] = 1 + solve((0.8*x + 0.5*x**2)-64/500*(i), x)[1]
for i in range(2):
    bounds[5][9-i] = bounds[5][10]-0.08*(i+1)

# 1.4
for i in range(1,6):
    bounds[6][i] = 1 + solve((0.6*x + 0.5*x**2)-51/500*(i), x)[1]
for i in range(4):
    bounds[6][9-i] = bounds[6][10]-0.085*(i+1)
  
# 1.6
for i in range(1,4):
    bounds[7][i] = 1 + solve((0.4*x + 0.5*x**2)-36/500*(i), x)[1]
for i in range(6):
    bounds[7][9-i] = bounds[7][10]-0.09*(i+1)
 
# 1.8
bounds[8][1] = 1 + solve((0.2*x + 0.5*x**2)-19/500, x)[1]
for i in range(8):
    bounds[8][9-i] = bounds[8][10]-0.095*(i+1)

# second half of each
for j in range(9):
    for i in range(10):
        bounds[j][-(i+1)] = 4 - bounds[j][i]

bounds = np.append(np.linspace(1,3,21), bounds)
bounds = np.append(bounds, np.linspace(1,3,21))
bounds = np.reshape(bounds, (11,21))



# Estimate correlations by averaging (using pearsonr)

mu1 = np.zeros((11,20))
for i in range(11):
    for j in range(20):
        mu1[i][j] = np.random.uniform(bounds[i][j], bounds[i][j+1])

corr = np.zeros(11)

for i in range(100):
    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(1,3))
    corr[0]+=pearsonr(mu1[0],mu2)[0]
    
    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[1][j]-1.8), min(3, mu1[1][j]+1.8)))
    corr[1]+=pearsonr(mu1[1],mu2)[0]
    
    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[2][j]-1.6), min(3, mu1[2][j]+1.6)))
    corr[2]+=pearsonr(mu1[2],mu2)[0]
    
    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[3][j]-1.4), min(3, mu1[3][j]+1.4)))
    corr[3]+=pearsonr(mu1[3],mu2)[0]

    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[4][j]-1.2), min(3, mu1[4][j]+1.2)))
    corr[4]+=pearsonr(mu1[4],mu2)[0]
    
    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[5][j]-1), min(3, mu1[5][j]+1)))
    corr[5]+=pearsonr(mu1[5],mu2)[0]
    
    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[6][j]-0.8), min(3, mu1[6][j]+0.8)))
    corr[6]+=pearsonr(mu1[6],mu2)[0]

    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[7][j]-0.6), min(3, mu1[7][j]+0.6)))
    corr[7]+=pearsonr(mu1[7],mu2)[0]

    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[8][j]-0.4), min(3, mu1[8][j]+0.4)))
    corr[8]+=pearsonr(mu1[8],mu2)[0]

    mu2 = []
    for j in range(20):
        mu2.append(3 + np.random.uniform(max(1, mu1[9][j]-0.2), min(3, mu1[9][j]+0.2)))
    corr[9]+=pearsonr(mu1[9],mu2)[0]

    mu2 = []
    for j in range(20):
        mu2.append(3 + mu1[10][j])
    corr[10] += pearsonr(mu1[10],mu2)[0]

r_est = corr / 100


# Calculate true correlations

limits = [[1.2, 2.8], [1.4, 2.6], [1.6, 2.4], [1.8, 2.2], [2,2], 
          [1.8, 2.2], [1.6, 2.4], [1.4, 2.6], [1.2, 2.8]]

areas = [19/25, 36/25, 51/25, 64/25, 75/25, 84/25, 91/25, 96/25, 99/25]

areas = areas[::-1]

def f1(x, a):
    return x/2 * ((x+a)**2 - 4**2)

def f2(x):
    return x/2 * (6**2 - 4**2)

def f3(x, a, b):
    return x/2 * ((x+a)**2 - (x+b)**2)

def f4(x, b):
    return x/2 * (6**2 - (x+b)**2)

xy_exp = []
for i in range(5):
    a = 4.8 - 0.2*i
    b = 1.2 + 0.2*i
    c = limits[i][0]
    d = limits[i][1]
    xy_exp.append((quad(f1, 1, c, args=(a))[0] +
          quad(f2, c, d)[0] +
          quad(f4, d, 3, args=(b))[0]) / areas[i])

for i in range(5,9):
    a = 4.8 - 0.2*i
    b = 1.2 + 0.2*i
    c = limits[i][0]
    d = limits[i][1]
    xy_exp.append((quad(f1, 1, c, args=(a))[0] +
          quad(f3, c, d, args=(a,b))[0] +
          quad(f4, d, 3, args=(b))[0]) / areas[i])

x2_exp = []

def f1(x, m, c1):
    return x**2 * (m*x+c1)

def f2(x, h):
    return x**2 * h

def f3(x, m, c2):
    return x**2 * (-m*x+c2)

for i in range(9):
    b = 5/(11+i)
    m = 1/areas[i]
    c1 = b - m
    c2 = b + 3*m
    if i <= 4:
        h = 2/areas[i]
    else:
        h = (2-0.4*(i-4))/areas[i]
    x2_exp.append((quad(f1, 1, limits[i][0], args=(m, c1))[0] +
          quad(f2, limits[i][0], limits[i][1], args=(h))[0] +
          quad(f3, limits[i][1], 3, args=(m, c2))[0]))

corr = []
for i in range(9):
    corr.append((xy_exp[i]-10)/(x2_exp[i]-4))

r_true = [0] + corr + [1]
    

# Plot

L_1stcome1 = [5.570802081269591,
5.5618862734237995,
5.554796020662318,
5.556904475245721,
5.5477117960402484,
5.551785478784425,
5.546299721320905,
5.536052656860399,
5.527575023286637,
5.53682691981708,
5.52835798954761]

L_1stcome2 = [5.571255820185921,
5.572551103868044,
5.566981877015151,
5.56239144868511,
5.55174354804697,
5.5490735917353105,
5.551737816829429,
5.540685702624527,
5.539717018574881,
5.526150029379062,
5.530372819659645]

L_1stcome3 = [5.567905529048911,
5.5711644545913055,
5.553103994519754,
5.553157098813087,
5.565945743637032,
5.552180480138752,
5.538557782671969,
5.5334196492507886,
5.530594319841053,
5.529548801146764,
5.540807092750636]

L_random1 = [5.529149550307968,
5.528448487875041,
5.533395397138069,
5.527105505790852,
5.5166265125110785,
5.502594396042298,
5.507988948802742,
5.507108647343118,
5.503297265469909,
5.490721797574482,
5.508364589095156]

L_random2 = [5.540579545048049,
5.530278067566261,
5.536109562369013,
5.52368350635017,
5.518481249326667,
5.513777792082292,
5.504382058474623,
5.503811266375553,
5.4973146307536656,
5.494586950822452,
5.504875331639392]

L_random3 = [5.542845925018179,
5.528879402076191,
5.524957926255949,
5.518241170279135,
5.509117147269552,
5.507595874778315,
5.50844607631868,
5.502302747169215,
5.492703369390135,
5.506825279664111,
5.503073412661925]

L_longerq1 = [5.679445743949742,
5.678505119881104,
5.677772582741618,
5.6706461494647025,
5.6639650299606545,
5.661683069952458,
5.6476744997098765,
5.648529515970607,
5.647319189744552,
5.647349710852653,
5.649823636937901]

L_longerq2 = [5.677779596790638,
5.672434695548519,
5.654082595550737,
5.666756953268158,
5.666116749555178,
5.665755259880071,
5.6632878490172605,
5.661450997874956,
5.650684385891238,
5.6436050574233985,
5.644547744450213]

L_longerq3 = [5.6718674429610605,
5.682728212012254,
5.6792366673161805,
5.6812708154333755,
5.662672826090898,
5.66767082789611,
5.647887106078899,
5.650186623805147,
5.648510420589,
5.646472229771753,
5.641464952325935]

L_1stcome = []
L_random = []
L_longerq = []

for i in range(11):
    L_1stcome.append((L_1stcome1[i] + L_1stcome2[i] + L_1stcome3[i])/3)
    L_random.append((L_random1[i] + L_random2[i] + L_random3[i])/3)
    L_longerq.append((L_longerq1[i] + L_longerq2[i] + L_longerq3[i])/3)
    
    
fig, ax = plt.subplots()
ax.plot(r_true, L_1stcome, marker = 'o', label = '1st come, 1st served')
ax.plot(r_true, L_random, marker = 'o', label = 'Random choice of next customer type')
ax.plot(r_true, L_longerq, marker = 'o', label = 'Serve next customer from longer queue')
ax.legend()
ax.set(xlabel = r'Correlation between $\mu_{i1}$ and $\mu_{i2}$', ylabel = r'$L_{avg}$')
    