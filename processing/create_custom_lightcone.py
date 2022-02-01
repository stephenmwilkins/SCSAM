
# --- create a custom catalogue with only specific columns and an optional flux cut

import h5py
import numpy as np

# custom_cat_name = 'Euclid'
# columns = []
# columns += [f'galphotdust/{x}' for x in ['z', 'LSST_u', 'LSST_g', 'LSST_r', 'LSST_i', 'LSST_z', 'LSST_y', 'Euclid_VIS', 'Euclid_Y', 'Euclid_J', 'Euclid_H']]
# columns += [f'FIR/{x}' for x in ['spire500']]

c = 'lightcone'
custom_cat_name = 'lightcone_Euclid'

columns = ['redshift']
columns += [x+'_dust' for x in ['LSST_u', 'LSST_g', 'LSST_r', 'LSST_i', 'LSST_z', 'LSST_y', 'Euclid_VIS', 'Euclid_Y', 'Euclid_J', 'Euclid_H', 'irac_ch1','irac_ch2']]


# cut_column = False
cut_column, cut_threshold, lt = 'Euclid_H_dust', 26.5, True


cat = h5py.File(f'{c}.h5', 'r')

if cut_column:
    if lt:
        s = cat[cut_column][:] < cut_threshold
    else:
        s = cat[cut_column][:] > cut_threshold

# --- create output file
custom_cat = h5py.File(f'{custom_cat_name}.h5', 'w')


for col in columns:
    if cut_column:
        data = cat[col][s]
    else:
        data = cat[col][k]

    custom_cat.create_dataset(col, data = data)

print(custom_cat.keys())



print('Number of galaxies:', len(custom_cat[columns[0]][:]))
custom_cat.close()
