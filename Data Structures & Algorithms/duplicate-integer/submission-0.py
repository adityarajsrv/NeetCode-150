class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        for key, value in freq.items():
            if value > 1:
                return True
        return False