class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS
        # 1. fill out adj map

        # for each course, run DFS

        # each course is a node and each prereq is a directed edge
        # indegree is number of prereqs for each course
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dest in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1

        # add all courses with indegree = 0 into a q
        # these courses have no prereqs
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0

        # while the q is not empty:
        while q:
            # remove a course from the q
            course = q.popleft()
            
            # mark it as finished
            finish += 1
            # reduce indegree of its dependent courses
            for dep in adj[course]:
                indegree[dep] -= 1

                if indegree[dep] == 0:
                    q.append(dep)

        return finish == numCourses