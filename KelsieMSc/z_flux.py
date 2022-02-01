

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



for f in ['FIR/spire250','galphotdust/Euclid_H']:

    print(f,'-'*20)

    # ---------------
    # NOTE - the units of quantities in galphotdust appear to be AB magnitudes while I can only imagine the units of FIR quantities are uJy. The code below **should** convert both to nJy.

    for fun in [np.min, np.median, np.max]:
        print(fun.__name__, f'{fun(cat[f][:])}')

    if f.split('/')[0] == 'FIR':
        flux = cat[f][:]*1E6 # uJy
    if f.split('/')[0] == 'galphotdust':
        m = cat[f][:]
        flux = 10**(-0.4*m)*3631*1E6 # uJy

    for fun in [np.min, np.median, np.max]:
        print(fun.__name__, f'{fun(flux):.2f}')

    # --- NOTE: there are many ways to use matplotlib. This is my **favourite** since it allows the most control over plot. However, something similar can be acheived with fewer steps.

    # --------------- SCATTER PLOT

    # --- initiate a figure
    # fig = plt.figure(figsize = (4, 4)) # 4" x 4" square
    #
    # left  = 0.15
    # bottom = 0.15
    # width = 0.8
    # height = 0.8
    #
    # ax = fig.add_axes((left, bottom, width, height)) # add an axis
    #
    #
    # ax.scatter(z, np.log10(flux), s = 1, alpha =  0.01) # s and alpha control the size and transparency. Since there are so many points these need to be set to values other than the default
    #
    # if f == 'galphotdust/Euclid_H': ax.axhline(np.log10(10**(-0.4*26.)*3631*1E6),c='k',lw=1)
    # if f == 'FIR/spire250': ax.axhline(4,c='k',lw=1)
    #
    # ax.set_xlim([0,10])
    #
    # ax.set_xlabel('z')
    # ax.set_ylabel(rf'$log_{{10}}({f.split("/")[1]}/\mu Jy)$')
    #
    # fig.savefig(f'z_{f.split("/")[1]}.png', dpi = 200) # save the figure. Probaby need to use a raster format (.png) due to so many points
    # fig.clf() # clear figure
