#
#   SOLVED
#
import numpy as np
from typing import List


class Solution:
    def parent(label:int) -> int:
        # find out in which row you are.
        row = int(np.log2(label))
        # how many steps to first in that row
        counter = label - 2**row
        parent = label - (counter + int(counter / 2) + 1)
        return parent

    def pathInZigZagTree(label: int) -> List[int]:
        # make it recursive
        sol = []
        while True:
            sol.append(label)
            print(sol)
            if label > 1:
                label = Solution.parent(label)
            else:
                break
        return sol[::-1]


if __name__ == '__main__':
    print(Solution.pathInZigZagTree(label=1))
