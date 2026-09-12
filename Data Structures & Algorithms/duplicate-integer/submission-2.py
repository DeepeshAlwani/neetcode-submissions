class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = {}
        for i, num in enumerate(nums):
            if num in hash_set:
                return True
            hash_set[num] = i
        
        return False