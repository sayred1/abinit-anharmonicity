# possible to sample bose-einstein number without a MD run?

import numpy as np
import sys
from dataclasses import dataclass

@dataclass
class Returnvalue:
    # return cartersian nuclear positions and kinetic energy
    u: list
    up: list

def convert_nuclear(q=None , w=None, m=None):
    """
    This function converts the normal mode coordinates into cartesian nuclear coordinates
        q: displacement vectors 
            float array - (num. modes, num ions, 3)
        w: frequency modes
            float array - (num. modes)
        m: ionic mass
            float array - (num. ions)
    """

    nions = m.shape[0] 
    nmodes = q.shape[0]
    u = np.zeros((nions,3))
    up = np.zeros((nions,3))
    
    # loop over ions 
    for ion in range(nions):
        mion = m[ion]
        xi_1 = np.random.uniform()
        xi_2 = np.random.uniform()
        # loop over modes
        for mode in range(nmodes):
            w_ = w[mode]
            q_ = q[mode,ion,:]
            A = oscillation_amplitude(mion, w_)
            # print('     mode %s: A = %s, frequency = %s, vector = %s i + %s j + %s k' %(j+1,A,wi,eps[0],eps[1],eps[2]))  
            u[ion] += q_*A*np.sqrt(-2*np.log(xi_1))*np.sin(2*np.pi*xi_2)
            up[ion] +=  w_*q_*A*np.sqrt(-2*np.log(xi_1))*np.cos(2*np.pi*xi_2)
    return Returnvalue(u,up)

def oscillation_amplitude(m, w, T = 300):
    # function of atomic m i and vibrational mode freq.
    # freq has eigenvector dxdydz which discusses displacement of i atom
    # this is where the switch between md and stochastic implementation deviates
    h_bar = 1.054571817E-34
    kB = 1.38E-23
    return 1/w * np.sqrt(kB*T/m)
