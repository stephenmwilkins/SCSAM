

import numpy as np
import h5py

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# plot the number of galaxies as a function of redshift in total and selected (see cc.py for selection)





# --- open the HDF5 file
cat = h5py.File('Euclid.h5', 'r')






z = cat['z'][:] # the redshift of the galaxy


fig = plt.figure(figsize = (4, 4)) # 4" x 4" square

left  = 0.15
bottom = 0.15
width = 0.8 # space left for a colour bar
height = 0.8 # space left for a colour bar

ax = fig.add_axes((left, bottom, width, height)) # add an axis

# --- plot a histogram of all galaxies
ax.hist(z, range = [0, 10], bins = 100, log = True, alpha = 0.5, label = 'all galaxies')


ax.set_xlabel(r'$\rm z$') # colour notation is e.g. Y-J
ax.set_ylabel(r'$\rm\log_{10}(N)$') # colour notation is e.g. Y-J

fig.savefig(f'N.pdf')

fig.clf() # clear figure
