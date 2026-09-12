class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hash_table = {}
        for i, num in enumerate(numbers):
            val = target - num

            if val in hash_table:
                return [hash_table[val] + 1 , i + 1]
            
            hash_table[num] = i

        
        