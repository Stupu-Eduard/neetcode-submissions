class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        substr = ""

        for c in s:
            if c in substr:
                max_length = max(max_length,len(substr))

                index = substr.index(c) + 1
                substr = substr[index:]
            
            substr += c

        max_length = max(max_length,len(substr))
        return max_length