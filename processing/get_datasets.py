


import h5py

for f in ['FIR','galphotdust','galphot','galprop','halos','lightcone']:

    print('-'*5,f,'-'*5)

    with h5py.File(f'{f}.h5', 'r') as file:
        for k in file.keys():
            print(k)
