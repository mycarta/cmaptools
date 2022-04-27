# coding: utf-8
# Author: Matteo Niccoli
# Email: matteo@mycarta.ca
# License: LGPL

# A collections of functions to enable evaluation and fixing of bad colormaps

import numpy as np
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def sqcbar(cmap):
    """
    Create a square RGB array from a matplotlib user-selected colormap
    The output can be sued to plot a square colorbar
   
    Args:
        cmap (string): matplotlib colormap
        
    Returns:
       rgb_colormap (array): a square rgb array that can be plotted as 
        
    Examples: 
    >>> cmap = 'afmhot'
    >>> rgb_colormap = sqcbar(sqmap)
    >>> rgb_colormap.shape
    (256, 256, 3)
    
    Example of plotting:
    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.imshow(rgb_colormap);
    
    """
   
    if not cmap:
        raise ValueError('please pass a colormap string')
    
    if not cmap in plt.colormaps():
        raise ValueError('please use a matplotlib colormap \n'
    'The full list can be printed by running matplotlib.pyplot.colormaps()')
    
    
    sp=np.arange(256)
    my_cmap = cm.get_cmap(cmap) 
    normsp = clr.Normalize(0, 256) 
    colsp = my_cmap(normsp(sp))
    rsp = np.tile(colsp[:,0], (256,1))
    gsp = np.tile(colsp[:,1], (256,1))
    bsp = np.tile(colsp[:,2], (256,1))
    rgb_cl=np.array(list(zip(rsp, gsp ,bsp)))
    rgb_colormap=np.swapaxes(rgb_cl,1,2)
    return rgb_colormap