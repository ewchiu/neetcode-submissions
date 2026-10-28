class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num in freq_map.keys():
            heapq.heappush(heap, (freq_map[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
