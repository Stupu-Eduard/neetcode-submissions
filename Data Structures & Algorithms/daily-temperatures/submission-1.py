class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        d = {}
        k = len(temperatures) - 1

        res = list(range(k + 1))
        res[k] = 0

        for i in range(k - 1,-1,-1):
            cp = i + 1
            while temperatures[i] >= temperatures[cp] and res[cp] != 0: 
                cp += 1
            
            if temperatures[i] < temperatures[cp]:
                res[i] = cp - i
            else:
                res[i] = 0
        
        return res

            


