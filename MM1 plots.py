# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 16:35:25 2022

@author: kinga
"""

# with storing previous values of Event Calendar and step plot

import numpy as np
import matplotlib.pyplot as plt

class Simulation(object):
    def __init__(self, Lambda):
        self.Lambda = Lambda
        
        self.A = 0
        self.T = 200
        self.S = self.T + 1
        
        self.EC = [[self.A], [self.S]]
        
        self.Q = [0]
        self.B = 0
        
        self.t_now = 0.0
        
        self.total_arrivals = 0
        self.total_departs = 0
        self.total_wait = 0.0
        self.total_busy = 0.0
        
    def run(self):
        while self.t_now < self.T:
            self.jump()
            
    def jump(self):
        t_event = min(self.EC[0][-1], self.EC[1][-1])
        
        self.total_wait += self.Q[-1] * (t_event - self.t_now)
        if self.Q[-1] > 0:
            self.total_busy += t_event - self.t_now
            
        self.t_now = t_event

        if t_event == self.EC[0][-1]:
            self.Q.append(self.Q[-1] + 1)
            self.total_arrivals += 1
            if self.B == 0:
                self.B = 1
            
            if self.Q[-1] <= 1:
                self.EC[1].append(self.t_now + np.random.exponential(1/6))
            
            self.EC[0].append(self.t_now + np.random.exponential(1/self.Lambda))
                
        else:
            self.Q.append(self.Q[-1] - 1)
            self.total_departs += 1
            if self.B == 1 and self.Q == 0:
                self.B = 0
                
            if self.Q[-1] > 0:
                self.EC[1].append(self.t_now + np.random.exponential(1/6))
            else:
                self.EC[1].append(self.T + 1)
            
s = Simulation(5)
s.run()

# Step plot
times = s.EC[0] + s.EC[1]
times.sort()

fig, ax = plt.subplots()
ax.step(times[0:len(s.Q)], s.Q, where='post')
ax.set_xlim(0,s.T)
ax.set_xlabel('Time (hours)')
ax.set_ylabel('Number of customers')

# Queue length pmf (aka steady states)
intervals = np.array(times[1:])-np.array(times[:-1])
intervals = intervals[:len(s.Q)]

total_state_times = [0] * (max(s.Q)+1)
for i in range(len(s.Q)):
    total_state_times[s.Q[i]] += intervals[i]

fig, ax = plt.subplots()
ax.bar(range(max(s.Q)+1), np.array(total_state_times)/s.T)
ax.set_xlabel('Queue length')
ax.set_ylabel('probability mass function')

# Average queue length against lambda/mu (mu=6)
Q_avg = []
lambdas = np.linspace(0,6,50)
for i in lambdas:
    s = Simulation(i)
    s.run()
    times = s.EC[0] + s.EC[1]
    times.sort()
    intervals = np.array(times[1:])-np.array(times[:-1])
    intervals = intervals[:len(s.Q)]
    Q_avg.append(np.dot(intervals, np.array(s.Q)) / s.T)
    
fig, ax = plt.subplots()
ax.plot(np.linspace(0, 1, 50), Q_avg, label = 'Simulation')
x = np.linspace(0,1,50)
ax.plot(x, x/(1-x), label = "Analytical expectation")
ax.set_ylabel('L', rotation = 0)
ax.set_xlabel('$\lambda$ / $\mu$')
ax.legend()
