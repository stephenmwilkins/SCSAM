
import h5py


# plot the number of galaxies as a function of redshift in total and selected (see cc.py for selection)


filename = 'custom/Kelsie'

# --- open the HDF5 file
cat = h5py.File(f'../../{filename}.h5', 'r')

# --- print all the datasets
cat.visititems(print)
