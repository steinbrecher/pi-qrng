###############################################################################
# # 
# # File Name: select_winner.py
# # 
# # Current owner: Greg Steinbrecher (steinbrecher@alum.mit.edu)
# # Last Modified Time-stamp: <2015-02-11 06:46:58 gstein>
# # 
# # Created by: Greg Steinbrecher (steinbrecher@alum.mit.edu)
# # Created on: 2015-02-08 (Sunday, February 8th, 2015)
# # 
###############################################################################

import numpy as np

numContestants = 235

# Load in the key generated from QKD system
# These are uniformly distributed from 0-255
randomNumbers = np.genfromtxt('key.txt', dtype='int64')

# Trim to number of contestants
randomNumbers = randomNumbers[:numContestants]

# Convert to strings and zero-pad
randomStrings = ["{:03d}".format(x) for x in randomNumbers]

# Load first million digits of pi 
# Trimmed from https://stuff.mit.edu/afs/sipb/contrib/pi/pi-billion.txt
with open('pi.txt', 'rb') as f:
    pi = f.readline()

offsets = np.array([pi.index(s) for s in randomStrings])

# Find 2012
index2012 = pi.index('2012')

# Find minimum
print "Winner Index: {:d}".format(np.abs(offsets - index2012).argmin())
    


