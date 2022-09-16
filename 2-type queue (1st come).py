# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:14:17 2022

@author: kinga
"""

# Skillset routing
# Two types of customer problems
# First come, first served

import numpy as np

class Simulation(object):
    def __init__(self, Lambda, Mu):
        # number of servers
        self.n = 3
        
        # Termination time
        self.t_termination = 20
        
        # Mean arrival rate
        self.Lambda = Lambda
        
        # Mean service rates
        self.Mu = Mu
        
        # Mean abandonment rate
        self.Gamma = 2
        
        # Event Calendar: arrival, n service completions, termination time, abandonment times
        self.EC = [0.0]*(self.n+3)
        self.EC[0] = self.generate_interarrival_time(1)
        self.EC[1] = self.generate_interarrival_time(2)
        self.EC[2:-1] = [float('inf')] * self.n
        self.EC[-1] = self.t_termination
        
        # Event Type: arrival, service completion, termination + reneging
        self.event_type = ['A1'] + ['A2'] + ['SC']*self.n + ['T']
            
        # busy or not, total busy time
        self.busy = np.zeros(self.n)
        self.total_busy = 0.0
        self.total_busy_n = np.zeros((self.n, 2))
        
        # current time
        self.t_now = 0.0     
        
        # number of customers in the system
        self.num_in_system = 0

        # total arrivals, departures, waiting time, renegers
        self.total_arrivals = [0, 0]
        self.total_wait = 0.0
        self.total_departs = 0
        self.total_departs_n = np.zeros((self.n, 2))
        self.total_reneging = 0
        
        # queueing before service
        self.total_queue_time = 0.0
        self.num_in_queue = [0,0]
            
    def run(self):
        while True:
            t_event = min(self.EC)
            
            # calculate total time spent in system by customers
            self.total_wait += self.num_in_system * (t_event - self.t_now)
            
            # calculate total time spent in queue by customers
            self.total_queue_time += sum(self.num_in_queue) * (t_event - self.t_now)
    
            if self.num_in_system > 0:
                # total busy time
                self.total_busy += t_event - self.t_now

            for i in range(self.n):
                if self.busy[i] == 1:
                    self.total_busy_n[i][0] += t_event - self.t_now
                elif self.busy[i] == 2:
                    self.total_busy_n[i][1] += t_event - self.t_now
                
            self.t_now = t_event
            
            i = self.EC.index(t_event)
            
            # Arrival
            if self.event_type[i] == 'A1':
                self.handle_arrival1()
            elif self.event_type[i] == 'A2':
                self.handle_arrival2()
            
            # Departure (service completion)
            elif self.event_type[i] == 'SC1':
                self.handle_departure1()
            elif self.event_type[i] == 'SC2':
                self.handle_departure2()
            
            
            # Termination
            elif self.event_type[i] == 'T':
                break
        
            # Reneging
            elif self.event_type[i] == 'R1':
                self.handle_reneging1()
            elif self.event_type[i] == 'R2':
                self.handle_reneging2()
                
            
    def handle_arrival1(self):
        self.num_in_system += 1
        self.total_arrivals[0] += 1
        # print('New type 1 arrival at {}'.format(self.t_now))
        self.EC.append(self.EC[0] + self.generate_abandonment_time())
        self.event_type.append('R1')
        
        free_servers = []
        for i in range(self.n):
            if self.busy[i] == 0:
                free_servers.append(i)
        
        if len(free_servers) != 0:
            ind = min(free_servers)
            self.busy[ind] = 1
            self.EC[ind+2] = self.t_now + self.generate_service_time(ind, 1)
            self.event_type[ind+2] = 'SC1'
            # pop abandonment time as soon as customer is allocated to a server
            self.EC.pop(self.event_type.index('R1'))
            self.event_type.pop(self.event_type.index('R1'))
            # print('Next type 1 allocated to server {}'.format(ind+1))
        
        else:
            self.num_in_queue[0] += 1
            
        self.EC[0] = self.t_now + self.generate_interarrival_time(1)
        
    def handle_arrival2(self):
        self.num_in_system += 1
        self.total_arrivals[1] += 1
        # print('New type 2 arrival at {}'.format(self.t_now))
        self.EC.append(self.EC[1] + self.generate_abandonment_time())
        self.event_type.append('R2')
        
        free_servers = []
        for i in range(self.n):
            if self.busy[i] == 0:
                free_servers.append(i)
        
        if len(free_servers) != 0:
            ind = min(free_servers)
            self.busy[ind] = 2
            self.EC[ind+2] = self.t_now + self.generate_service_time(ind, 2)
            self.event_type[ind+2] = 'SC2'
            # pop abandonment time as soon as customer is allocated to a server
            self.EC.pop(self.event_type.index('R2'))
            self.event_type.pop(self.event_type.index('R2'))
            # print('Next type 2 allocated to server {}'.format(ind+1))
        
        else:
            self.num_in_queue[1] += 1
            
        self.EC[1] = self.t_now + self.generate_interarrival_time(2)

        
    def handle_departure1(self):
        self.num_in_system -= 1
        self.total_departs += 1
        
        ind = self.EC.index(self.t_now) - 2
        
        self.total_departs_n[ind][0] += 1
            
        # print('Depart type 1 from server {} at {}'.format(ind+1, self.t_now))
        
        if self.num_in_queue[0] > 0 or self.num_in_queue[1] > 0 :
            if self.event_type[self.n+3] == 'R1' or self.num_in_queue[1] == 0:
                self.EC[ind+2] = self.t_now + self.generate_service_time(ind, 1)
                self.event_type[ind+2] = 'SC1'
                # pop abandonment time as soon as customer is allocated to a server
                self.EC.pop(self.event_type.index('R1'))
                self.event_type.pop(self.event_type.index('R1'))
                self.num_in_queue[0] -= 1
                # print('Next type 1 allocated to server {}'.format(ind+1))
                
            elif self.event_type[self.n+3] == 'R2' or self.num_in_queue[0] == 0:
                self.EC[ind+2] = self.t_now + self.generate_service_time(ind, 2)
                self.event_type[ind+2] = 'SC2'
                self.busy[ind] = 2
                # pop abandonment time as soon as customer is allocated to a server
                self.EC.pop(self.event_type.index('R2'))
                self.event_type.pop(self.event_type.index('R2'))
                self.num_in_queue[1] -= 1
                # print('Next type 2 allocated to server {}'.format(ind+1))

        else:
            self.EC[ind+2] = float('inf')
            self.event_type[ind+2] = 'SC'
            self.busy[ind] = 0

    def handle_departure2(self):
        self.num_in_system -= 1
        self.total_departs += 1
        
        ind = self.EC.index(self.t_now) - 2
        
        self.total_departs_n[ind][1] += 1
            
        # print('Depart type 2 from server {} at {}'.format(ind+1, self.t_now))
        
        if self.num_in_queue[0] > 0 or self.num_in_queue[1] > 0 :
            if self.event_type[self.n+3] == 'R1' or self.num_in_queue[1] == 0:
                self.EC[ind+2] = self.t_now + self.generate_service_time(ind, 1)
                self.event_type[ind+2] = 'SC1'
                # pop abandonment time as soon as customer is allocated to a server
                self.EC.pop(self.event_type.index('R1'))
                self.event_type.pop(self.event_type.index('R1'))
                self.num_in_queue[0] -= 1
                # print('Next type 1 allocated to server {}'.format(ind+1))
                
            elif self.event_type[self.n+3] == 'R2' or self.num_in_queue[0] == 0:
                self.EC[ind+2] = self.t_now + self.generate_service_time(ind, 2)
                self.event_type[ind+2] = 'SC2'
                self.busy[ind] = 2
                # pop abandonment time as soon as customer is allocated to a server
                self.EC.pop(self.event_type.index('R2'))
                self.event_type.pop(self.event_type.index('R2'))
                self.num_in_queue[1] -= 1
                # print('Next type 2 allocated to server {}'.format(ind+1))

        else:
            self.EC[ind+2] = float('inf')
            self.event_type[ind+2] = 'SC'
            self.busy[ind] = 0

    def handle_reneging1(self):
        self.num_in_system -= 1
        self.total_reneging += 1
        self.num_in_queue[0] -= 1
        
        ind = self.EC.index(self.t_now)
        self.event_type.pop(ind)
        self.EC.pop(ind)
        # print('Reneging no. {} in queue at {}'.format(ind-self.n-2, self.t_now))

    def handle_reneging2(self):
        self.num_in_system -= 1
        self.total_reneging += 1
        self.num_in_queue[1] -= 1
        
        ind = self.EC.index(self.t_now)
        self.event_type.pop(ind)
        self.EC.pop(ind)
        # print('Reneging no. {} in queue at {}'.format(ind-self.n-2, self.t_now))
    
    def generate_interarrival_time(self, ctype):
        return np.random.exponential(1/self.Lambda[ctype-1])
    
    def generate_service_time(self, server, ctype):
        return np.random.exponential(1/self.Mu[ctype-1][server])
    
    def generate_abandonment_time(self):
        return np.random.exponential(1/self.Gamma)
