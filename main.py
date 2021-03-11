############################################Tidholm et. al.##############################################

# A snapshot of a canonocal ensemble is finished 
    # Self conistent phonon calculations 

# 1 iteration = 30 configurations to convergence of phonon-dispersion relationas and phonon free energy 
# approximately 3 iterations for Nb

# Program start 
    # Read from phonon calculations (OUTCAR)
        # eigenvalue and eigenvector of of dynamical matrix (omega_s, epsilon_S) 
        # occupation number (bose ein. stats.) ns
            # 1) can be approximate classically 
            # 2) obtain the canonical partition function Z from which we can derive ns following Bose-eisnsetin statistcs
        # mass of ith ion mi
    # Sample phase space
        # calulate ui and u_doti in alpha direction (cartersian componant in the alha direction for ... 
        # the diplacement from the thermal avg. and velocity for ion i)
            # 1) xi1 xi2 uniformly distributed (0,1)
            # 3) calculate oscillation amplitude (will include zero point motion)
        # populate supercells (configurations)
# Program end
# Input supercells to DFT
# Calculation energies and forces (DFT)
# Calculate phonons (TDEP)
# Back to program start 
#########################################################################################################

import numpy as np
import sys
from read_tdep import read
from calc import convert_nuclear

# read the outcar and obtain ion information, normal mode frequencies and dispacements
tdep = read()
epsilon = tdep.epsilons
omega = tdep.omegas
mass = tdep.mass
mass = np.array([i*1.66053886E-27 for i in mass])  
omega = np.array([i*100 for i in omega])

# convert from normal mode frequencies to nuclear coordinates
nuclear = convert_nuclear(epsilon,omega,mass)
u = nuclear.u
up = nuclear.up

