class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True) # Farthest away first
        print(pair)
        stack = []
        for p,s in pair:
            stack.append((target-p)/s) # Time taken
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Merge
                stack.pop()
        return len(stack)