class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = 0
        left = 0
        right = 1
        buffer_string = ""
        for right in range(len(s)):

            while s[right] in buffer_string:
                buffer_string = buffer_string[1:]
                left += 1

            buffer_string += s[right]

            longest_string = max(longest_string, len(buffer_string))

        return longest_string
                

        