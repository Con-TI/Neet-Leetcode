class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        # This algo is greedy since 
        # we immediately mark the cards in the hand that we find successors for
        # this is a locally optimal choice whenever we are trying to look for successors of our
        # current hand
        
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        for i in range(n):
            # Not visited
            if hand[i] >= 0:
                if not self.find_successors(hand, groupSize, i, n):
                    return False
        return True

    def find_successors(self, hand, groupSize, i, n):    
        # Checks the hand for sufficient successors
        # Uses visited nodes
        next_val = hand[i] + 1
        hand[i] = -1
        count = 1
        i += 1
        while i < n and count < groupSize:
            if hand[i] == next_val:
                next_val = hand[i] + 1
                hand[i] = -1
                count += 1
            i += 1
        return count == groupSize
