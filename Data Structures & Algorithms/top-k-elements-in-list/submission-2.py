class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = []
        res = []

        for key in freq_map:
            heapq.heappush(min_heap, (freq_map[key], key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])

        return res