class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        # build indegree arr for each course
        # add edges to adj arr
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = collections.deque()
        # add all indegree == 0 to q, that means no dependencies
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0, []
        # BFS
        while q:
            # pop q, inc finish and append to output
            course = q.popleft()
            output.append(course)
            finish += 1

            # go through indegrees and dec dependencies
            # if indegree = 0 add to q as it has no more dependencies
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish != numCourses:
            return []

        return output[::-1]