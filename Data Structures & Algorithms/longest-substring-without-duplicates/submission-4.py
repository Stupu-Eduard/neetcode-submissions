class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = []
        dup, current, maxl = 0, 0, 0

        for i in range(len(s)):
            if s[i] in visited:
                dupi = visited.index(s[i])
                visited = visited[dupi + 1:]
                visited.append(s[i])
                maxl = max(maxl,current)
                current = len(visited)
            else:
                current += 1
                visited.append(s[i])
            
        return max(maxl,current)