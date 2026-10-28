class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        # fill out adj map
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # track the visited nodes
        visited = set()

        def dfs(crs):
            if crs in visited:
                # cycle detected
                return False

            if preMap[crs] == []:
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

        # each course is a node and each prereq is a directed edge
        # add all courses with indegree = 0 into a q
        # while the q is not empty:
        # remove a course from the q
        # mark it as finished
        # reduce indegree of its dependent courses

