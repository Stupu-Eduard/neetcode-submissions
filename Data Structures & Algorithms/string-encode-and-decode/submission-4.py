class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            res.append(str(len(word)))
            res.append('#')
            res.append(word) 
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':      
                j += 1
            l = int(s[i:j])          

            word = []
            for k in range(l):
                word.append(s[j + 1 + k])   

            res.append(''.join(word))
            i = j + 1 + l            
        return res