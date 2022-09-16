# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:28:50 2022

@author: kinga
"""

import numpy as np
import matplotlib.pyplot as plt

Lambda = np.linspace(1,8,10)

ind_L1_sim = [0.5088815856425593,
0.8854671865108678,
1.2644827871599762,
1.641744330879376,
2.0070574590692134,
2.3710614706081508,
2.7404845929261663,
3.102209296161805,
3.4692476123915093,
3.813076240818679]

ind_L1_an = [0.5288199943386056,
0.9257618805681224,
1.3173723070874295,
1.7059849464344299,
2.092754022266789,
2.4783882391673266,
2.8633915141818393,
3.248140949103637,
3.6329140430807754,
4.017903384317391]

ind_L2_sim = [0.47280453978235315,
0.8486987383441941,
1.2219090300319553,
1.5863334598382195,
1.9594800816919022,
2.320821944673822,
2.6953650953730413,
3.06147632131682,
3.4297078129399794,
3.800265445831318]

ind_L2_an = [0.5288199943386056,
0.9257618805681224,
1.3173723070874295,
1.7059849464344299,
2.092754022266789,
2.4783882391673266,
2.8633915141818393,
3.248140949103637,
3.6329140430807754,
4.017903384317391]


fig, ax = plt.subplots()
ax.plot(Lambda, ind_L1_an, label = "$\mu_i \sim U(1,3)$, analytical sol.", color = 'blue', linestyle = 'dashdot')
ax.plot(Lambda, ind_L2_an, label = "$\mu_i \sim U(1.9, 2.1)$, analytical sol.", color = 'green', linestyle = 'dotted')
ax.plot(Lambda, ind_L1_sim, label = "$\mu_i \sim U(1,3)$, simulation", color = 'red')
ax.plot(Lambda, ind_L2_sim, label = "$\mu_i \sim U(1.9, 2.1)$, simulation", color = 'orange')
ax.legend()
ax.set(xlabel = "$\lambda$", ylabel = "$L_{avg}$")




rand_L1_sim = [0.5121056624183529,
0.8917035541114305,
1.2700344860954984,
1.6419426049348609,
2.008115029644054,
2.3702520481789096,
2.7294260307590728,
3.104531164064295,
3.464229903417974,
3.8186655760128176]

rand_L1_an = [0.6194416736913619,
1.10385546143763,
1.5504563287770035,
1.9619249632599025,
2.3481931415892854,
2.718627974567433,
3.0803634473316626,
3.438373434727244,
3.795925350484352,
4.155034057717869]

rand_L2_sim = [0.4781276937517096,
0.8396180632174198,
1.2160886765447718,
1.5880085554322059,
1.9527694615794744,
2.3224777891379853,
2.6970733740386073,
3.0688259238209374,
3.4335242296076998,
3.8011024821922375]

rand_L2_an = [0.5741378149444272,
1.0415109418464472,
1.483839346937837,
1.8974301683179995,
2.2885028543061616,
2.664678784952428,
3.0323417942379898,
3.3961544940388344,
3.759249413439659,
4.123571705423263]

fig, ax = plt.subplots()
ax.plot(Lambda, rand_L1_an, label = "$\mu_i \sim U(1,3)$, analytical sol.", color = 'blue')
ax.plot(Lambda, rand_L2_an, label = "$\mu_i \sim U(1.9, 2.1)$, analytical sol.", color = 'green')
ax.plot(Lambda, rand_L1_sim, label = "$\mu_i \sim U(1,3)$, simulation", color = 'red')
ax.plot(Lambda, rand_L2_sim, label = "$\mu_i \sim U(1.9, 2.1)$, simulation", color = 'orange')
ax.legend()
ax.set(xlabel = "$\lambda$", ylabel = "$L_{avg}$")





li_L1_sim = [0.509929079976863,
0.8981379010116729,
1.271080163958944,
1.6557584003920751,
2.0203809721002806,
2.3864831096979437,
2.7476909384226094,
3.1107885649940283,
3.4852406841673007,
3.835816934192626]

li_L1_an = [0.5404853247789378,
0.9480038474952007,
1.3463768913215877,
1.7378868163524899,
2.1246904715501187,
2.5085801861975807,
2.890921859722795,
3.2726872153856577,
3.6545225998479425,
4.036824081306956]

li_L2_sim = [0.4718487344812098,
0.8418703085040962,
1.2133070593074486,
1.5803933139466049,
1.9503902905348933,
2.319604214481355,
2.6911340539935202,
3.06149352849046,
3.4326982695732666,
3.7998431685320613]

li_L2_an = [0.5005233078233415,
0.8897213930705359,
1.2788362505349085,
1.6678768806003337,
2.0568564974467534,
2.445789613935208,
2.8346898349449594,
3.2235686339093332,
3.6124349344668345,
4.001295208859916]


fig, ax = plt.subplots()
ax.plot(Lambda, li_L1_an, label = "$\mu_i \sim U(1,3)$, analytical sol.", color = 'blue')
ax.plot(Lambda, li_L2_an, label = "$\mu_i \sim U(1.9, 2.1)$, analytical sol.", color = 'green')
ax.plot(Lambda, li_L1_sim, label = "$\mu_i \sim U(1,3)$, simulation", color = 'red')
ax.plot(Lambda, li_L2_sim, label = "$\mu_i \sim U(1.9, 2.1)$, simulation", color = 'orange')
ax.legend()
ax.set(xlabel = "$\lambda$", ylabel = "$L_{avg}$")



fig, ax = plt.subplots()
ax.plot(Lambda, ind_L1_an, label = 'Index-based')
ax.plot(Lambda, rand_L1_an, label = 'Random')
ax.plot(Lambda, li_L1_an, label = 'Longest Idle Server')
ax.legend()
ax.set(xlabel = "$\lambda$", ylabel = "$L_{avg}$")



fig, ax = plt.subplots()
ax.plot(Lambda, ind_L2_an, label = 'Index-based')
ax.plot(Lambda, rand_L2_an, label = 'Random')
ax.plot(Lambda, li_L2_an, label = 'Longest Idle Server')
ax.legend()
ax.set(xlabel = "$\lambda$", ylabel = "$L_{avg}$")
