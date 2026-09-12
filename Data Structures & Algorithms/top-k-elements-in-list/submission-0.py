class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = 1 + hash_table.get(num,0)
        sorted_nums = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
        result = []

        for i in range(k):
            result.append(sorted_nums[i][0])
        return result