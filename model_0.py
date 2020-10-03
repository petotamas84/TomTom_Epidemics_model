# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:53:15 2020

@author: Tomi
"""
import numpy as np
import matplotlib.pyplot as plt

pop = 10000000.0
inf = 1.0
n_inf = 0.0
d = 1.0
death = 0.0
ill = 0.0
rec_c = 0.0

r_1 = input("Adja meg megbetegedési arányt: ")
rate_i = float(r_1)
r_2 = input("Adja meg a reprudukciós indexet: ")
ri = float(r_2)
r_3 = input("Adja meg a halálozási arányt: ")
rate_d = float(r_3)

d_t = []
ill_t = []
death_t = []
inf_t = []
n_inf_t = []
rec_c_t = []


while(inf < pop and d < 200):
    
    ri_e = ri*(1 - inf/pop)
    
    if(ri_e > 1):
        
        n_inf = inf*ri_e - inf
        inf = inf*ri_e - rec_c
        d = d + 3.5
        ill = inf*rate_i
        rec_c = ill*(1-rate_d)
        death = ill*rate_d
        
    elif(ri_e < 1):
        
        n_inf = inf - inf*ri_e
        inf = inf*ri_e - rec_c
        d = d + 3.5
        ill = inf*rate_i
        rec_c = ill*(1-rate_d)
        death = ill*rate_d
        
    
    #print(n_inf)    
    d_t.append(d)
    ill_t.append(ill)
    death_t.append(death)
    inf_t.append(inf)
    n_inf_t.append(n_inf)
    rec_c_t.append(rec_c)
    #print(inf/pop)

plt.clf()
plt.figure(1)

plt.subplot(511)
plt.plot(d_t, inf_t, 'o-')
plt.title("Ferőzöttek száma", fontsize=8) 

plt.subplot(512)
plt.plot(d_t, n_inf_t, 'b-')
plt.title("Új fertőzöttek száma", fontsize=8)       
      
plt.subplot(513)
plt.plot(d_t, ill_t, 'y-')
plt.title("Betegek száma", fontsize=8) 
 
plt.subplot(514)
plt.plot(d_t, death_t, 'r-')
plt.title("Halotak száma", fontsize=8)

plt.subplot(515)
plt.plot(d_t, rec_c_t, 'g-')
plt.title("Gyógyultak száma", fontsize=8)

plt.savefig("Alapmodel.png", dpi = 300)

  

print("\n")
#print(inf/pop)
print(d)
print("Fertőzőtek száma: %f" % inf)
print("Betegek száma: %f" % ill)
print("Elhalálozások száma: %f" % death)
print("Gyógyultak: %f" % rec_c)