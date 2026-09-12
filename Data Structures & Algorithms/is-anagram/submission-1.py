class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}
        if len(s) != len(t):
            return False
        for i, so in enumerate(s):
            hash_map1[so] = hash_map1.get(so, 0) + 1
            hash_map2[t[i]] = hash_map2.get(t[i], 0) + 1
        
        return hash_map1 == hash_map2