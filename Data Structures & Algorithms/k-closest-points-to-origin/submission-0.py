from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        # calculate distance of each point
        for point in points:
            dist = math.sqrt(((0 - point[0]) ** 2) + ((0 - point[1]) ** 2))
            
            # store points in minHeap with distance like [[distance, (x, y)]]
            heapq.heappush(maxHeap, [-dist, (point[0], point[1])])

            # if len(minHeap) > k, pop an element from the minheap
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        # return all points in the heap
        res = []
        for point in maxHeap:
            res.append(point[1])
        
        return res