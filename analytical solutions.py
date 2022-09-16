# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:34:46 2022

@author: kinga
"""

import numpy as np

# Index-based allocation

# 3 server
l = 5

m1 = 2
m2 = 2
m3 = 2

Q = np.array([[-l, m1, 0],
             [l, -(m1+l), m1+m2],
             [0, l, -(m1+m2+l)]])
coeffs = [[0], [0], [-(m1+m2+m3)]]

steady_states = np.matmul(np.linalg.inv(Q), coeffs)
pi3 = 1/(np.sum(steady_states) + 1/(1-(l/(m1+m2+m3))))
steady_states = steady_states * pi3
steady_states = np.append(steady_states, pi3)
for i in range(30):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+m3))
# print(steady_states)


# Random allocation

# 2 server
l = 3
m1 = 2
m2 = 2
p = 0.5

Q = np.array([[-l, m1, m2],
              [p*l, -(m1+l), 0],
              [(1-p)*l, 0, -(m2+l)]])
coeffs = [[0], [-m2], [-m1]]

steady_states = np.matmul(np.linalg.inv(Q), coeffs)
pi2 = 1/(np.sum(steady_states) + 1/(1-(l/(m1+m2))))
steady_states = steady_states * pi2
steady_states = np.append(steady_states, pi2)
for i in range(30):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2))
# print(steady_states)

# 3 server
l = 5

m1 = 2
m2 = 2
m3 = 2

p1 = 1/3
p2 = 1/3
p3 = 1/3

Q = np.array([[-l, m1, m2, m3, 0, 0, 0],
             [p1*l, -(m1+l), 0, 0, m2, m3, 0],
             [p2*l, 0, -(m2+l), 0, m1, 0, m3],
             [p3*l, 0, 0, -(m3+l), 0, m1, m2],
             [0, (p2*l)/(p2+p3), (p1*l)/(p1+p3), 0, -(m1+m2+m3+l), 0, 0],
             [0, (p3*l)/(p2+p3), 0, (p1*l)/(p1+p2), 0, -(m1+m2+m3+l), 0],
             [0, 0, (p3*l)/(p1+p3), (p2*l)/(p1+p2), 0, 0, -(m1+m2+m3+l)]])
coeffs = [[0], [0], [0], [0], [-m3], [-m2], [-m1]]

steady_states = np.matmul(np.linalg.inv(Q), coeffs)
pi3 = 1/(np.sum(steady_states) + 1/(1-(l/(m1+m2+m3))))
steady_states = steady_states * pi3
steady_states = np.append(steady_states, pi3)
for i in range(30):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+m3))
# print(steady_states)


# Longest idle server

# 2 server
l = 3
m1 = 2
m2 = 2

Q = np.array([[-l, 0, 0, m2],
              [0, -l, m1, 0],
              [l, 0, -m1-l, 0],
              [0, l, 0, -m2-l]])
coeffs = [[0], [0], [-m2], [-m1]]

steady_states = np.matmul(np.linalg.inv(Q), coeffs)
pi2 = 1/(np.sum(steady_states) + 1/(1-(l/(m1+m2))))
steady_states = steady_states * pi2
steady_states = np.append(steady_states, pi2)
for i in range(30):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2))
# print(steady_states)

# 3 server
l = 5

m1 = 2
m2 = 2
m3 = 2

p1 = 1/3
p2 = 1/3
p3 = 1/3

Q = np.array([[-l,0,0,0,0,0, 0,0,0,0,m3,0, 0,0,0],
               [0,-l,0,0,0,0, 0,0,m2,0,0,0, 0,0,0],
               [0,0,-l,0,0,0, 0,0,0,0,0,m3, 0,0,0],
               [0,0,0,-l,0,0, m1,0,0,0,0,0, 0,0,0],
               [0,0,0,0,-l,0, 0,0,0,m2,0,0, 0,0,0],
               [0,0,0,0,0,-l, 0,m1,0,0,0,0, 0,0,0],
               
               [l,0,0,0,0,0, -m1-l,0,0,0,0,0, 0,m3,0],
               [0,l,0,0,0,0, 0,-m1-l,0,0,0,0, m2,0,0],
               [0,0,l,0,0,0, 0,0,-m2-l,0,0,0, 0,0,m3],
               [0,0,0,l,0,0, 0,0,0,-m2-l,0,0, m1,0,0],
               [0,0,0,0,l,0, 0,0,0,0,-m3-l,0, 0,0,m2],
               [0,0,0,0,0,l, 0,0,0,0,0,-m3-l, 0,m1,0],
               
               [0,0,0,0,0,0, l,0,l,0,0,0, -m1-m2-l,0,0],
               [0,0,0,0,0,0, 0,l,0,0,l,0, 0,-m1-m3-l,0],
               [0,0,0,0,0,0, 0,0,0,l,0,l, 0,0,-m2-m3-l]])
coeffs = [[0],[0],[0],[0],[0],[0], [0],[0],[0],[0],[0],[0], [-m3],[-m2],[-m1]]

steady_states = np.matmul(np.linalg.inv(Q), coeffs)
pi3 = 1/(np.sum(steady_states) + 1/(1-(l/(m1+m2+m3))))
steady_states = steady_states * pi3
steady_states = np.append(steady_states, pi3)
for i in range(30):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+m3))
# print(steady_states)



# With abandonment

# M/M/1 Queue
l = 5   # 5 customers come every hour
m = 4   # 4 customers are served every hour
g = 2   # 2 customers waiting in line leave every hour

steady_states = np.array([1])
for i in range(30):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m+i*g))

pi0 = 1 / np.sum(steady_states)
steady_states = steady_states * pi0
# print(steady_states)
L = 0
for i in range(len(steady_states)):
    L += i*steady_states[i]
# print(L)


# Index-based 3-server queue
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
    mu3.append(np.random.uniform(m3[i], m3[i+1]))
p = 0.5
g = 2

for l in Lambda:
    L=0
    for m1 in mu1:
        for m2 in mu2:
            for m3 in mu3:

                Q = np.array([[-l, m1, 0],
                             [l, -(m1+l), m1+m2],
                             [0, l, -(m1+m2+l)]])
                coeffs = [[0], [0], [-(m1+m2+m3)]]
                
                steady_states = np.matmul(np.linalg.inv(Q), coeffs)
                for i in range(25):
                    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+m3+i*g))
                
                steady_states = steady_states / np.sum(steady_states)
                # print(steady_states)
                for i in range(len(steady_states)):
                    L += i*steady_states[i]
    # print(L/len(mu1)/len(mu2)/len(mu3))

# Random allocation

# 2 server
Lambda = np.linspace(1,8,10)
m1 = np.linspace(1.9, 2.1, 21)
mu1 = []
for i in range(len(m1)-1):
    mu1.append(np.random.uniform(m1[i], m1[i+1]))
m2 = np.linspace(1.9, 2.1, 21)
mu2 = []
for i in range(len(m2)-1):
    mu2.append(np.random.uniform(m2[i], m2[i+1]))
p = 0.5
g = 2

for l in Lambda:
    L=0
    for m1 in mu1:
        for m2 in mu2:

            Q = np.array([[-l, m1, m2],
                          [p*l, -(m1+l), 0],
                          [(1-p)*l, 0, -(m2+l)]])
            coeffs = [[0], [-m2], [-m1]]
            
            steady_states = np.matmul(np.linalg.inv(Q), coeffs)
            steady_states = np.append(steady_states, 1)
            for i in range(1,25):
                steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+i*g))
            
            steady_states = steady_states / np.sum(steady_states)
            # print(steady_states)
            for i in range(len(steady_states)):
                if i == 0:
                    j = 0
                elif i <= 2:
                    j = 1
                else:
                    j = i-1
                L += j*steady_states[i]
    # print(L/len(mu1)/len(mu2))


# 3 server
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
    
p1 = 1/3
p2 = 1/3
p3 = 1/3

g = 2

for l in Lambda:
    L=0
    for m1 in mu1:
        for m2 in mu2:
            for m3 in mu3:
    
                Q = np.array([[-l, m1, m2, m3, 0, 0, 0],
                             [p1*l, -(m1+l), 0, 0, m2, m3, 0],
                             [p2*l, 0, -(m2+l), 0, m1, 0, m3],
                             [p3*l, 0, 0, -(m3+l), 0, m1, m2],
                             [0, (p2*l)/(p2+p3), (p1*l)/(p1+p3), 0, -(m1+m2+m3+l), 0, 0],
                             [0, (p3*l)/(p2+p3), 0, (p1*l)/(p1+p2), 0, -(m1+m2+m3+l), 0],
                             [0, 0, (p3*l)/(p1+p3), (p2*l)/(p1+p2), 0, 0, -(m1+m2+m3+l)]])
                coeffs = [[0], [0], [0], [0], [-m3], [-m2], [-m1]]
                
                steady_states = np.matmul(np.linalg.inv(Q), coeffs)
                steady_states = np.append(steady_states, 1)
                for i in range(1,25):
                    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+m3+i*g))
                steady_states = steady_states / np.sum(steady_states)
                # print(steady_states)
                for i in range(len(steady_states)):
                    if i == 0:
                        j = 0
                    elif i <=3:
                        j = 1
                    elif i <= 6:
                        j = 2
                    else:
                        j = i-4
                    L += j*steady_states[i]
    # print(L/len(mu1)/len(mu2)/len(mu3))

# Longest idle server

# 2 server
l = 5
m1 = 2
m2 = 2
g = 2

Q = np.array([[-l, 0, 0, m2],
              [0, -l, m1, 0],
              [l, 0, -m1-l, 0],
              [0, l, 0, -m2-l]])
coeffs = [[0], [0], [-m2], [-m1]]

steady_states = np.matmul(np.linalg.inv(Q), coeffs)
steady_states = np.append(steady_states, 1)
for i in range(1,25):
    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+i*g))
steady_states = steady_states / np.sum(steady_states)
# print(steady_states)
L = 0
for i in range(len(steady_states)):
    if i <= 1:
        j = 0
    elif i <= 3:
        j = 1
    else:
        j = i-2
    L += j*steady_states[i]
# print(L)


# 3 server
Lambda = np.linspace(1,8,10)
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

g = 2

for l in Lambda:
    L=0
    for m1 in mu1:
        for m2 in mu2:
            for m3 in mu3:

                Q = np.array([[-l,0,0,0,0,0, 0,0,0,0,m3,0, 0,0,0],
                               [0,-l,0,0,0,0, 0,0,m2,0,0,0, 0,0,0],
                               [0,0,-l,0,0,0, 0,0,0,0,0,m3, 0,0,0],
                               [0,0,0,-l,0,0, m1,0,0,0,0,0, 0,0,0],
                               [0,0,0,0,-l,0, 0,0,0,m2,0,0, 0,0,0],
                               [0,0,0,0,0,-l, 0,m1,0,0,0,0, 0,0,0],
                               
                               [l,0,0,0,0,0, -m1-l,0,0,0,0,0, 0,m3,0],
                               [0,l,0,0,0,0, 0,-m1-l,0,0,0,0, m2,0,0],
                               [0,0,l,0,0,0, 0,0,-m2-l,0,0,0, 0,0,m3],
                               [0,0,0,l,0,0, 0,0,0,-m2-l,0,0, m1,0,0],
                               [0,0,0,0,l,0, 0,0,0,0,-m3-l,0, 0,0,m2],
                               [0,0,0,0,0,l, 0,0,0,0,0,-m3-l, 0,m1,0],
                               
                               [0,0,0,0,0,0, l,0,l,0,0,0, -m1-m2-l,0,0],
                               [0,0,0,0,0,0, 0,l,0,0,l,0, 0,-m1-m3-l,0],
                               [0,0,0,0,0,0, 0,0,0,l,0,l, 0,0,-m2-m3-l]])
                coeffs = [[0],[0],[0],[0],[0],[0], [0],[0],[0],[0],[0],[0], [-m3],[-m2],[-m1]]
                
                steady_states = np.matmul(np.linalg.inv(Q), coeffs)
                steady_states = np.append(steady_states, 1)
                for i in range(1,25):
                    steady_states = np.append(steady_states, steady_states[-1]*l/(m1+m2+m3+i*g))
                steady_states = steady_states / np.sum(steady_states)
                # print(steady_states)
                for i in range(len(steady_states)):
                    if i <= 5:
                        j = 0
                    elif i <= 11:
                        j = 1
                    elif i <= 14:
                        j = 2
                    else:
                        j = i-12
                    L += j*steady_states[i]
    print(L/len(mu1)/len(mu2)/len(mu3))
