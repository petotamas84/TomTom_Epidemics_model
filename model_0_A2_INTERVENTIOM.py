# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:53:15 2020

@author: Tomi
"""

import matplotlib.pyplot as plt

inf = 300000.0         #starting value of infected people
n_inf = 30000.0         #new infection

d = 0.0             #days
di = 0.0            #incubation time parameter
dd = 0.0
dr = 0.0            #disease time parameter

ill = 9000.0           #number of disease
sum_ill = 0.0       #all disease

death = 686.0         #all deceased
n_death = 0.0       #new deceased

rec_c = 5000.0         #recovered
n_rec_c = 0.0       #newly recovered
imm_c = 0.0         #immunity, i think it should be exist becouse in case of virus if you don't die you become immune

##pop = input("Enter the population: ")
pop = 9654000 #population
pop_k = pop

ri = input("Enter reproduction index: ")
ri = float(ri) #reproduction index

'''
inf = input("Enter the initial number of infection: ")
inf = float(inf) #initial infection

imm_c = input("Enter the initial number of resestant people: ")
imm_c = float(imm_c)
'''

rc = input("Enter the length of reproduction cycle: ")
rc = int(rc) #reproduction cycle

rate_i = input("Enter disease rate: ")
rate_i = float(rate_i) #disease rate

rate_d = input("Enter mortality: ")
rate_d = float(rate_d) #mortality

ACT = input("Enter intervention (Y = apply intevention): ")
ACT = str(ACT)

ACT_TYPE = 0

ACT_POINT_D = pop
ACT_POINT_I = pop

ACT_LENGTH = 1

if (ACT == 'Y'):
    
    ACT_TYPE = input("Enter the type of intervention(1 = number of daily deceased case; 2 = number of sick people): ")
    ACT_TYPE = int(ACT_TYPE)

if(ACT_TYPE == 1):
    
    ACT_POINT_D = input("Enter the number of daily deceased case when you interrupt: ")
    ACT_POINT_D = int(ACT_POINT_D)
    
    ACT_LENGTH = input("Enter the number length of restriction: ")
    ACT_LENGTH = int(ACT_LENGTH)
    
    ACT_STRENGTH = input("Enter the intensity of restriction: ")
    ACT_STRENGTH = float(ACT_STRENGTH)
    

elif(ACT_TYPE == 2):
    
    ACT_POINT_I = input("Enter the number of daily deceased case when you interrupt: ")
    ACT_POINT_I = int(ACT_POINT_I)
    
    ACT_LENGTH = input("Enter the number length of restriction: ")
    ACT_LENGTH = int(ACT_LENGTH)
    
    ACT_STRENGTH = input("Enter the intensity of restriction(between 0 and 1).: ")
    ACT_STRENGTH = float(ACT_STRENGTH)
    
CLI = ACT_LENGTH + 1

d_t = []
di_t = []
dd_t = []
dr_t = []

da_t = []
dai_t = []
dad_t = []
dar_t = []

inf_t = []
n_inf_t = []

ill_t = []
sum_ill_t = []

death_t = []
n_death_t= []

rec_c_t = []
n_rec_c_t = []

filename = "Model_0_A2_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f = open(filename, "w+")

filename_ex_mor = "Model_0_A2_daily_mortality_" + str(ri) + "_" + str(rc) +  "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_mor = open(filename_ex_mor, "w+")

filename_ex_ill = "Mode_0_A2_daily_ill_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_ill = open(filename_ex_ill, "w+")

filename_ex_inf = "Model_0_A2_daily_inf_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" +  str(rate_d) + ".txt"
f_ex_inf = open(filename_ex_inf, "w+")

while(inf < pop and ill >= 2):
    
    if (CLI <= ACT_LENGTH):
        
        ri_e = ri*(1 - inf/pop)*ACT_STRENGTH#ri: reproduction index multiply with a probality to meet someone who are not infected
        CLI = CLI + 1
        
    else:
        ri_e = ri*(1 - inf/pop)
        
    n_inf = n_inf*ri_e  # number of new infection
    n_inf = (n_inf // 1)
        
    if(n_inf < 0):
            
        n_inf = 0 # no negativ new infection
  
    inf = inf + n_inf #all infection         
    ill = n_inf * rate_i    #new disease
    
    if(ill < 0):
        
        ill = 0
    
    if(ill % 2 < (ill / 2)): #egészre kerekítés
            
        ill = ill // 1

    else:
            
        ill = (ill // 1) + 1 #egészre kerekítés vége
        
    if (ill/rc >= ACT_POINT_I):
        
        CLI = 0

    sum_ill = sum_ill + ill    #all disease
    n_death = ill * rate_d     #new deceased
    
    if(n_death < 0):
        
        ill = 0
    
    if(n_death % 2 < (n_death / 2)): #egészre kerekítés
            
        n_death = n_death // 1
            
    else:
            
        n_death = (n_death // 1) + 1 #egészre kerekítés vége
    
    if (n_death/rc >= ACT_POINT_D):
        
        CLI = 0
            
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
    
    #idő faktor
    di = int(d) + 5
    dd = int(di) + 14
    dr = int(di) + 25
    d = int(d) + rc
    
    d_t.append(d)
    di_t.append(di)
    dd_t.append(dd)
    dr_t.append(dr)
    
    for i in range(0, rc):
        
        ill_t.append(int(ill/rc))
        n_death_t.append(int(n_death/rc))
        n_inf_t.append(int(n_inf/rc))
        n_rec_c_t.append(int(n_rec_c/rc))
    
    sum_ill_t.append(sum_ill)
    death_t.append(death)
    inf_t.append(inf)
    rec_c_t.append(rec_c)
    
    
    f.write("%d %.3f   %d %.3f   %d %.3f   %d %.3f\n"  % (d, inf, di, sum_ill, dd, death, dr, rec_c))
    
    for i in range(0, rc):
        
        f_ex_mor.write("%d\n"  % (int(n_death/rc)))
        f_ex_ill.write("%d\n"  % (int(ill/rc)))
        f_ex_inf.write("%d\n"  % (int(n_inf/rc)))
    
for i in range(0, rc*len(d_t)):
    da_t.append(i)
    dai_t.append(i+5)
    dad_t.append(i+19)
    dar_t.append(i+30)

figurename_1 = 'model_0_A2_figure_Total' + '_' + str(ri) + "_" + str(rc) + '_' + str(rate_i) + '_' + str(rate_d) + '.png'
figurename_2 = 'model_0_A2_figure_Daily' + '_' + str(ri) + "_" + str(rc) + '_' + str(rate_i) + '_' + str(rate_d) + '.png'


plt.clf()
plt.figure(1)

plt.subplot(411)
plt.plot(d_t, inf_t, 'bo', markersize = 2)
plt.ylabel("Totlal number of infections", fontsize = 8)
plt.title("Number of infected, patients, deceased and recovered (all)\n(Population = %.0f, R = %.2f, Disease rate = %.2f, Mortality = %.3f)" %(pop_k, ri, rate_i, rate_d), fontsize=14)

plt.subplot(412)
plt.plot(di_t, sum_ill_t, 'yo', markersize = 2)
plt.ylabel("Number of all patients", fontsize = 8)

plt.subplot(413)
plt.plot(dd_t, death_t, 'ro', markersize = 2)
plt.ylabel("Number of all deceased", fontsize = 8)

plt.subplot(414)
plt.plot(dr_t, rec_c_t, 'go', markersize = 2)
plt.ylabel("Number of totaly recovered", fontsize = 8)
plt.xlabel("Days", fontsize = 12)
plt.show()

plt.savefig(figurename_1, dpi = 300)

plt.clf()
plt.figure(2)

plt.subplot(411)
plt.plot(da_t, n_inf_t, 'co', markersize = 2)
plt.ylabel("Number of daily infections", fontsize = 8)
plt.title("Number of infected, patients, deceased and recovered (Daily)\n(Population = %.0f, R = %.2f, Disease rate = %.2f, Mortality = %.3f)" %(pop_k, ri, rate_i, rate_d), fontsize=14)

plt.subplot(412)
plt.plot(dai_t, ill_t, 'mo', markersize = 2)
plt.ylabel("Number of daily new patients", fontsize = 8)

plt.subplot(413)
plt.plot(dad_t, n_death_t, 'ko', markersize = 2)
plt.ylabel("Number of daily deceased", fontsize = 8)

plt.subplot(414)
plt.plot(dar_t, n_rec_c_t, 'go', markersize = 2)
plt.ylabel("Number of newly recovered", fontsize = 8)
plt.xlabel("Days", fontsize = 12)
plt.show()

plt.savefig(figurename_2, dpi = 300)

print('\n')
print("Number of infections = %.0f" % inf)
print("Number of patients = %.0f" % sum_ill)
print("Number of deceased = %.0f" % death)
print("Recovered = %.0f" % rec_c)
print("Expected end of epidemic is the %.0f. day from the zero day (if the parameters are considered constant)." % dr)

f.write("Basic reproduction index = %.3f\nDisease rate = %.3f\nMortality = %.3f\nNumber of infections = %.0f\nNumber of patients = %.0f\nNumber of deceased = %.0f\nRecovered = %.0f\nExpected end of epidemic is the %.0f. day from the zero day (if the parameters are considered constant)." % (ri, rate_i, rate_d, inf, sum_ill, death, rec_c, dr))