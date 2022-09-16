# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 00:42:31 2022

@author: kinga
"""

# Random routing (note that code could be largely simplified if no initial 
# server probabilities are given, just assuming each of them is always equally
# likely)

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
        
        # Mean abandonment time
        self.Gamma = 2
        
        # Probabilities of being allocated to each server (equal probabs)
        self.server_probab = np.zeros(self.n)
        for i in range(self.n):
            self.server_probab[i] = 1/self.n
        
        # Event Calendar: arrival, n service completions, termination time, abandonment times
        self.EC = [0.0]*(self.n+3)
        self.EC[0] = self.generate_interarrival_time()
        self.EC[1:-2] = [float('inf')] * self.n
        self.EC[-2] = self.t_termination
        self.EC[-1] = self.EC[0] + self.generate_abandonment_time()
        
        # Event Type: arrival, service completion, termination + reneging
        self.event_type = ['A'] + ['SC']*self.n + ['T'] + ['R']
        
        # busy or not, total busy time
        self.busy = np.zeros(self.n)
        self.total_busy = 0.0
        self.total_busy_n = np.zeros(self.n)
        
        # current time
        self.t_now = 0.0     
        
        # number of customers in the system
        self.num_in_system = 0

        # total arrivals, departures, waiting time, renegers
        self.total_arrivals = 0
        self.total_wait = 0.0
        self.total_departs = 0        
        self.total_departs_n = np.zeros(self.n)
        self.total_reneging = 0
        
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
        
            # Reneging
            elif self.event_type[i] == 'R':
                self.handle_reneging()
            
    def handle_arrival(self):
        self.num_in_system += 1
        self.total_arrivals += 1
        print('New arrival at {}'.format(self.t_now))
        
        free_servers = []
        for i in range(self.n):
            if self.busy[i] == 0:
                free_servers.append(i)
        
        if len(free_servers) != 0:
            ind = self.choose_random_server(free_servers)
            self.busy[ind] = 1
            self.EC[ind+1] = self.t_now + self.generate_service_time(ind)
            # pop abandonment time as soon as customer is allocated to a server
            self.event_type.pop(self.n+2)
            self.EC.pop(self.n+2)
            print('Next in line allocated to server {}'.format(ind+1))
        
        else:
            self.num_in_queue += 1
            
        self.EC[0] = self.t_now + self.generate_interarrival_time()
        self.EC.append(self.EC[0] + self.generate_abandonment_time())
        self.event_type.append('R')
        
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
            # pop abandonment time as soon as customer is allocated to a server
            self.event_type.pop(self.n+2)
            self.EC.pop(self.n+2)
            self.num_in_queue -= 1
            print('Next in line allocated to server {}'.format(ind+1))

        else:
            self.EC[ind+1] = float('inf')
    
    def handle_reneging(self):
        self.num_in_system -= 1
        self.total_reneging += 1
        self.num_in_queue -= 1
        
        ind = self.EC.index(self.t_now)
        self.event_type.pop(ind)
        self.EC.pop(ind)
        print('Reneging no. {} in queue at {}'.format(ind-self.n-1, self.t_now))
    
    def generate_interarrival_time(self):
        return np.random.exponential(1/self.Lambda)
    
    def generate_service_time(self, server):
        return np.random.exponential(1/self.Mu[server])
    
    def generate_abandonment_time(self):
        return np.random.exponential(1/self.Gamma)
    
    def choose_random_server(self, free_servers):
        # rescaling probabilities based on number of free servers
        total_probab = 0
        for i in free_servers:
            total_probab += self.server_probab[i]
        server_probabs = self.server_probab / total_probab
        
        p = []
        for i in free_servers:
            p.append(server_probabs[i])
            
        # turn probabilities into interval boundaries
        boundaries = np.zeros(len(p)+1)
        for i in range(len(p)):
            boundaries[i+1] = boundaries[i] + p[i]
        
        # Check which interval the random number generated falls into
        # to determine number of server chosen
        random_nr = np.random.random()
        for i in range(1, len(p)+1):
            if random_nr < boundaries[i] and random_nr > boundaries[i-1]:
                    return free_servers[i-1]
        
        
            
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
print("Total number of impatient leaves:", s.total_reneging)

print("\nAverage system time:", avg_system_time)
print("Average number of customers in system:", avg_num_in_system)


print("\nAverage queue time:", avg_queue_time)
print("Average number of customers in queue:", avg_num_in_queue)

print("\nUtilization:", utilization)
for i in range(s.n):
    print("Utilization of server {}: {}".format(i+1, s.total_busy_n[i]/
                                                s.t_termination))
print("Throughput:", throughput)


# u = []
# for i in range(10):
#     s = Simulation(5)
#     s.run()
#     u.append(s.total_busy / s.t_termination)
# print(sum(u)/len(u))

# Q_avg = np.zeros(12)
# for i in range(1,13):
#     s = Simulation(i)
#     s.run()
#     Q_avg[i-1] = s.total_wait / s.t_termination
    
# fig, ax = plt.subplots()
# ax.bar(range(1,13), Q_avg)
# ax.set_ylabel('Average number of customers in system')
# ax.set_xlabel('No. of customers arriving per hour ($\lambda$)')
# ax.set_title(r'Random, 3-server with abandonment ($\bar \mu_i$ = 2, $\gamma$ = 2)')