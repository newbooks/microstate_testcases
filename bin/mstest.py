#!/usr/bin/env python

import os
import random

pw = 2.0  # base interaction in kt
bgmax = 0.25

class Conformer:
    def __init__(self):
        self.name = ""
        self.crg = 0.0
        self.selfE = 0.0
        return

class Residue:
    def __init__(self):
        self.seq = 0
        self.name = "R"
        self.crg = 0
        self.conf = []
        return

    def load_conf(self):
        n = 6
        if abs(self.crg)< 0.001:
            for i in range(n):
                conf = Conformer()
                conf.name = "%s0A%03d_%02d" % (self.name, self.seq, i)
                self.conf.append(conf)
        else:
            hn = int(n/2)
            for i in range(hn):
                conf = Conformer()
                conf.name = "%s0A%03d_%02d" % (self.name, self.seq, i)
                self.conf.append(conf)
            for i in range(hn, n):
                conf = Conformer()
                conf.crg = self.crg
                if self.crg > 0.5:
                    conf.name = "%s+A%03d_%02d" % (self.name, self.seq, i)
                else:
                    conf.name = "%s-A%03d_%02d" % (self.name, self.seq, i)
                self.conf.append(conf)

        return


class Prot:
    def __init__(self):
        self.residues = []
        return

    def print_headlst(self):
        counter = 0
        lines = []
        lines.append("iConf  CONFORMER    crg     selfE\n")
        for res in self.residues:
            for conf in res.conf:
                counter += 1
                lines.append(("%05d  %s   %6.3f  %6.3f\n" % (counter, conf.name, conf.crg, conf.selfE)))
        open("head3.lst", "w").writelines(lines)

    def load_bgenergy(self):
        # background self energy
        for res in self.residues:
            for conf in res.conf:
                conf.selfE = random.uniform(-bgmax, bgmax)

        # background pairwise energy


def makecase(r=100, i=0.4, c=4, s=4, l=1.0, folder="./"):
    residues = r
    pairwise = pw * l


    # create and enter a folder
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    prot = Prot()
    for j in range(residues):
        res = Residue()
        res.seq = j+1
        prot.residues.append(res)

    # make charged residues
    n_charged = int(r * i)
    if n_charged > r:
        n_charged = r

    charged_residues = random.sample(prot.residues, n_charged)


    for res in charged_residues:
        t = random.randint(0,1)
        if t:
            res.crg = 1
        else:
            res.crg = -1

    # make clusters
    charged_residues = set(charged_residues)
    clusters = []
    for j in range(c):

        if s<=len(charged_residues):
            size = s
        else:
            size = len(charged_residues)
        cluster = set(random.sample(charged_residues, size))
        charged_residues -= cluster
        if cluster:
            clusters.append(cluster)

    # make confomers
    for res in prot.residues:
        res.load_conf()


    prot.print_headlst()

    # exit folder
    os.chdir("../")

    return