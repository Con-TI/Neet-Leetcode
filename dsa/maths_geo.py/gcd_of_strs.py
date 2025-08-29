class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Non identical structure
        if str1 + str2 != str2 + str1:
            return ""

        # Simply find the gcd of their lengths since its in
        # multiples of the smallest divisor
        g = self.gcd(min(len(str1),len(str2)), max(len(str1), len(str2)))
        return str1[:g]

    def gcd(self, a, b):
        # Euclid's algo
        # Leverages division properties
        while b:
            a, b = b, a % b
        return a