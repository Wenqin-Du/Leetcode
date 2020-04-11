
class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visit = [0] * numCourses
        courseNeighbor = [[] for _ in range(numCourses)]
        # Do not use [[]] * numCourses here!
        # it will end up in identical list in a list

        for x, y in prerequisites:
            courseNeighbor[x].append(y)

        for i in range(numCourses):
            if not self.dfs(courseNeighbor, visit, i):
                return False
        return True


    def dfs(self, L, visit, i):

        if visit[i] == -1: return False
        if visit[i] == 1: return True

        visit[i] = -1
        for j in L[i]:
            if not self.dfs(L, visit, j):
                return False
        visit[i] = 1

        return True
