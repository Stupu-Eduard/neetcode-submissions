class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []
        word = ""
        
        for s in strs:
            encoded_str.append(f"{len(s)}#{s}")

        return "".join(encoded_str)



    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1
            
            leng = int(s[i:j])
            word = s[j + 1:j + 1 + leng]

            decoded_str.append(word)
            i = j + 1 + leng
        return decoded_str
