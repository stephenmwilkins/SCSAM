
# --- create a custom catalogue with only specific columns and an optional flux cut

import h5py
import numpy as np

# custom_cat_name = 'Euclid'
# columns = []
# columns += [f'galphotdust/{x}' for x in ['z', 'LSST_u', 'LSST_g', 'LSST_r', 'LSST_i', 'LSST_z', 'LSST_y', 'Euclid_VIS', 'Euclid_Y', 'Euclid_J', 'Euclid_H']]
# columns += [f'FIR/{x}' for x in ['spire500']]




# cat = 'lightcone'
# custom_cat_name = 'lightcone_Euclid'
#
# columns = ['z']
# columns += [x+'_dust' for x in ['LSST_u', 'LSST_g', 'LSST_r', 'LSST_i', 'LSST_z', 'LSST_y', 'Euclid_Y', 'Euclid_J', 'Euclid_H', 'irac_ch1','irac_ch2','irac_ch3','irac_ch4']]
#
# cut_column = False
# cut_column, cut_threshold, lt = 'Euclid_H_dust', 26.5, True


custom_cat_name = 'Kelsie'
columns = []
columns += [f'galphotdust/{x}' for x in ['z', 'Euclid_H', 'NIRCam_F150W', 'VISTA_H', 'wfc3f160w']]
columns += [f'FIR/{x}' for x in ['L_bol', 'L_dust', 'spire500', 'spire350','spire250','scuba850','pacs160','pacs100']]
# columns += [f'galprop/{x}' for x in ['mstar','sfr_ave']] # doesn't work - not correct length
cut_column = False




# --- open the catalogues we need
cats = set(map(lambda x: x.split('/')[0], columns)) # determine the catalogues we need to open
print(cats)
cat = {}
for c in cats:
    print(c)
    cat[c] = h5py.File(f'../../{c}.h5', 'r')

if cut_column:
    c, k = cut_column.split('/')
    if lt:
        s = cat[c][k][:] < cut_threshold
    else:
        s = cat[c][k][:] > cut_threshold

# --- create output file
custom_cat = h5py.File(f'../../custom/{custom_cat_name}.h5', 'w')


for col in columns:
    c, k = col.split('/')

    if cut_column:
        data = cat[c][k][s]
    else:
        data = cat[c][k]

    custom_cat.create_dataset(col, data = data)

print(custom_cat.keys())



print('Number of galaxies:', len(custom_cat[columns[0]][:]))
custom_cat.close()
