#!/usr/bin/env python

import argparse
from mstest import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)-s: %(message)s')

if __name__ == "__main__":
    helpmsg = "Generate linked residues, clusters, and microstates as a test case for linked residue detection."

    parser = argparse.ArgumentParser(description=helpmsg)
    parser.add_argument("-r", metavar="residues", default=100, help="number of residues, default to 100", type=int)
    parser.add_argument("-i", metavar="ionizable", default=1.0, help="fraction of ionizable residues, default 0.4", type=float)
    parser.add_argument("-c", metavar="clusters", default=4, help="number of clusters, default to 4", type=int)
    parser.add_argument("-l", metavar="linkage", default=1.0, help="linkage strength between residues, default is 1.0", type=float)
    args = parser.parse_args()

    folder="test_case"
    makecase(r=args.r, i=args.i, c=args.c, l=args.l, folder=folder)
