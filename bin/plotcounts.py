""" Versatile python script to plot Zipf's law for a given csv data file. """

import argparse
import pandas as pd
import numpy as np
import scipy
from scipy.optimize import minimize_scalar
#.minimize_scalar as min_scal


def nlog_likelihood(beta, counts):
    """Log-likelihood function."""
    likelihood = - np.sum ( np.log( (1/counts)**(beta-1) - 1/(counts+1) ** (beta-1) ) ) 
    return likelihood


def get_power_law_params(word_counts):
    """Get the power law parameters."""
    mle = minimize_scalar( nlog_likelihood, bracket=(1+1e-10,4), args=word_counts, method = 'brent' ) 
    beta= mle.x
    alpha = 1 / (beta - 1)
    return alpha


def plot_fit( curve_xmin, curve_xmax, max_rank, alpha, ax ):
    """ Plot the power law curve that was fitted to the data. 
    Parameters:
    curve_xmin : float
        minimum x-bound for fitted curve
    curve_xmax : float
        maximum x-bound for fitted curve
    max_rank = int
        maximum word frequency rank
    alpha : float
        estimated alpha parameter for the power law.
    ax : matplotlib axes
        scatter plot to which the power curve will be added."""

    xvals = np.arange( curve_xmin, curve_xmax )
    yvals = max_rank * (xvals ** (-1/alpha) )
    ax.loglog ( xvals, yvals, color = 'grey' ) 


def main(args):
    """Run the command line program."""
    df = pd.read_csv(args.infile, header = None, names = ("word", "word_frequency") ) 
    df["rank"] = df["word_frequency"].rank(ascending=False, method = 'max')
    df['inverse_rank'] = 1 / df['rank']
    ax = df.plot.scatter(x='word_frequency', y='rank', loglog=True, figsize=[12,6], grid=True, xlim=args.xlim)
    word_counts = df[ 'word_frequency' ].to_numpy()
    alpha = get_power_law_params(word_counts) 
    print('alpha', alpha)

    # Since the ranks are already sorted, we can take the last one instead of computing which row has the highest rank.
    max_rank = df[ 'rank' ].to_numpy()[-1]

    # Use the range of the data as the boundaries when drawing the power law curve
    curve_xmin = df[ 'word_frequency' ].min()
    curve_xmax = df[ 'word_frequency' ].max()

    plot_fit( curve_xmin, curve_xmax, max_rank, alpha, ax )
    ax.figure.savefig(args.outfile)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default = '-', help= 'Input csv file name')
    parser.add_argument('--outfile', type=str, default='plotcounts.png', help= 'Output image file name.')
    parser.add_argument('--xlim', type=float, nargs=2, metavar=('Xmin', 'Xmax'), default= None, help = 'X-axis limits.' )
    args = parser.parse_args()
    main(args)

