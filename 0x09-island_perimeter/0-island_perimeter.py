#!/usr/bin/python3
'''0x09. Island Perimeter'''

def island_perimeter(grid):
    '''Calculate the perimeter of the island described in grid'''
    counter = 0
    grid_max = len(grid) - 1  # Last row index
    lst_max = len(grid[0]) - 1  # Last column index

    for lst_idx, lst in enumerate(grid):
        for land_idx, land in enumerate(lst):
            if land == 1:  # If the current cell is land
                # Check left boundary or adjacent cell
                if land_idx == 0 or lst[land_idx - 1] == 0:
                    counter += 1

                # Check right boundary or adjacent cell
                if land_idx == lst_max or lst[land_idx + 1] == 0:
                    counter += 1

                # Check top boundary or adjacent cell
                if lst_idx == 0 or grid[lst_idx - 1][land_idx] == 0:
                    counter += 1

                # Check bottom boundary or adjacent cell
                if lst_idx == grid_max or grid[lst_idx + 1][land_idx] == 0:
                    counter += 1

    return counter
