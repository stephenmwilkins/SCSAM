import numpy as np
import h5py

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# --- make a simple redshift histogram of galaxies in the sample


filename = 'lightcone'

# --- open the HDF5 file
cat = h5py.File(f'../../{filename}.h5', 'r')

z = cat['redshift'][:]
ra = np.pi*2*cat['ra'][:]/360 # rad
dec = np.pi*2*cat['dec'][:]/360 # rad

# --- get min, median, max
for x in [ra,dec]:
    for fun in [np.min, np.median, np.max]:
        print(fun.__name__, f'{fun(x):.2f}')




for theta_name, theta in zip(['ra','dec'], [ra, dec]):

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    ax.scatter(theta, z)

    fig.savefig(f'z_{theta_name}.png')
