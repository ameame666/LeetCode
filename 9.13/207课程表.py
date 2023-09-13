# https://leetcode.cn/problems/course-schedule/
# 转化为图是否有环问题，dfs解决，建立两个数组，一个判断该点是否被访问过，另一个用来回溯确定是否有环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def buildgraph(numCourses, prerequisites):
            graph = [[] for _ in range(numCourses)]
            for x, y in prerequisites:
                graph[y].append(x)
            return graph
        
        graph = buildgraph(numCourses, prerequisites)
        onpath = [False] * numCourses
        visited = [False] * numCourses
        hascycle = [False]

        def dfs(i):
            if onpath[i]:
                hascycle[0] = True
                return
            if visited[i] or hascycle[0]:
                return
            onpath[i] = True
            visited[i] = True
            for s in graph[i]:
                dfs(s)
            onpath[i] = False
        
        for i in range(numCourses):
            if not visited[i] and not hascycle[0]:
                dfs(i)
        
        return not hascycle[0]

# bfs解法