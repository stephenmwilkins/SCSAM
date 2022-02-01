

import h5py
import numpy as np

def create_new(name, item):
    if hasattr(item, 'value'):
        hf.create_dataset(name, (Ntot,))

def append(name, item):
    if hasattr(item, 'value'):
        N = len(item.value)
        hf[name][Ns:Ns+N] = item[()]


topdir = f'/Users/stephenwilkins/Downloads'

redshifts = [0.0,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.25,1.5,1.75,2.0,2.25,2.5,2.75,3.,3.25,3.5,3.75,4.,4.5,5.,5.5,6.,7.,8.,9.,10.]

# redshifts = [0.0,0.05,0.1]

Nfiles = len(redshifts)-1

files = ['galphot','galprop','halos','lightcone']
files = ['lightcone']

for f in files: #'FIR','galphotdust',

    N = np.zeros(Nfiles, dtype=int)

    for i, (z1,z2) in enumerate(zip(redshifts[:-1],redshifts[1:])):

        dir = f'{topdir}/part_z{z1:.2f}_z{z2:.2f}'

        with h5py.File(f'{dir}/{f}.h5', 'r') as file:
            N[i] = len(file[list(file.keys())[0]])
            print(i, z1,z2, N[i])

    Ntot = np.sum(N)
    print(f'total number of galaxies: {Ntot}')



    # --- create output file
    hf = h5py.File(f'{f}.h5', 'w')

    dir = f'{topdir}/part_z{redshifts[0]:.2f}_z{redshifts[1]:.2f}'

    first_hf = h5py.File(f'{dir}/{f}.h5', 'r')

    for key, value in first_hf.attrs.items():
        hf.attrs[key] = value

    first_hf.visititems(create_new)
    first_hf.close()

    # ---------------------------------------------
    # --- append each entry

    Ns = 0
    for i, (z1,z2) in enumerate(zip(redshifts[1:-1],redshifts[2:])):
        dir = f'{topdir}/part_z{z1:.2f}_z{z2:.2f}'
        next_hf = h5py.File(f'{dir}/{f}.h5', 'r')
        next_hf.visititems(append)
        next_hf.close()
        Ns += N[i+1]

    print('Number in final file:', len(hf[list(hf.keys())[0]]))

    hf.close()
