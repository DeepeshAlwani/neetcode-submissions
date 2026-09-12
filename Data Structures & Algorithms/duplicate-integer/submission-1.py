class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i,num in enumerate(nums):
            if num in hash_table:
                return True
            hash_table[num] = i

        print(hash_table)
            
        return False