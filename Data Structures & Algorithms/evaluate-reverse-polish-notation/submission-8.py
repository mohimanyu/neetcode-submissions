class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d_stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                d2, d1 = d_stack.pop(), d_stack.pop()
                if token == '+': result = d1 + d2
                elif token == '-': result = d1 - d2
                elif token == '*': result = d1 * d2
                else: result = int(d1 / d2)
                d_stack.append(result)
            else:
                num = int(token)
                d_stack.append(num)                
        
        return int(d_stack[0])