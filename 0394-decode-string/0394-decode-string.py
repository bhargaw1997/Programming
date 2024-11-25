class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                curr_string = ''
                while stack[-1] != "[":
                    curr_string = stack.pop() + curr_string
                stack.pop()

                curr_number = ''
                while stack and stack[-1].isdigit():
                    curr_number = stack.pop() + curr_number
                
                curr_string = int(curr_number) * curr_string
                stack.append(curr_string)
        return "".join(stack)