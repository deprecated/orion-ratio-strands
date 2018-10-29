# ---
# jupyter:
#   jupytext_format_version: '1.2'
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.3
# ---

import ipyvolume as ipv

import numpy as np

from astropy.io import fits

# +
hdu1 = fits.open('../Ratios-for-Alba/ratio-6583-6563.fits')[0]
hdu2 = fits.open('../Ratios-for-Alba/ratio-5007-4861.fits')[0]
hdu3 = fits.open('../Ratios-for-Alba/ratio-9069-6731.fits')[0]
x = hdu1.data.ravel()
y = hdu2.data.ravel() 
z = hdu3.data.ravel()

xyzrange = [0.0, 0.7], [0.0, 5.0], [0, 25]
H, edges = np.histogramdd(np.stack((x, y, z)).T, bins=[150, 150, 150], range=xyzrange)

# + {"scrolled": false}
ipv.quickvolshow(H.T, lighting=True, level=[0.08, 0.2, 0.50], opacity=[0.04, 0.05, 0.10], level_width=0.05)

# +
hdu1 = fits.open('../Ratios-for-Alba/ratio-6583-6563.fits')[0]
hdu2 = fits.open('../Ratios-for-Alba/ratio-5007-4861.fits')[0]
hdu3 = fits.open('../Ratios-for-Alba/ratio-7330-6583.fits')[0]
x = hdu1.data.ravel()
y = hdu2.data.ravel() 
z = hdu3.data.ravel()

xyzrange = [0.0, 0.7], [0.0, 5.0], [0, 0.2]
H, edges = np.histogramdd(np.stack((x, y, z)).T, bins=[150, 150, 150], range=xyzrange)
# -

ipv.quickvolshow(H.T, lighting=True, level=[0.08, 0.2, 0.50], opacity=[0.04, 0.05, 0.10], level_width=0.05)

# +
hdu1 = fits.open('../Ratios-for-Alba/ratio-6583-6563.fits')[0]
hdu2 = fits.open('../Ratios-for-Alba/ratio-5007-4861.fits')[0]
hdu3 = fits.open('../Ratios-for-Alba/ratio-6716-6731.fits')[0]
x = hdu1.data.ravel()
y = hdu2.data.ravel() 
z = hdu3.data.ravel()

xyzrange = [0.0, 0.7], [0.0, 5.0], [0, 1.6]
H, edges = np.histogramdd(np.stack((x, y, z)).T, bins=[150, 150, 150], range=xyzrange)
# -

ipv.quickvolshow(H.T, lighting=True)

ipv.quickvolshow?


