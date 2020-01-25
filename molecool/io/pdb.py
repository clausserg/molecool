"""
pdb.py

This submodule does stuff with pdb files
"""

import numpy as np

def open_pdb(f_location):
    # This function reads in a pdb file and returns the atom names and coordinates.
    with open(f_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symmbols.append(line[76:79].strip())
            atom_coordinates = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coordinates)

    # Convert list to numpy array
    coordinates = np.array(coordinates)

    return symbols, coordinates
