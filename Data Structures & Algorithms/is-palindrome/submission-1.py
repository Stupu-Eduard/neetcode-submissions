class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s)
        l = list(s)

        
        left = 0
        right = len(l) - 1
        res = True

        while left < right:
            if not l[left].isalnum():
                 left += 1
                 continue

            if not l[right].isalnum():
                 right -= 1
                 continue
            
            if l[left].lower() != l[right].lower():
                print(l[left], l[right])
                return False
            
            left += 1
            right -= 1

        return True 
            