class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seen = []
        add, sub, mul, div = '+', '-', '*', '/'
        for token in tokens:
            if token not in add and token not in sub and token not in mul and token not in div:
                seen.append(int(token))
            else: 
                b = seen.pop()
                a = seen.pop()

                if token == add:
                    seen.append(a + b)
                elif token == sub:
                    seen.append(a - b)
                elif token == mul:
                    seen.append(a * b)
                elif token == div:
                    seen.append(int(a / b))
        return seen[0] # last val == result