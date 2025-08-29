class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """

        letters = deque()
        first = {}
        last = {}

        for i,letter in enumerate(s):
            if first.get(letter,None) is None:
                first[letter] = i

            if last.get(letter,None) is None:
                last[letter] = i
            last[letter] = max(last[letter], i)

            if letter not in letters:
                letters.append(letter)

        res = []
        while letters:
            letter = letters.popleft()

            smallest_idx = first[letter]
            largest_idx = last[letter]
            for _ in range(len(letters)):
                letter = letters.popleft()
                l, r = first[letter], last[letter]
                if smallest_idx < l < largest_idx or smallest_idx < r < largest_idx:
                    smallest_idx = min(smallest_idx, l)
                    largest_idx = max(largest_idx, r)
                else:
                    letters.append(letter)
            size = largest_idx - smallest_idx + 1
            res.append(size)
        return res


