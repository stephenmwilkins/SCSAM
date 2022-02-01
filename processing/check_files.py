

import os
import sys
import numpy as np


redshifts = [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.,3.25,3.5,3.75,4.,4.5,5.,5.5,6.,7.,8.,9.,10.]

for z1,z2 in zip(redshifts[:-1],redshifts[1:]):

    dir = f'part_z{z1:.2f}_z{z2:.2f}'

    try:
        FIR = np.loadtxt(f'/Users/stephenwilkins/Downloads/{dir}/FIR.dat')
        galphotdust = np.loadtxt(f'/Users/stephenwilkins/Downloads/{dir}/galphotdust.dat')
        lightcone = np.loadtxt(f'/Users/stephenwilkins/Downloads/{dir}/lightcone.dat')
        print(z1, z2, FIR.shape[0], galphotdust.shape[0], lightcone.shape[0])
    except:
        print(z1, z2, 'FAILED')
