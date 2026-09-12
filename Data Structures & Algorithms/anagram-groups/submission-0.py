class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for i, string in enumerate(strs):
            hash_freq = {}
            for s in string:
                hash_freq[s] = 1 + hash_freq.get(s, 0)
            key = tuple(sorted(hash_freq.items()))
        
            if key not in result:
                result[key] = []
            result[key].append(string)

        return list(result.values())