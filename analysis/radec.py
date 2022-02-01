import numpy as np
import h5py

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# --- make a simple redshift histogram of galaxies in the sample


filename = 'lightcone'

# --- open the HDF5 file
cat = h5py.File(f'../../{filename}.h5', 'r')

ra = cat['ra'][:]
dec = cat['dec'][:]

# --- get min, median, max
for x in [ra,dec]:
    for fun in [np.min, np.median, np.max]:
        print(fun.__name__, f'{fun(x):.2f}')


fig = plt.figure(figsize = (4, 4)) # 4" x 4" square

left  = 0.15
bottom = 0.15
width = 0.8 # space left for a colour bar
height = 0.8 # space left for a colour bar

ax = fig.add_axes((left, bottom, width, height)) # add an axis

ax.scatter(ra,dec)

ax.set_xlabel(r'$\rm ra$') # colour notation is e.g. Y-J
ax.set_ylabel(r'$\rm dec$') # colour notation is e.g. Y-J

fig.savefig(f'radec.png')

fig.clf() # clear figure

fig.clf() # clear figure
