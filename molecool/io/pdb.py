"""
pdb.py

This submodule does stuff with pdb files
"""

import numpy as np

def open_pdb(f_location):
    """
    Opens and reads a PDB files

    Parameters
    ==========
    f_location : string
        The name of the files that is desired to be opened

    Returns
    =======
    symbols : list
        A list containing the atom symbols, names
    coordinates : np.ndarray
        A numpy array containing the coordinates

    Examples
    ========

    >>> open_pdb("thorocene.pdb")
    """
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
