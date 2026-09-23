class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = list(s.replace(" ", ""))
        res = list(char.lower() for char in res)
        left = 0
        right = len(res) - 1

        while left < right:

            # Check if both res[left] and res[right] are alphanumerical characters
            if not res[left].isalnum():
                left +=1
                continue
            if not res[right].isalnum():
                right -=1
                continue
            

            if res[left] != res[right]:
                print(res[right] + res[left])
                return False

            left +=1
            right -=1

        return True
                
