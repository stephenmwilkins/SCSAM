

import numpy as np
import h5py

import matplotlib as mpl
import matplotlib.pyplot as plt

# make a simple plot of flux vs. redshift





filename = 'custom/Kelsie'

# --- open the HDF5 file
cat = h5py.File(f'../../{filename}.h5', 'r')



# --- define shorthand for quantities

z = cat['galphotdust/z'][:] # the redshift of the galaxy

f = 'galphotdust/Euclid_H' # dust attenuation Euclid H-band (1.6um) flux

m = cat[f][:] # the AB apparent magnitude in filter f.


print(np.min(m),np.median(m),np.max(m))



# --- NOTE: there are many ways to use matplotlib. This is my **favourite** since it allows the most control over plot. However, something similar can be acheived with fewer steps.


# --------------- SCATTER PLOT

# --- initiate a figure
fig = plt.figure(figsize = (4, 4)) # 4" x 4" square

left  = 0.15
bottom = 0.15
width = 0.8
height = 0.8

ax = fig.add_axes((left, bottom, width, height)) # add an axis


ax.scatter(z, m, s = 1, alpha =  0.05) # s and alpha control the size and transparency. Since there are so many points these need to be set to values other than the default


# for z in np.arange(0.0,10,0.25):
#     ax.axvline(z, color='k', lw=1, alpha=0.5)

ax.set_xlim([0,10])

ax.set_xlabel('z')
ax.set_ylabel(f'{f}')


fig.savefig(f'z_mag.png', dpi = 200) # save the figure. Probaby need to use a raster format (.png) due to so many points
fig.clf() # clear figure
