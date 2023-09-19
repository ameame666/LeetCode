# https://leetcode.cn/problems/gas-station/description/
# 把路程看作一个环形数组，选取最低点作为开始点

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s, minsum, start = 0, 0, 0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            if s < minsum:
            # 满足条件表明油量到达新低，记录最小油量
                start = i + 1
                minsum = s
        if s < 0:
        # 如果最后的油量和减去花费小于0证明不管怎么都跑不完
            return -1
        # 
        return 0 if start == len(gas) else start