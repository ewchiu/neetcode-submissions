import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap to keep track of the heaviest stones
        # Iterate through the array, adding stones to the min heap
        # in while loop:
        # pop the max heap to remove the largest 2 stones and smash them together
        max_heap = []
        
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) * -1
            stone2 = heapq.heappop(max_heap) * -1

            if stone1 > stone2:
                new_stone = stone1 - stone2
                heapq.heappush(max_heap, -new_stone)

        max_heap.append(0)
        return abs(max_heap[0])
