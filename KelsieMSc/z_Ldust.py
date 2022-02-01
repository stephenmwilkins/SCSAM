

import numpy as np
import h5py

import matplotlib as mpl
import matplotlib.pyplot as plt

# make a simple plot of dust luminosity vs. redshift. This shold look like Fig. 14a from https://arxiv.org/pdf/2105.05659.pdf though with more faint galaxies.


filename = 'custom/Kelsie'

# --- open the HDF5 file
cat = h5py.File(f'../../{filename}.h5', 'r')



# --- define shorthand for quantities

z = cat['galphotdust/z'][:] # the redshift of the galaxy

log10Ldust = cat['FIR/L_dust'][:] # the log10(L_dust/L_sun)

for fun in [np.min, np.median, np.max]:
    print(fun.__name__, f'{fun(log10Ldust):.2f}')


# --- NOTE: there are many ways to use matplotlib. This is my **favourite** since it allows the most control over plot. However, something similar can be acheived with fewer steps.

# --------------- SCATTER PLOT

# --- initiate a figure
fig = plt.figure(figsize = (4, 4)) # 4" x 4" square

left  = 0.15
bottom = 0.15
width = 0.8
height = 0.8

ax = fig.add_axes((left, bottom, width, height)) # add an axis


ax.scatter(z, log10Ldust, s = 1, alpha =  0.01) # s and alpha control the size and transparency. Since there are so many points these need to be set to values other than the default

ax.set_xlim([0,10])
ax.set_ylim([8,13])

ax.set_xlabel('z')
ax.set_ylabel(r'$log_{{10}}(L_{dust}/L_{\odot})$')

fig.savefig(f'z_Ldust.png', dpi = 200) # save the figure. Probaby need to use a raster format (.png) due to so many points
fig.clf() # clear figure
