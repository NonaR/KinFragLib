"""
Contains plotting functionalities for different filters.
"""
import matplotlib.pyplot as plt
from matplotlib import gridspec
import statistics

def make_hists(values_list, fragment_library, filtername = None, plot_stats = True, cutoff = None):
    """
    Creates a histogram for each subpocket.
    
    Parameters
    ----------
    values_list : pandas.Series
        smiles series containing fragment smiles strings

    fragment_library : dict of pandas.DataFrame
        Fragment details, i.e. SMILES, and fragment RDKit molecules, KLIFS and fragmentation details (values)
        for each subpocket (key).

    filtername : str
        name of the filter creating the values plottet

    cutoff : int or float
    """
    #get even number if number of plots not even
    num_plots = round(len(values_list)+0.5)
    fig = plt.figure(figsize=(20, 22))
    gs = gridspec.GridSpec(int(num_plots/2),int(num_plots/2))
    keys = list(fragment_library.keys())
    for i in range(0, 2):
        for j in range(0, int((num_plots)/2)):
            if (i*4)+j < num_plots:
                ax = plt.subplot(gs[i,j])
                ax.hist(values_list[((i*4)+j)], facecolor = '#04D8B2', edgecolor='#808080')
                ax.set_title(keys[((i*4)+j)])
                if plot_stats:
                    plt.plot([], [], ' ', label="mean: "+str(round(statistics.mean(values_list[((i*4)+j)]))))
                    plt.plot([], [], ' ', label="min: "+str(round(min(values_list[((i*4)+j)]))))
                    plt.plot([], [], ' ', label="max: "+str(round(max(values_list[((i*4)+j)]))))
                    plt.legend()
                if not cutoff is None:
                    plt.axvline(x=cutoff, color='r', linestyle='-')
                if not filtername is None:
                    plt.xlabel(filtername)
                plt.ylabel("Number of fragments")         
    plt.suptitle(filtername)