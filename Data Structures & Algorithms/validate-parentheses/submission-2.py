class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []
        # push opening ones
        for bracket in s:

            if bracket in hash_map:

                if not stack:
                    return False

                if hash_map[bracket] != stack.pop():
                    return False

            else:
                stack.append(bracket)

        return len(stack) == 0

            





        