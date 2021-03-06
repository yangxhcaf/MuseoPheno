# -*- coding: utf-8 -*-
"""
Compute a spectral index or an expression without defining a sensor
=============================================================================

This example shows how to compute an expression or an index in a time series (or at one acquisition)
without defining a sensor.

"""

##############################################################################
#   Use sample from Sentinel2 level 3A syntheses (from Theia)
# --------------------------------------------------------------------
from museopheno.time_series import expression_manager
from museopheno import datasets

X,dates = datasets.Sentinel2_3a_2018(return_dates=True,return_random_sample=True)

print(X.shape)

##############################################################################
# We have to define the band order and the number of compenent (i.e. number of band per date)
#

bands_order = ['2','3','4','8','5','6','7','8A','11','12']

##############################################################################
# As our raster has 10 bands per date, let's check the number of columns of X array  divided by the numver of bands per date
#

print('Image contains {} dates.'.format(int(X.shape[1]/len(bands_order))))

##############################################################################
#   Let's create an expression
# --------------------------------------------------------------------------

expression = 'B8/(B2+1)'

result = expression_manager(X,bands_order=bands_order,expression=expression)

print(result)

##############################################################################
# Plot result
#
from matplotlib import pyplot as plt
from datetime import datetime
dateToDatetime = [datetime.strptime(str(date),'%Y%m%d') for date in dates]
plt.plot_date(dateToDatetime,result.T[:,:100],'-o')
