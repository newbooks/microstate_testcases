#!/usr/bin/env python
import random

N = 100000

# Residue R1, R2, R3, R4, R5, R6, R7, R8
# R1 is on a constant conformer
#   10
# R2 and R3 concerted flips, 1 on 1, flip between individuals:
#   20 - 30
#   21 - 31
#   22 - 32
#   23 - 33
# R4 and R5 have concerted flips, 2 to 2, flip between groups:
#   40, 41 - 50, 51
#   42, 43 - 52, 53
# R6 and R7 have partially concerted flips:
#   60 - 70
#   61, 62, 63 - 71, 72, 73
# R8 flips randomly
#   80, 81, 82, 83

LINKING_RULES = {20: [30],
                 21: [31],
                 22: [32],
                 23: [33],
                 30: [20],
                 31: [21],
                 32: [22],
                 33: [23],
                 40: [50, 51],
                 41: [50, 51],
                 42: [52, 53],
                 43: [52, 53],
                 50: [40, 41],
                 51: [40, 41],
                 52: [42, 43],
                 53: [42, 43],
                 60: [70],
                 61: [71, 72, 73],
                 62: [71, 72, 73],
                 63: [71, 72, 73],
                 70: [60],
                 71: [61, 62, 63],
                 72: [61, 62, 63],
                 73: [61, 62, 63]
                 }


class Residue:
    def __init__(self):
        self.confs = []
        self.name = ""


if __name__ == "__main__":
    residues = []

    # residue 1
    res = Residue()
    res.name = "R1"
    res.confs.append(10)
    residues.append(res)

    # residue 2 to 8
    for ir in range(2, 9):
        res = Residue()
        res.name = "R%d" % ir
        for i in range(4):
            res.confs.append(10*ir+i)
        residues.append(res)


    # initial state
    state = []
    # res 1
    state.append(residues[0].confs[0])
    # res 2
    state.append(random.choice(residues[1].confs))
    # res 3
    state.append(random.choice(LINKING_RULES[state[1]]))
    # res 4
    state.append(random.choice(residues[3].confs))
    # res 5
    state.append(random.choice(LINKING_RULES[state[3]]))
    # res 6
    state.append(random.choice(residues[5].confs))
    # res 7
    state.append(random.choice(LINKING_RULES[state[5]]))
    # res 8
    state.append(random.choice(residues[7].confs))

    flippable = range(2, 9)
    for i in range(N):
        site = random.choice(flippable)
        new_conf = state[site-1]
        while new_conf == state[site-1]:
            new_conf = random.choice(residues[site-1].confs)

        if new_conf in LINKING_RULES:
            new_conf2 = random.choice(LINKING_RULES[new_conf])
            site2 = int(new_conf2/10)
            state[site-1] = new_conf
            state[site2-1] = new_conf2
        else:
            state[site-1] = new_conf


        print("%s" % " ".join(["%d" % x for x in state]))