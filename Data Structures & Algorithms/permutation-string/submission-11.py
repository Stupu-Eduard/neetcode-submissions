class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = list(s1)
        
        for i,c in enumerate(s2):
            if c in l:
                l.remove(c)

                for j in range(len(s1) - 1):
                    if (i + j + 1 < len(s2)) and s2[i + j + 1] in l:
                        l.remove(s2[i + j + 1])
                    else:
                        l = list(s1)
                        break
                if not l:
                    return True
            else:
                l = list(s1)
        
        return False
