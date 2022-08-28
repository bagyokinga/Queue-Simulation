# Queue-Simulation
Simulation and stochastic modelling of different types of queues with some analysis.

## 1 type of customer problem
- M/M/1 queue: a single line served by a single server on a first-come, first-served basis
- n-server queue: a single line served by n servers
- routing methods:
    - index-based: first allocate to server 1, then server 2, etc.
    - random: route to a random server
    - longest idle: allocate next customer to longest idle server
- abandonment/reneging: sometimes customers run out of patience and decide to leave the queue without being served
- analysis:
    - important features: utilization, throughput, average queue length...
    - obtain analytical solutions for the steady state probabilities using Chapman-Kolmogorov equation
    - calculate average queue length from steady state probabilites
    - comparison of average queue length from simulation with analytical solutions
    - observe how average queue length changes with the variance of average service rates ($\mu$-s are uniformly distributed, e.g. $U[1,3]$ or $U[1.9, 2.1]$)

## 2 types of customer problems
- type I and type II customers arriving
- each server is capable of catering for both types of problems
- servers have different mean service rates for type I and type II problems
- routing to a server can be 3 types: index-based, random, longest-idle
- choosing a type of customer to serve next can be
    - first come, first served
    - random
    - choose a customer from the longest queue
- Question: Does the dependence of type I and type II mean service rates affect average queue length?

## Files in the repository:
- MM1 plots: M/M/1 queue
    - step plot of number of customers in the system
    - queue length pmf (i.e. steady state probabilities graph)
    - average queue length vs $\lambda$ / $\mu$
- 3 routing methods with and without abandonment
- average queue length: method to find average queue length for simulation
- analytical solutions: finding average queue length from steady-state probabilities (matrix inversion from Chapman-Kolmogorov)
- 2-type queue: type I and type II customers arriving
    - 1st come, 1st served
    - random
    - choose next customer from longer queue
- correlation-L graphs: find correlation of $\mu_{i1}$ and $\mu_{i2}$, then graph it against average queue length obtained from simulation
    
