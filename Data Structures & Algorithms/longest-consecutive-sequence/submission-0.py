class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0
        for i, num in enumerate(nums):
            if num-1 not in cache:
                current = num
                length = 1
                while current + 1 in cache:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest
        