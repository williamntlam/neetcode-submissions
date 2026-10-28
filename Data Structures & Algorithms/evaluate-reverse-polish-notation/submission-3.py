class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # what about numbers with multiple digits?
        # i think it's fine, if a resulting number is double
        # digits we can account for this in the stack.
        # runtime complexity: O(n)
        # spacetime complexity: O(n) -> we could append n-1 numbers with + potentially.
        stack = []
        for index in range(len(tokens)):
            token = tokens[index]
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                second_number = stack.pop()
                first_number = stack.pop()

                if token == "+":
                    stack.append(first_number + second_number)
                elif token == "-":
                    stack.append(first_number - second_number)
                elif token == "*":
                    stack.append(first_number * second_number)
                else:
                    stack.append(int(first_number / second_number))

        return stack[-1]
        