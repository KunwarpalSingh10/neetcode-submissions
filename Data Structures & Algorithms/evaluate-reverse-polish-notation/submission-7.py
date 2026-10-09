class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        out = 0
        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    out = num1 + num2
                elif t == "-":
                    out = num1 - num2
                elif t == "*":
                    out = num1 * num2
                else:
                    out = int(num1 / num2)
                stack.append(out)
            else:
                stack.append(int(t))
        return stack[-1]