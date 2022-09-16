# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:02:58 2022

@author: kinga
"""

# Routing to longest idle server without abandonment

import numpy as np
import matplotlib.pyplot as plt

class Simulation(object):
    def __init__(self, Lambda):
        # number of servers
        self.n = 3
        
        # Termination time
        self.t_termination = 100
        
        # Mean arrival rate
        self.Lambda = Lambda
        
        # Mean service rates
        self.Mu = 2 * np.random.random(self.n) + 1
        
        # Event Calendar: arrival, n service completions, termination time, patience times
        self.EC = [0.0]*(self.n+2)
        self.EC[0] = self.generate_interarrival_time()
        self.EC[1:-1] = [float('inf')] * self.n
        self.EC[-1] = self.t_termination
        
        # Event Type: arrival, service completion, termination + reneging
        self.event_type = ['A'] + ['SC']*self.n + ['T']
        
        # busy or not, total busy time
        self.busy = np.zeros(self.n)
        self.total_busy = 0.0
        self.total_busy_n = np.zeros(self.n)
        
        # running idle time of each server
        self.idle_time_n = [0] * self.n
        
        # current time
        self.t_now = 0.0     
        
        # number of customers in the system
        self.num_in_system = 0

        # total arrivals, departures, waiting time, renegers
        self.total_arrivals = 0
        self.total_wait = 0.0
        self.total_departs = 0        
        self.total_departs_n = np.zeros(self.n)
        
        # queueing before service
        self.total_queue_time = 0.0
        self.num_in_queue = 0
            
    def run(self):
        while True:
            # print(self.EC)
            t_event = min(self.EC)
            
            # calculate total time spent in system by customers
            self.total_wait += self.num_in_system * (t_event - self.t_now)
            
            # calculate total time spent in queue by customers
            self.total_queue_time += self.num_in_queue * (t_event - self.t_now)
    
            if self.num_in_system > 0:
                # total busy time
                self.total_busy += t_event - self.t_now
                
            for i in range(self.n):
                if self.busy[i] == 1:
                    self.total_busy_n[i] += t_event - self.t_now
                    self.idle_time_n[i] = 0
                else:
                    self.idle_time_n[i] += t_event - self.t_now
                
            self.t_now = t_event
            
            i = self.EC.index(t_event)
            
            # Arrival
            if self.event_type[i] == 'A':
                self.handle_arrival()
            
            # Departure (service completion)
            elif self.event_type[i] == 'SC':
                self.handle_departure()
            
            # Termination
            elif self.event_type[i] == 'T':
                break
            
    def handle_arrival(self):
        self.num_in_system += 1
        self.total_arrivals += 1
        print('New arrival at {}'.format(self.t_now))
        
        free_servers = []
        for i in range(self.n):
            if self.busy[i] == 0:
                free_servers.append(i)
        
        if len(free_servers) != 0:
            ind = self.idle_time_n.index(max(self.idle_time_n))
            self.busy[ind] = 1
            self.EC[ind+1] = self.t_now + self.generate_service_time(ind)
            print('Next in line allocated to server {}'.format(ind+1))
        
        else:
            self.num_in_queue += 1
            
        self.EC[0] = self.t_now + self.generate_interarrival_time()
        
    def handle_departure(self):
        self.num_in_system -= 1
        self.total_departs += 1
        
        ind = self.EC.index(self.t_now) - 1
        
        self.total_departs_n[ind] += 1
        
        if self.busy[ind] == 1 and self.num_in_queue == 0:
            self.busy[ind] = 0
            
        print('Depart from server {} at {}'.format(ind+1, self.t_now))
        
        if self.num_in_queue > 0:
            self.EC[ind+1] = self.t_now + self.generate_service_time(ind)
            self.num_in_queue -= 1
            print('Next in line allocated to server {}'.format(ind+1))

        else:
            self.EC[ind+1] = float('inf')
    
    def generate_interarrival_time(self):
        return np.random.exponential(1/self.Lambda)
    
    def generate_service_time(self, server):
        return np.random.exponential(1/self.Mu[server])

            
s = Simulation(5)
s.run()

# Statistics

avg_system_time = s.total_wait / s.total_arrivals
avg_num_in_system = s.total_wait / s.t_termination
avg_queue_time = s.total_queue_time / s.total_arrivals
avg_num_in_queue = s.total_queue_time / s.t_termination
utilization = s.total_busy / s.t_termination
throughput = s.total_departs / s.t_termination

print("\nTotal number of arrivals:", s.total_arrivals)
print("Total number of departures:", s.total_departs)
for i in range(s.n):
    print("Total number of departures from server {}: {}".format(i+1, 
                                                    int(s.total_departs_n[i])))

print("\nAverage system time:", avg_system_time)
print("Average number of customers in system:", avg_num_in_system)


print("\nAverage queue time:", avg_queue_time)
print("Average number of customers in queue:", avg_num_in_queue)

print("\nUtilization:", utilization)
for i in range(s.n):
    print("Utilization of server {}: {}".format(i+1, s.total_busy_n[i]/
                                                s.t_termination))
print("Throughput:", throughput)

Q_avg = np.zeros(12)
for i in range(1,13):
    s = Simulation(i)
    s.run()
    Q_avg[i-1] = s.total_wait / s.t_termination
    
fig, ax = plt.subplots()
ax.bar(range(1,13), Q_avg)
ax.set_ylabel('Average number of customers in system')
ax.set_xlabel('No. of customers arriving per hour ($\lambda$)')