class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # fill out indegrees/adj matrix
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # add root nodes to q
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # traverse graph, adding courses with indegrees == 0 to q
        # for each course popped from the q append to output
        output = []
        finish = 0
        while q:
            course = q.popleft()
            output.append(course)
            finish += 1
            for adj_course in adj[course]:
                indegree[adj_course] -= 1
                if indegree[adj_course] == 0:
                    q.append(adj_course)

        if finish != numCourses:
            return []
        return output[::-1]