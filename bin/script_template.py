"""Brief description of what the script does."""

import argparse

def userfunc(args):
    print("Input File", args.infile)
    print("Output File", args.outfile)

def double(num):
    "Double the input."
    return 2*num


if __name__ == "__main__":
    USAGE = "Brief description of what the script does."
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("outfile", type=str, help="Output file name")
    args = parser.parse_args()
    userfunc(args)

print("double(3) = ", double(3))