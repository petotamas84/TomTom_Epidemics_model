# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:53:15 2020

@author: Tomi
"""

import matplotlib.pyplot as plt

inf = 33000.0         #starting value of infected people
n_inf = 0.0         #new infection

d = 0.0             #days
di = 0.0            #incubation time parameter
dd = 0.0
dr = 0.0            #disease time parameter

ill = 3960.0           #number of disease
sum_ill = 0.0       #all disease

death = 812.0         #all deceased
n_death = 0.0       #new deceased

rec_c = 10000.0         #recovered
n_rec_c = 0.0       #newly recovered
imm_c = 0.0         #immunity, i think it should be exist becouse in case of virus you don't die you become immune

#pop = input("Enter the population: ")
pop = 9654000 #population

ri = input("Enter reproduction index: ")
ri = float(ri) #reproduction index

rate_i = input("Enter disease rate: ")
rate_i = float(rate_i) #disease rate

rate_d = input("Enter mortality: ")
rate_d = float(rate_d) #marality

d_t = []
di_t = []
dd_t = []
dr_t = []

inf_t = []
n_inf_t = []

ill_t = []
sum_ill_t = []

death_t = []
n_death_t= []

rec_c_t = []
n_rec_c_t = []

pop_k = pop

filename = "2020_october3_covid_hu" + str(ri) + ".txt"
f = open(filename, "w+")

while(inf < pop and ill >= 2):
    
    ri_e = ri*(1 - inf/pop) #ri: reproduction index multiply with a probality to meet someone who are not infected

    if(ri_e > 1):
        
        n_inf = inf*(ri_e - 1)  # number of new infection
        n_inf = (n_inf // 1)
        
        if(n_inf < 0):
            
            n_inf = 0 # no negativ new infection
        
    elif(ri_e < 1):
            
        n_inf = inf*(1 - ri_e)
        n_inf = (n_inf // 1)
        
        if(n_inf < 0):
            
            n_inf = 0 # no negativ infection
        
    inf = inf + n_inf #all infection         
    ill = n_inf * rate_i    #new disease
    
    if(ill < 0):
        
        ill = 0
    
    if(ill % 2 < (ill / 2)): #egészre kerekítés
            
        ill = ill // 1
            

    else:
            
        ill = (ill // 1) + 1 #egészre kerekítés vége

    sum_ill = sum_ill + ill    #all disease
    n_death = ill * rate_d     #new deceased
    
    if(n_death % 2 < (n_death / 2)): #egészre kerekítés
            
        n_death = n_death // 1
            
    else:
            
        n_death = (n_death // 1) + 1 #egészre kerekítés vége
            
    n_rec_c = ill * (1 - rate_d)
    
    if(n_rec_c % 2 < (n_rec_c / 2)): #egészre kerekítés
            
        n_rec_c = n_rec_c // 1
            
    else:
            
        n_rec_c = (n_rec_c // 1) + 1 #egészre kerekítés vége
    
    death = death + n_death #elhunytak, gyógyultak, immunitással rendelektők száma
    rec_c = rec_c + n_rec_c
    imm_c = rec_c * 0.9
    
    if(imm_c % 1 < (imm_c / 2)): #egészre kerekítés
            
        imm_c = imm_c // 1
            
    else:
            
        imm_c = (imm_c // 1) + 1 #egészre kerekítés vége
    
    pop = pop - n_death #populáció csökkennás
    
    d = int(d) + 2  #idő faktor
    di = int(d) + 5
    dd = int(di) + 14
    dr = int(di) + 25
    
    d_t.append(d)
    di_t.append(di)
    dd_t.append(dd)
    dr_t.append(dr)
    
    ill_t.append(ill)
    sum_ill_t.append(sum_ill)
    
    death_t.append(death)
    n_death_t.append(n_death)
    
    inf_t.append(inf)
    n_inf_t.append(n_inf)
    
    rec_c_t.append(rec_c)
    n_rec_c_t.append(n_rec_c)

figurename = '0b_model_2020_october3initial_hungary_figure' + '_' + str(ri) + '_' + str(rate_i) + '_' + str(rate_d) + '.png'

plt.clf()
plt.figure(1)

plt.subplot(411)
plt.plot(d_t, inf_t, 'bo', markersize = 2)
plt.plot(d_t, n_inf_t, 'co', markersize = 2)
plt.ylabel("Number of infections", fontsize = 8)
plt.title("Number of infected, patients, deceased and recovered (Daily and all)\n(Population = %.0f, R = %.2f, Disease rate = %.2f, Mortality = %.3f)" %(pop_k, ri, rate_i, rate_d), fontsize=14)

plt.subplot(412)
plt.plot(di_t, ill_t, 'mo', markersize = 2)
plt.plot(di_t, sum_ill_t, 'yo', markersize = 2)
plt.ylabel("Number of patients", fontsize = 8)

plt.subplot(413)
plt.plot(dd_t, n_death_t, 'ko', markersize = 2)
plt.plot(dd_t, death_t, 'ro', markersize = 2)
plt.ylabel("Number of deceased", fontsize = 8)

plt.subplot(414)
plt.plot(dr_t, n_rec_c_t, 'bo', markersize = 2)
plt.plot(dr_t, rec_c_t, 'go', markersize = 2)
plt.ylabel("Number of recovered", fontsize = 8)
plt.xlabel("Days", fontsize = 12)
plt.show()

plt.savefig(figurename, dpi = 300)

print('\n')
print("Number of infections = %.0f" % inf)
print("Number of patients = %.0f" % sum_ill)
print("Number of deceased = %.0f" % death)
print("Recovered = %.0f" % rec_c)
print("Expected end of epidemic is the %.0f. day from the zero day (if the parameters are considered constant)" % dr)

f.write("Basic reproduction index = %.3f\nDisease rate = %.3f\nMortality = %.3f\nNumber of infections = %.0f\nNumber of patients = %.0f\nNumber of deceased = %.0f\nRecovered = %.0f\nExpected end of epidemic is the %.0f. day from the zero day (if the parameters are considered constant)." % (ri, rate_i, rate_d, inf, sum_ill, death, rec_c, dr))