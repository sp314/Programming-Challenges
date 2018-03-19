'''
Input:
The input consists of a single integer aa (1≤a≤10181≤a≤1018), the area in square meters of Old MacDonald’s pasture.

Output:
Output the total length of fence needed for the pasture, in meters.
The length should be accurate to an absolute or relative error of at most 10−610−6.
'''
import math

def fenceNeeded():
    area = int(input())
    return 4*math.sqrt(area)

print(fenceNeeded())