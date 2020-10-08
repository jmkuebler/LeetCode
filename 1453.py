from typing import List
import numpy as np

class Solution:
    def numPoints(self, points: List[List[int]], r: int) -> int:
        # brute force by hint 1: Use a combinatorial approach. Since for the optimal solution two points are on the
        # circle, we can construct the center for each pair of two points and compute how many other points lie within
        # Scaling: n^2 * n = n^3 (for each pait of points we need to construct the circle and check how many other
        # points lie within
        n = len(points)
        points = np.array(points)
        max_points = 0
        for i in range(n):
            a = points[i]
            for j in range(n):
                b = points[j]
                dist = np.linalg.norm(a - b)
                if dist > 2 * r:
                    # no circle that includes both points
                    darts = 1
                    if darts > max_points:
                        max_points = darts
                    continue
                for sign in [+1, -1]:
                    if all(a == b):
                        center = a
                    else:
                        middle = 1/2 *(a+b)
                        cath_len = np.sqrt(r**2 - dist**2/4)   # r^2 = (dist/2)^2 + cathetus^2
                        cath_direction = a-b
                        cath_direction[0] = -cath_direction[1]
                        cath_direction[1] = (a-b)[0]
                        cath_direction = cath_direction / np.linalg.norm(cath_direction)

                        center = middle + sign * cath_len * cath_direction
                    darts = 0
                    for k in range(n):
                        if np.linalg.norm(points[k]-center) <= r:
                            darts += 1
                    if darts > max_points:
                        max_points = darts
        return max_points

if __name__ == '__main__':
    # print(Solution.numPoints(self=None, points=[[-3,0],[3,0],[0,2],[0,-2]], r=2))
    print(Solution.numPoints(self=None, points=[[-6, 15], [-22, -15], [-15, -34], [-11, 8], [-30, 33], [-26, -1], [15, -35], [-1, -34], [-14, 20], [28, -28],
     [24, 18], [-36, 28], [24, -28], [-14, -3], [21, 5], [38, 17], [-24, -16], [-4, -7], [25, -9], [-9, 36], [-16, -26],
     [5, 35], [36, 19], [-16, -35], [37, 25], [12, -33], [-8, 12], [-24, -15], [36, -21], [7, 9], [19, 31], [15, 24],
     [-17, -9], [-29, 33], [25, -38], [-39, -24]], r=33))