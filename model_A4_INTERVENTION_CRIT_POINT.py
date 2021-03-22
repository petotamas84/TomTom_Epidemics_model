# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:53:15 2020

@author: Tomi
"""

#import tkinter
import matplotlib.pyplot as plt
import scipy.optimize as sciopt
import numpy as np

def Gauss(x_value, eltolás, magasság, centrum, stan_dev):
    
    eltolás = np.ones(len(x_value)) * eltolás
    y_value= eltolás + magasság * np.exp( -1 * (x_value-np.ones(len(x_value)) * centrum) ** 2 / (2 * stan_dev ** 2))
    
    return y_value 

d = 0.0             #days
di = 0.0            #incubation time parameter
dho = 0.0           #incubation time parameter
dd = 0.0
dr = 0.0            

#pop = input("Enter the population: ")
pop = 9654000 #population
pop_k = pop

ri = input("Enter reproduction index: ")
ri = float(ri) #reproduction index
'''
inf = input("Enter the initial number of infection: ")
inf = float(inf) #initial infection

n_inf = input("Enter the initial number of new infection: ")
n_inf = float(n_inf) #initial infection

ill_c = input("Enter the initial number of resestant people: ")
ill_c = float(ill_c)

imm_c = input("Enter the initial number of resestant people: ")
imm_c = float(imm_c)
'''
inf = 800000.0         #starting value of infected people
n_inf = 8000.0         #new infection
act_inf = 160000.0 

n_ill = 4800.0           #number of disease
sum_ill = 480000.0      #all disease
act_ill = 100000.0

death = 14672.0         #all deceased
n_death = 0.0       #new deceased

rec_c = 5000.0         #recovered
n_rec_c = 315781.0       #newly recovered
imm_c = 1200000.0         #immunity, i think it should be exist becouse in case of virus if you don't die you become immune

"""
act_hosp = input("Enter the initial number of new infection: ")
act_hosp = float(akt_hosp) #actuall hospitalisation
"""
n_hosp = 240.0           #number of disease
sum_hosp = 0.0       #all disease
act_hosp = 3532

rc = input("Enter the length of reproduction cycle: ")
rc = int(rc) #reproduction cycle

rate_i = input("Enter disease rate: ")
rate_i = float(rate_i) #disease rate

#LATENCY_TIME = input("Enter avarge latency period: ")
#LATENCY_TIME = int(LATENCY_TIME)

LATENCY_TIME = 5

rate_h = input("Enter hospitality rate: ")
rate_h = float(rate_h)

#HOSP_TIME = input("Enter avarge time of hospitalisation after : ")
#HOSP_TIME = int(HOSP_TIME)
HOSP_TIME = 7

rate_d = input("Enter mortality: ")
rate_d = float(rate_d) #mortality

#D_TIME = input("Enter avarge time of death after the first symptoms : ")
#D_TIME = int(D_TIME)
D_TIME = 18

#REC_TIME = input("Enter avarge time of recover after the first symptoms : ")
#REC_TIME = int(REC_TIME)
REC_TIME = 28

vac = input("Enter vaccination per day: ")
vac = float(vac)

d_t = []
di_t = []
dho_t = []
dd_t = []
dr_t = []

da_t = []
dai_t = []
daho_t = []
dad_t = []
dar_t = []

inf_t = []
n_inf_t = []
act_inf_t = []

n_ill_t = []
sum_ill_t = []
act_ill_t = []

n_hosp_t = []
sum_hosp_t = []
act_hosp_t = []

death_t = []
n_death_t= []

rec_c_t = []
n_rec_c_t = []

filename_sum = "Model_A4_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_sum = open(filename_sum, "w+")

filename_ex_mor = "Model_A4_Daily_Mortality_" + str(ri) + "_" + str(rc) +  "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_mor = open(filename_ex_mor, "w+")

filename_ex_ill = "Mode_A4_Daily_Ill_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_ill = open(filename_ex_ill, "w+")

filename_ex_act_ill = "Mode_A4_Act_ILL_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_act_ill = open(filename_ex_act_ill, "w+")

filename_ex_hosp = "Mode_A4_Daily_Hosp_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_hosp = open(filename_ex_hosp, "w+")

filename_ex_act_hosp = "Mode_A4_Act_Hosp_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_act_hosp = open(filename_ex_act_hosp, "w+")

filename_ex_inf = "Model_A4_Daily_Inf_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" +  str(rate_d) + ".txt"
f_ex_inf = open(filename_ex_inf, "w+")

filename_ex_act_inf = "Mode_A4_Act_Inf_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_ex_act_inf = open(filename_ex_act_inf, "w+")

ACT = input("Enter intervention (Y = apply intervention): ")
ACT = str(ACT)

ACT_TYPE = 0

ACT_POINT_D = pop
ACT_POINT_I = pop

ACT_LENGTH = 1
ACT_START = 0
ACT_TIME_DRIFT = 12

if (ACT == 'Y'):
    
    ACT_TYPE = input("Enter the type of intervention (1 = number of daily deceased case; 2 = number of new patient in hospital per a day): ")
    ACT_TYPE = int(ACT_TYPE)
    
    ACT_TIME_DRIFT = input("Enter the expected time after the action(s) have effect: ")
    ACT_TIME_DRIFT = int(ACT_TIME_DRIFT)

if(ACT_TYPE == 1):
    
    ACT_POINT_D = input("Enter the number of daily deceased case when you interrupt: ")
    ACT_POINT_D = int(ACT_POINT_D)
    
    ACT_LENGTH = input("Enter the length of restriction: ")
    ACT_LENGTH = int(ACT_LENGTH)
    
    ACT_STRENGTH = input("Enter the intensity of restriction: ")
    ACT_STRENGTH = float(ACT_STRENGTH)
    

elif(ACT_TYPE == 2):
    
    ACT_POINT_I = input("Enter the number of hospitalized case when you interrupt: ")
    ACT_POINT_I = int(ACT_POINT_I)
    
    ACT_LENGTH = input("Enter the length of restriction: ")
    ACT_LENGTH = int(ACT_LENGTH)
    
    ACT_STRENGTH = input("Enter the strength of restriction (between 0 and 1): ")
    ACT_STRENGTH = float(ACT_STRENGTH)

CLI = ACT_LENGTH + 1

CRIT_POINT = pop
CRIT_RATE = 1

CRIT = input("Enter critical point (Y = apply critical point): ")
CRIT = str(CRIT)

if (CRIT == 'Y'):
    
    CRIT_POINT = input('Enter the hospital capacity: ')
    CRIT_POINT = float(CRIT_POINT)
    
    CRIT_RATE = input('Enter the mortality rate increase multiplicator: ')
    CRIT_RATE = float(CRIT_RATE)

while(inf < pop and n_inf >= 2):
    
    if (CLI <= ACT_LENGTH & ACT_START >= ACT_TIME_DRIFT):
        
        ri_e = ri*(1 - imm_c/pop)*ACT_STRENGTH#ri: reproduction index multiply with a probality to meet someone who are not infected
        CLI = CLI + 1
        
    else:
        ri_e = ri*(1 - imm_c/pop)
        
    n_inf = n_inf*ri_e  # number of new infection
    n_inf = (n_inf // 1)
        
    if(n_inf < 0):
            
        n_inf = 0 # no negativ new infection
        
    f = int(REC_TIME + LATENCY_TIME)
    if (len(n_inf_t) <= f):
        
        act_inf = act_inf + n_inf/rc
        
    else:
        
        act_inf = 0
        
        for j in range(len(n_inf_t) - f, len(n_inf_t)):
        
            act_inf = act_inf + n_inf/rc
    
    if(act_inf < 0):
        
        act_inf = 0
  
    inf = inf + n_inf #all infection         
    n_ill = n_inf * rate_i    #new disease
    
    if(n_ill < 0):
        
        n_ill = 0
    
    if(n_ill % 2 < (n_ill / 2)): #egészre kerekítés
            
        n_ill = n_ill // 1

    else:
            
        n_ill = (n_ill // 1) + 1 #egészre kerekítés vége
        
    sum_ill = sum_ill + n_ill    #all disease
    
    k = int((REC_TIME - LATENCY_TIME))
    if (len(n_ill_t) <= k):
        
        act_ill = act_ill + n_ill/rc
        
    else:
        
        act_ill = 0
        
        for m in range(len(n_ill_t) - k, len(n_ill_t)):
        
            act_ill = act_ill + n_ill/rc
    
    if(act_ill < 0):
        
        act_ill = 0
    
    n_hosp = n_ill * rate_h    #new disease
    
    if(n_hosp < 0):
        
        n_hosp = 0
    
    if(n_hosp % 2 < (n_hosp / 2)): #egészre kerekítés
            
        n_hosp = n_hosp // 1

    else:
            
        n_hosp = (n_hosp // 1) + 1 #egészre kerekítés vége
    
    if(n_hosp < 0):
        
        n_hosp = 0
    
    if(n_hosp % 2 < (n_hosp / 2)): #egészre kerekítés
            
        n_hosp = n_hosp // 1

    else:
            
        n_hosp = (n_hosp // 1) + 1 #egészre kerekítés vége
        
    sum_hosp = sum_hosp + n_hosp
    
    s = int((REC_TIME - HOSP_TIME)/2)
    if (len(n_hosp_t) <= s):
        
        act_hosp = act_hosp + n_hosp/rc
        
    else:
        
        act_hosp = 0
        
        for n in range(len(n_hosp_t) - s, len(n_hosp_t)):
        
            act_hosp = act_hosp + n_hosp/rc
    
    if(act_hosp < 0):
        
        act_hosp = 0
        
    if (act_hosp >= ACT_POINT_I):
        
        CLI = 0
        ACT_START = ACT_START + rc
    
    if (act_hosp > CRIT_POINT):
    
        n_death = (n_ill - (act_hosp - CRIT_POINT)) * rate_d + (act_hosp - CRIT_POINT) * rate_d * CRIT_RATE     #new deceased
    
    else:
        
        n_death = n_ill * rate_d
        
    if(n_death < 0):
        
        n_death = 0
    
    if(n_death % 2 < (n_death / 2)): #egészre kerekítés
            
        n_death = n_death // 1
            
    else:
            
        n_death = (n_death // 1) + 1 #egészre kerekítés vége
    
    if (n_death/rc >= ACT_POINT_D):
        
        CLI = 0
        ACT_START = ACT_START + rc
            
    n_rec_c = act_ill * (1 - rate_d)
    
    if(n_rec_c % 2 < (n_rec_c / 2)): #egészre kerekítés
            
        n_rec_c = n_rec_c // 1
            
    else:
            
        n_rec_c = (n_rec_c // 1) + 1 #egészre kerekítés vége
    
    death = death + n_death #elhunytak, gyógyultak, immunitással rendelektők száma
    rec_c = rec_c + n_rec_c
    
    if rec_c > pop:
        
        rec_c = pop
    
    imm_c = rec_c * 0.95 + (rc * vac)
    
    if imm_c > pop:
        
        imm_c = pop

    if(imm_c % 1 < (imm_c / 2)): #egészre kerekítés
            
        imm_c = imm_c // 1
            
    else:
            
        imm_c = (imm_c // 1) + 1 #egészre kerekítés vége
        
    pop = pop - n_death #populáció csökkennás
    
    di = int(d) + LATENCY_TIME
    dho = int(di) + HOSP_TIME
    dd = int(di) + D_TIME
    dr = int(di) + REC_TIME
    d = int(d) + rc
    
    d_t.append(d)
    di_t.append(di)
    dho_t.append(dho)
    dd_t.append(dd)
    dr_t.append(dr)
        
    inf_t.append(inf)
    sum_ill_t.append(sum_ill)
    #act_ill_t.append(act_ill)
    sum_hosp_t.append(sum_hosp)
    #act_hosp_t.append(act_hosp)
    death_t.append(death)
    rec_c_t.append(rec_c)
    
    f_sum.write("%d %.3f   %d %.3f %.3f   %d %.3f   %d %.3f\n"  % (d, inf, di, sum_ill, sum_hosp, dd, death, dr, rec_c))
    
    for i in range(0, rc):
        
        n_inf_t.append(int(n_inf/rc))
        act_inf_t.append(act_inf)
        n_ill_t.append(int(n_ill/rc))
        act_ill_t.append(act_ill)
        n_hosp_t.append(int(n_hosp/rc))
        act_hosp_t.append(act_hosp)
        n_death_t.append(int(n_death/rc))
        n_rec_c_t.append(int(n_rec_c/rc))
        
        f_ex_mor.write("%d\n"  % (int(n_death/rc)))
        f_ex_ill.write("%d\n"  % (int(n_ill/rc)))
        f_ex_act_ill.write("%d\n"  % (int(act_ill)))
        f_ex_hosp.write("%d\n"  % (int(n_hosp/rc)))
        f_ex_act_hosp.write("%d\n" % (int(act_hosp)))
        f_ex_inf.write("%d\n"  % (int(n_inf/rc)))
        f_ex_act_inf.write("%d\n"  % (int(act_inf)))
    
for i in range(0, rc*len(d_t)):
    
    da_t.append(i)
    dai_t.append(i + LATENCY_TIME)
    daho_t.append(i + HOSP_TIME)
    dad_t.append(i + D_TIME)
    dar_t.append(i + REC_TIME)
    
guess = np.array([25, 100000, 50, 1])
params, extras = sciopt.curve_fit(Gauss, da_t, act_inf_t, guess)
act_inf_fit = Gauss(da_t, params[0], params[1], params[2], params[3])

guess = np.array([25, 600000, 50, 1])
params, extras = sciopt.curve_fit(Gauss, dai_t, act_ill_t, guess)
act_ill_fit = Gauss(dai_t, params[0], params[1], params[2], params[3])

guess = np.array([25, 30000, 50, 1])
params, extras = sciopt.curve_fit(Gauss, daho_t, act_hosp_t, guess)
act_hosp_fit = Gauss(daho_t, params[0], params[1], params[2], params[3])

guess = np.array([25, 10000, 50, 1])
params, extras = sciopt.curve_fit(Gauss, da_t, n_inf_t, guess)
n_inf_fit = Gauss(da_t, params[0], params[1], params[2], params[3])

guess = np.array([20, 50000, 50, 1])
params, extras = sciopt.curve_fit(Gauss, dai_t, n_ill_t, guess)
n_ill_fit = Gauss(dai_t, params[0], params[1], params[2], params[3])

guess = np.array([20, 1000, 60, 1])
params, extras = sciopt.curve_fit(Gauss, daho_t, n_hosp_t, guess)
n_hosp_fit = Gauss(daho_t, params[0], params[1], params[2], params[3])

guess = np.array([20, 200, 70, 1])
params, extras = sciopt.curve_fit(Gauss, dad_t, n_death_t, guess)
n_death_fit = Gauss(dad_t, params[0], params[1], params[2], params[3])

guess = np.array([20, 130000, 80, 1])
params, extras = sciopt.curve_fit(Gauss, dar_t, n_rec_c_t, guess)
n_rec_fit = Gauss(dar_t, params[0], params[1], params[2], params[3])

filename_act_inf_fit = "Mode_A4_Act_Inf_fit" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_act_inf_fit = open(filename_act_inf_fit, "w+")

filename_act_ill_fit = "Mode_A4_Act_Inf_fit" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_act_ill_fit = open(filename_act_inf_fit, "w+")

for i in range(0, len(dai_t)):
    
    f_act_inf_fit.write("%d\n"  % (int(act_inf_fit[i])))
    f_act_ill_fit.write("%d\n"  % (int(act_ill_fit[i]))) 

filename_daily_hosp_fit = "Mode_A4_Daily_Hosp_fit_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_daily_hosp_fit = open(filename_daily_hosp_fit, "w+")

filename_act_hosp_fit = "Mode_A4_Act_Hosp_fit_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_act_hosp_fit = open(filename_act_hosp_fit, "w+")

for i in range(0, len(daho_t)):
    
    f_daily_hosp_fit.write("%d\n"  % (int(n_hosp_fit[i])))
    f_act_hosp_fit.write("%d\n"  % (int(act_hosp_fit[i]))) 

filename_daily_mort_fit = "Mode_A4_Mortality_fit_" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_daily_mortality_fit = open(filename_daily_mort_fit, "w+")

for i in range(0, len(dad_t)):
    
    f_daily_mortality_fit.write("%d\n"  % (int(n_death_fit[i])))

filename_daily_rec_fit = "Mode_A4_Daily_Rec_fit" + str(ri) + "_" + str(rc) + "_" + str(rate_i) + "_" + str(rate_d) + ".txt"
f_daliy_rec_fit = open(filename_daily_rec_fit, "w+")

for i in range(0, len(dar_t)):
    
    f_daily_mortality_fit.write("%d\n"  % (int(n_rec_c_t[i])))

figurename_1 = 'model_A4_figure_Total' + '_' + str(ri) + "_" + str(rc) + '_' + str(rate_i) + '_' + str(rate_d) + '.png'
figurename_2 = 'model_A4_figure_Daily' + '_' + str(ri) + "_" + str(rc) + '_' + str(rate_i) + '_' + str(rate_d) + '.png'
figurename_3 = 'model_A4_figure_Actually' + '_' + str(ri) + "_" + str(rc) + '_' + str(rate_i) + '_' + str(rate_d) + '.png'

plt.clf()
plt.figure(1)

plt.subplot(511)
plt.plot(d_t, inf_t, 'bo', markersize = 1)
plt.ylabel("Totlal number of infections", fontsize = 5)
plt.title("Number of infected, patients, deceased and recovered (all)\n(Population = %.0f, R = %.2f, RC = %d, Disease rate = %.2f, Mortality = %.3f)" %(pop_k, ri, rc, rate_i, rate_d), fontsize=14)

plt.subplot(512)
plt.plot(di_t, sum_ill_t, 'yo', markersize = 1)
plt.ylabel("Number of all patients", fontsize = 5)

plt.subplot(513)
plt.plot(dho_t, sum_hosp_t, 'mo', markersize = 1)
plt.ylabel("Number of all hospitalisation", fontsize = 5)

plt.subplot(514)
plt.plot(dd_t, death_t, 'ro', markersize = 1)
plt.ylabel("Number of all deceased", fontsize = 5)

plt.subplot(515)
plt.plot(dr_t, rec_c_t, 'go', markersize = 1)
plt.ylabel("Number of totaly recovered", fontsize = 5)
plt.xlabel("Days", fontsize = 8)
plt.show()

plt.savefig(figurename_1, dpi = 600)

plt.clf()
plt.figure(2)

plt.subplot(511)
plt.plot(da_t, n_inf_t, 'co', markersize = 1)
plt.plot(da_t, n_inf_fit, 'c-', markersize = 1)
plt.ylabel("Number of daily infections", fontsize = 5)
plt.title("Number of infected, patients, deceased and recovered (Daily)\n(Population = %.0f, R = %.2f, RC = %d, Disease rate = %.2f, Mortality = %.3f)" %(pop_k, ri, rc, rate_i, rate_d), fontsize=14)

plt.subplot(512)
plt.plot(dai_t, n_ill_t, 'mo', markersize = 1)
plt.plot(dai_t, n_ill_fit, 'm-', markersize = 1)
plt.ylabel("Number of daily new patients", fontsize = 5)

plt.subplot(513)
plt.plot(daho_t, n_hosp_t, 'ro', markersize = 1)
plt.plot(daho_t, n_hosp_fit, 'r-', markersize = 1)
plt.ylabel("Number of patients in hospital", fontsize = 5)

plt.subplot(514)
plt.plot(dad_t, n_death_t, 'ko', markersize = 1)
plt.plot(dad_t, n_death_fit, 'k-', markersize = 1)
plt.ylabel("Number of daily deceased", fontsize = 5)

plt.subplot(515)
plt.plot(dar_t, n_rec_c_t, 'go', markersize = 1)
plt.plot(dar_t, n_rec_fit, 'g-', markersize = 1)
plt.ylabel("Number of newly recovered", fontsize = 5)
plt.xlabel("Days", fontsize = 8)
plt.show()

plt.savefig(figurename_2, dpi = 600)

plt.clf()
plt.figure(3)

plt.subplot(311)
plt.plot(da_t, act_inf_t, 'yo', markersize = 1)
plt.plot(da_t, act_inf_fit, 'y-', markersize = 1)
plt.ylabel("Number of actually infected people", fontsize = 5)
plt.title("Number of actuall infected people, patients and patients in hospital (Actuall data)\n(Population = %.0f, R = %.2f, RC = %d, Disease rate = %.2f, Mortality = %.3f)" %(pop_k, ri, rc, rate_i, rate_d), fontsize=14)

plt.subplot(312)
plt.plot(dai_t, act_ill_t, 'mo', markersize = 1)
plt.plot(dai_t, act_ill_fit, 'm-', markersize = 1)
plt.ylabel("Number of actually sick people", fontsize = 5)

plt.subplot(313)
plt.plot(daho_t, act_hosp_t, 'ro', markersize = 1)
plt.plot(daho_t, act_hosp_fit, 'r-', markersize = 1)
plt.ylabel("Number of actuall patients in hospital", fontsize = 5)
plt.show()

plt.savefig(figurename_3, dpi = 600)

print('\n')
print("Number of infections = %.0f" % inf)
print("Number of patients = %.0f" % sum_ill)
print("Number of hospitalisation = %.0f" % sum_hosp)
print("Number of deceased = %.0f" % death)
print("Recovered = %.0f" % rec_c)
print("People with immunity = %.0f" % imm_c)
print("Expected end of epidemic is the %.0f. day from the zero day (if the parameters are considered constant)." % dr)

f_sum.write("Basic reproduction index = %.3f\nDisease rate = %.3f\nHospitality rate = %.3f\nMortality = %.3f\nNumber of infections = %.0f\nNumber of patients = %.0f\nNumber of deceased = %.0f\nRecovered = %.0f\nPeople with immunity = %.0f\nExpected end of epidemic is the %.0f. day from the zero day (if the parameters are considered constant)." % (ri, rate_i, rate_h, rate_d, inf, sum_ill, death, rec_c, dr, imm_c))