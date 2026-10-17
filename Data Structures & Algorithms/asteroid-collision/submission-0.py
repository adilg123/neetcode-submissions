class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        res = []
        stack = []
        for i in asteroids:
            if i > 0:
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1] < abs(i):
                    stack.pop()
                if len(stack) == 0:
                    res.append(i)
                else:
                    if stack[-1] == abs(i):
                        stack.pop()
        res += stack
        return res