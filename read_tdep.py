# rough script to ready phonon information from TDEP SC run - OUTCAR 

import numpy as np
import sys
from dataclasses import dataclass

@dataclass
class Returnvalue:
    mass: list 
    epsilons: list
    omegas: list


def read():

    nions = 0 # number of ions 
    nspecies = 0 # number of total species
    dof = 0 # number of modes 3
    mass = [] # list for masses (in a.u.)
    i = 0
    j = 0

    file = open('OUTCAR', 'r') 
    while True:
        line = file.readline()
        if 'ions per type' in line:
            ipt = line.split()[-2:]
            ipt = [int(i) for i in ipt]
        elif 'NIONS' in line:
            nions = int(line.split()[-1])
            dof = 3*nions
            omegas = np.zeros(shape=dof)
            epsilons = np.empty(shape=(dof,nions,3))
        elif 'POMASS' in line and 'ZVAL' not in line:
            line = line.split()
            nspecies = len(line) - 2
            tmp = line[-2:]
            tmp = [float(i) for i in tmp]
            for l,m in zip(ipt,tmp):
                for o in range(l):
                    mass.append(m)
            mass = np.array(mass)
        elif 'THz' in line:
            # get eigenvals
            if 'f/i' in line:
                omegas[i] = float(line.split()[6])
                pass
            else:
                omegas[i] = float(line.split()[7])
            i+=1
            # get eigenvectors
        elif 'dx' in line and 'dy' in line and 'dz' in line:
            count = 0
            xyz = []
            while count < nions:
                line = file.readline().split()
                xyz.append([float(line[3]),float(line[4]),float(line[5])])
                count +=1
            xyz = np.array(xyz)
            epsilons[j] = xyz
            j+=1
        if not line:
            file.close()
            return Returnvalue(mass,epsilons,omegas)
