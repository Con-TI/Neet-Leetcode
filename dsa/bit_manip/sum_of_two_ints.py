class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Hexadecimal representations
        # Every char represents 4 bits (so numbers 0 to 15 using 0 to 9 and A to F)
        
        mask = 0xFFFFFFFF # 32 bits all set to 1, to truncate things to 32 bits
        # In python, ints are unbounded so we need to have the mask

        max_int = 0x7FFFFFFF # first 31 bits set to 1

        while b != 0:
            
            # Carry over (only if both bits are matching)
            # Then left shift by 1 (as you would)
            carry = (a & b) << 1
            
            # Sum of binary nums without any carry over
            # Truncating within 32 bits
            a = (a ^ b) & mask 

            b = carry & mask # Trunacting within 32 bits

        return a if a <= max_int else ~(a ^ mask) # Truncated if larger than maxint