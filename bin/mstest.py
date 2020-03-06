#!/usr/bin/env python

import os
import random

pw_base = 2.0  # base interaction in kt
bgsigma = 0.2

class Conformer:
    def __init__(self):
        self.name = ""
        self.index = 0
        self.crg = 0.0
        self.selfE =  random.gauss(0.0, bgsigma)
        return

class Residue:
    def __init__(self):
        self.seq = 0
        self.name = "R"
        self.crg = 0
        self.sign = "0"
        self.conf = []
        return

    def load_conf(self):
        n = 6
        if self.sign == "0":
            for i in range(n):
                conf = Conformer()
                conf.name = "%s0A%03d_%02d" % (self.name, self.seq, i)
                self.conf.append(conf)
        else:
            hn = int(n/2)
            for i in range(hn, n):
                conf = Conformer()
                conf.crg = self.crg
                conf.name = "%s%sA%03d_%02d" % (self.name, self.sign, self.seq, i)
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


def makecase(r=100, i=0.4, c=4, s=4, l=1.0, folder="./"):
    residues = r
    pairwise = pw_base * l


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
            res.sign = "+"
        else:
            res.crg = -1
            res.sign = "-"

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

    # make conformers
    for res in prot.residues:
        res.load_conf()

    # make pairwise interaction
    conformers = []
    counter = 0
    for res in prot.residues:
        for conf in res.conf:
            conf.index = counter
            counter += 1
            conformers.append(conf)

    pw = [[random.gauss(0.0, bgsigma) for j in range(len(conformers))] for k in range(len(conformers))]
    for cluster in clusters:
        cluster = list(cluster)
        for j in range(len(cluster)-1):
            for conf1 in cluster[j].conf:
                for conf2 in cluster[j+1].conf:
                    pw[conf1.index][conf2.index] = pw[conf2.index][conf1.index] = conf1.crg * conf2.crg * pairwise


    prot.print_headlst()
    # print energies
    folder = "energies"
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    for conf in conformers:
        fname = "%s.opp" % conf.name
        lines = []
        
        open(fname, "w").writelines(lines)

    # exit folder
    os.chdir("../")

    return