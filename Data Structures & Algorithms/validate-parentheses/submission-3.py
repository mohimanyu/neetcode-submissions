class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        call_stack = []

        for ch in s:
            length = len(call_stack)
            if ch in ['(', '{', '[']:
                call_stack.append(ch)
            elif length > 0 and ch == ')' and call_stack[length-1] == '(':
                del call_stack[length-1]
            elif length > 0 and ch == '}' and call_stack[length-1] == '{':
                del call_stack[length-1]
            elif length > 0 and ch == ']' and call_stack[length-1] == '[':
                del call_stack[length-1]
            else:
                return False
        
        return len(call_stack) == 0
            