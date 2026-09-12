class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_table = {}
        for i, num in enumerate(nums):
            val = target - num
            if val in hash_table:
                return [hash_table[val],i]
            
            hash_table[num] = i
        