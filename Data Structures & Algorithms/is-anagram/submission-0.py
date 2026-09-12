class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table1 = {}
        hash_table2 = {}
        if len(s) != len(t):
            return False
        for i, alpha in enumerate(s):
            hash_table1[alpha] = 1 + hash_table1.get(alpha, 0)
            hash_table2[t[i]] = 1 + hash_table2.get(t[i], 0)


        return hash_table1 == hash_table2
        