#!/usr/bin/env python
from argparse import (ArgumentParser, FileType)

def parse_args():
    "Parse the input arguments, use '-h' for help"
    parser = ArgumentParser(description='Convert Tandem Repeat Finder (TRF) dat file to space delimited txt format with header line appropriate for parsing with R')
    parser.add_argument(
        '--dat', type=str, required=True,
        help='Input dat file produced by Tandem Repeat Finder (TRF) using the -d option')
    parser.add_argument(
        '--txt', type=str, required=True,
        help='Output txt file.')

    return parser.parse_args() 

### Main
def main():
    # Parse command line arguments
    args = parse_args()
    datfile = args.dat
    txtfile = args.txt

    with open(txtfile, 'w') as txt:
        txt.write('Contig StartPos EndPos PeriodSize CopyNumber ConsensusSize PercentMatches PercentIndels Score A C G T Entropy(0-2) Motif Sequence\n')

        chrom = ""
        with open(datfile, 'r') as dat:
            for line in dat:
                splitline = line.split()
                if line.startswith("Sequence:"):
                    chrom = line.split()[1]
                else:
                    # Catch index errors when line is blank
                    try:
                        # Check if in header sequence (all non-header lines start with an int: start pos)
                        try:
                            int(splitline[0])
                        except ValueError:
                            continue
                        txt.write(chrom + ' ' + line)
                    except IndexError:
                        pass

if __name__ == '__main__':
    main()
