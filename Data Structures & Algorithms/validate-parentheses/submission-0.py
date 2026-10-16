class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack for tihs.
        # runtime: O(n)
        # spacetime: O(n)

        stack = []

        for char in s:
            if char == "(":
                stack.append(")")
                continue
            elif char == "[":
                stack.append("]")
                continue
            elif char == "{":
                stack.append("}")
                continue

            if char == ")" or char == "}" or char == "]":
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False


        return stack == []