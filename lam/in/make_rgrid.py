#!/usr/bin/env python3

# Read and store 'header' file, which contains the text
# that will be in the header of the initial guess file.
rgrid = open('header','r')
guess = rgrid.readlines()
rgrid.close()

# from header, get mesh size and store in 'grid'
grid = list(map(int,guess[14].split())) 

# template line for initial guess file
line = '    {:.9f}    {:.9f}\n'

# loop through gridpoints, determine the composition at
# each gridpoint, and store compositions in 'guess'
for i in range(grid[0]):
  if i < (grid[0] / 4) or i >= (grid[0] * 3 / 4):
    guess.append(line.format(0.9,0.1))
  else:
    guess.append(line.format(0.1,0.9))

rgrid = open('c.rf','w')
rgrid.writelines(guess)
rgrid.close()
