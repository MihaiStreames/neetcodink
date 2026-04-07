class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return heapq.nlargest(k, counter, key=counter.get)
