import numpy as np

def despike(pixel, doys, thresh = 0.05, nodata = 0):
    """
    Iteratively despike a timeseries using linear interpolation and taking the upper envelope.
    
    Parameters
    ----------
    pixel : array
        The Timeseries' y-values
    doys : array
        Day of year, ie The timeseries' x-values
    thresh : float
        The despiking threshold. Spikes are defined as points on the timeseries
        which differ from their interpolation by more than this value.
    nodata : float
        NoData value, will be removed from timeseries
   Returns
   -------
   pixel2 : array
       Updated and despiked timeseries y-values
   Doys2 : array
       Updated timeseries x-values (nodata and NaN values removed)
        
        
    """
    valid_inds = np.where((pixel != nodata) & np.isfinite(pixel))  # find valid indices (not NaN not nodata)
    doys2 = doys[valid_inds]  # remove invalid data
    pixel2 = pixel[valid_inds]  # remove invalid data
    iterations = 0
    max_dif = 100
    
    while max_dif > thresh and iterations < 100:
        # create left and right verisons of arrays:
        y1 = np.roll(pixel2, -1)
        y2 = np.roll(pixel2, 1)
        x1 = np.roll(doys2, -1)
        x2 = np.roll(doys2, 1)
        x1[0], y1[0], x2[-1], y2[-1] = doys2[0], pixel2[0], doys2[-1], pixel2[-1]  # handle edges
        interp = ((y2-y1)/(x2-x1))*(doys2 - x1)+y1  # caluculate neighbour interpolation for each point        
        interp[0], interp[-1] = np.mean(pixel2[1:3]), np.mean(pixel2[-3:-1])  # set edges of interpolation as mean of closest 2 points
        diff = interp- pixel2   # difference between value and interpolation
        max_dif = np.max(diff)
        # remove spike if over thresh:
        if max_dif > thresh:
            bigspike = np.argmax(diff)
            pixel2[bigspike] = interp[bigspike]
        iterations +=1
    return pixel2, doys2
  
  
