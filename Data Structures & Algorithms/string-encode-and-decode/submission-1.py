class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(s)
            res.append("#.#")
        
        return "".join(map(str,res))


    def decode(self, s: str) -> List[str]:
        res = []
        l = s.split("#.#")[:-1]
        return l
