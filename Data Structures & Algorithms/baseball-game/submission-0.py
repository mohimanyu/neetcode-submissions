class Solution:
    def calPoints(self, operations: List[str]) -> int:
        calstack = []

        for op in operations:
            stack_length = len(calstack)
            if op == '+':
                calstack.append(int(calstack[stack_length-1]) + int(calstack[stack_length-2]))
            elif op == 'D':
                calstack.append(2 * int(calstack[stack_length-1]))
            elif op == 'C':
                del calstack[stack_length-1]
            else:
                calstack.append(op)
        
        result = 0
        for item in calstack:
            result += int(item)

        return result
        