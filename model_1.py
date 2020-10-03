# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:53:15 2020

@author: Tomi
"""
import numpy as np
import matplotlib.pyplot as plt

pop = 10000000.0    #népesség, esetünkbe magyarország
inf = 1.0           #fertőzöttek induló értéke
n_inf = 0.0         #új fertőzőttek induló értéke
d = 0.0             #napok száma
death = 0.0         #halálesetek száma
ill = 0.0           #betegek száma
imm_c = 0.1         #immmunitással rendelekezők száma, azért feltéeletem, hogy van ilyen mert sokan nem betegszenek meg
rec_c = 0.0         #gyógyultak száma 

r_1 = input("Adja meg megbetegedési arányt: ")
rate_i = float(r_1) #megbetegedési arány
r_2 = input("Adja meg a reprudukciós indexet: ")
ri = float(r_2) #reprodukciós index
r_3 = input("Adja meg a halálozási arányt: ")
rate_d = float(r_3) #halálozási arány


d_t = []
ill_t = []
death_t = []
inf_t = []
n_inf_t = []
rec_c_t = []

while(inf < pop and d < 100 and inf > 0):
    
    ri_e = ri*(1 - inf/pop) #ri: reprodukciós index, megszorzom annak a valószínűséggével, hogy olyan ember adja át aki nem fertözött
    
    if(ri_e > 1):
        
        n_inf = inf*ri_e - inf - imm_c # új fertőzöttek száma
        
        if(n_inf < 0):
            
            n_inf = 0 # hogy ne legyen negatív számú új fertőzött
            
        inf = inf*ri_e - rec_c#összes fertőzött
        d = d + 3.5
        ill = inf*rate_i # betgek száma
        death =ill*rate_d # halotak száma

        
    elif(ri_e < 1):
        
        n_inf = inf*ri_e - inf - imm_c
        
        if(n_inf < 0):
            
            n_inf = 0
            
        inf = inf + n_inf - rec_c
        d = d + 3.5
        ill = inf*rate_i
        death = ill*rate_d
        
 
    rec_c = ill*(1-rate_d) # gyógyultak száma
    imm_c = rec_c*0.9
    
    
    #print(n_inf)     -
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

plt.savefig("Alapmodel_immunitással.png", dpi = 300)


print("\n")
#print(inf/pop)
print(d)
print("Fertőzőtek száma: %f" % inf)
print("Betegek száma: %f" % ill)
print("Elhalálozások száma: %f" % death)
print("Gyógyultak: %f" % rec_c)
