class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # On the number of (
        upperbound, lowerbound = 0, 0


        for letter in s:
            if letter == "(":
                upperbound += 1
                lowerbound += 1
            elif letter == ")":
                upperbound -= 1
                lowerbound -= 1
            else:
                # Star counts as either left or right
                upperbound += 1
                lowerbound -= 1
            if upperbound < 0:
                return False

            # Can't have fewer
            if lowerbound < 0:
                lowerbound = 0

        # If our upper bound stayed positive, then we have enough stars and ( to compensate )
        # Then we just need to make sure ( is 0 as it means there is a way to match all ( and )
        # equally
        return lowerbound == 0