class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create indegree arr
        indegree = [0] * numCourses
        # create adj matrix
        adj = [[] for _ in range(numCourses)]
        # go through prereqs and add relationships to arrs
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # start q for bfs, add courses with 0 dependencies to q
        q = collections.deque()
        for course in range(len(indegree)):
            if indegree[course] == 0:
                q.append(course)

        # while q: pop courses and remove indegrees from arr
        finish = 0
        output = []
        while q:
            course = q.popleft()
            output.append(course)
            finish += 1

            for next in adj[course]:
                indegree[next] -= 1

                # if indegrees = 0 add to q
                if indegree[next] == 0:
                    q.append(next)

        if finish != numCourses:
            return []

        return output[::-1]
