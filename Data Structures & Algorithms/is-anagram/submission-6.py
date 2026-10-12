class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counters = {}
        countert = {}

        for cs in s:
            counters[cs] = counters.get(cs,0) + 1
        for ct in t:
            countert[ct] = countert.get(ct,0) + 1

        if countert == counters:
            return True
        return False
