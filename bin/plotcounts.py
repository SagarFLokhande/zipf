""" Versatile python script to plot Zipf's law for a given csv data file. """

import argparse
import pandas as pd

def main(args):
    """Run the command line program."""
    df = pd.read_csv(args.infile, header = None, names = ("word", "word_frequency") ) 
    df["rank"] = df["word_frequency"].rank(ascending=False, method = 'max')
    df['inverse_rank'] = 1 / df['rank']
    templot = df.plot.scatter(x='word_frequency', y='inverse_rank', figsize=[12,6], grid=True, xlim=args.xlim)
    templot.figure.savefig(args.outfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = __doc__)
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?', default = '-', help= 'Input csv file name')
    parser.add_argument('--outfile', type=str, default='plotcounts.png', help= 'Output image file name.')
    parser.add_argument('--xlim', type=float, nargs=2, metavar=('Xmin', 'Xmax'), default= None, help = 'X-axis limits.' )
    args = parser.parse_args()
    main(args)

