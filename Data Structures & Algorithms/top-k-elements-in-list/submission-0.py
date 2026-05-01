class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for i in nums:
            freqMap[i] = freqMap.get(i, 0) + 1

        buckets = [[] for _ in range(len(nums)+1)]

        for num, count in freqMap.items():
            buckets[count].append(num)

        result = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result