#!/usr/bin/env python

import os

pw = 2.0  # base interaction in kt

class Prot:
    def __init__(self):
        self.residues = []
        return



def makecase(r=100, i=0.4, c=4, l=1.0, folder="./"):
    residues = r
    ionizable_residues = int(r * i)
    positive_residues = int(ionizable_residues/2)
    negative_residues = ionizable_residues - positive_residues
    clusters = c
    pairwise = pw * l


    # create and enter a folder
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    prot = Prot()
    for i in range(len(residues)):

        prot.residues

    # exit folder
    os.chdir("../")
    return