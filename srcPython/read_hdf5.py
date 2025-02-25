#!/usr/bin/env python

import datetime as dt
import numpy as np
import h5py

filename = 'VISTA_110805.hdf5'


iYr_ = filename.find('.hdf5') - 6
year = 2000 + int(filename[iYr_ : iYr_ + 2])
month = int(filename[iYr_ + 2 : iYr_ + 4])
day = int(filename[iYr_ + 4 : iYr_ + 6])

basetime = dt.datetime(year, month, day, 0, 0, 0)
print(basetime)

f = h5py.File(filename, 'r')

print('keys : ')
for key in f.keys():
    print(' -> ', key)
    
print('inside the keys : ')
for key in f.keys():
    print(' -> ', f[key].keys())


print('inside data attributes : ')
for key in f['data'].attrs.keys():
    print(' -> ', key)
    
vista = np.array(f['data']['VISTA'])
print(np.shape(vista))
    
f.close()
    
