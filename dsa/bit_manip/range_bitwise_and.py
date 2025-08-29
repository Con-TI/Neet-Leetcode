class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """
        Idea: 
        - left = 10101 ....
        - right = 10101 ....

        the only parts that change throughout the range 
        are the right bits of left and right
        since they change, 0 is hit during the range on those bits
        so the final number is just the common left prefix of bits
        followed by zeroes.

        """
        shift = 0
        # Right shift until they are equal
        while left < right:
            left >>= 1 # Right shift
            right >>= 1 # Right shift
            shift += 1 # Add 1
        return left << shift