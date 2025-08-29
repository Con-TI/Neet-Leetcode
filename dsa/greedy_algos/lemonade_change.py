class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for b in bills:
            if b == 5:
                fives += 1
            elif b == 10:
                tens += 1
                fives -= 1
            elif b == 20:
                if tens > 0:
                    tens -= 1
                    fives -= 1
                else:
                    fives -= 3
            if fives < 0 or tens <0:
                return False

        return True