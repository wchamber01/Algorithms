#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    res = ['rock', 'paper', 'scissors']
    for i in range(res[i]):
        cur_combo = []
        for j in range(len(res)+1):
            cur_combo.append((res[i], res[j]))
    return res[n]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')