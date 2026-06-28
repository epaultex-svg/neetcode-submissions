class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t.isdigit() or (t.startswith('-') and len(t) > 1):
                stack.append(int(t))
            elif t == "+":
                stack[-2] += stack[-1]
                stack.pop()
            elif t == "-":
                stack[-2] -= stack[-1]
                stack.pop()
            elif t == "*":
                stack[-2] *= stack[-1]
                stack.pop()
            elif t == "/":
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
        return stack[0]