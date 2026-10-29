from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for tok in tokens:
            if tok in {"+","-","*","/"}:
                a = stack.pop()
                b = stack.pop()
                if tok == "+":
                    stack.append(a+b)
                if tok == "-":
                    stack.append(b-a)
                if tok == "*":
                    stack.append(a*b)
                if tok == "/":
                    stack.append(int(b/a))
            else:
                stack.append(int(tok))
        return stack[-1]
