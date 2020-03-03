# Microstate Test Cases

## Purpose

This program is part of MCCE testing tools. It will generate residues, some of which are linked, 
and their microstate output.

These test cases help to see if your analysis tool is able to correctly identify linked residues from microstates.  

## What test cases are produced in this program

### Smallest case
5 residues

### Realistic case
You can define:

* total residues: default is 100
* % ionizable: default is 40%
* number of clusters: default is 4
* average cluster size: 4
* linkage strength of the cluster members: default is 100%

## Usage
generate_mstests.py [-r residues] [-i ionizable] [-c clusters] [-s cluster_size] [-l linkage]

-r residues: number of residues (default 100)

-i ionizable: ionization residue rate (default 0.4)

-c clusters: number of clusters (default 4)

-s cluster_size: average cluster size (default 4)

-l linkage: linkage strength of the cluster members (default is 1)


## Output

### Residues


Residue type:

* R+: can have 0 and +1 charge
* R-: can have 0 and -1 charge
* R0: 0 charge



### Clusters

Linked residues have strong interactions and flip conformers in a synchronized way. A group of linked residues form a
 cluster.

### Microstates analytical
A list of microstates, their energy and probability.

### Microstates Monte Carlo
A list of microstates, their energy and occupancy.


### Test cases included
minimum_case

realistic_case

