# https://leetcode.cn/problems/spiral-matrix/description/
# 进行模拟即可，注意判断语句，在while内，每次判断要看res是不是满了，此外，注意索引问题
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m, n = len(matrix), len(matrix[0])
        left, down = 0, 0
        right, up = n-1, m-1
        while len(res) < m*n:
            if left <= right and len(res) < m * n:
                for i in range(left, right+1):
                    res.append(matrix[down][i])
                down += 1
            if down <= up and len(res) < m * n:
                for i in range(down, up+1):
                    res.append(matrix[i][right])
                right -= 1
            if left <= right and len(res) < m * n:
                for i in range(right, left-1, -1):
                    res.append(matrix[up][i])
                up -= 1
            if down <= up and len(res) < m * n:
                for i in range(up, down-1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res