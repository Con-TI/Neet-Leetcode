class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            if nums.count(candidate) > n // 2:
                return candidate

        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res

        nums.sort()
        return nums[len(nums) // 2]

        hash_map = defaultdict(int)
        res = 0
        max_count = 0
        for n in nums:
            hash_map[n] += 1
            if hash_map[n]>max_count:
                res = n
                max_count = hash_map[n]
        return res

        hash_map = dict()
        for n in nums:
            if n not in hash_map.keys():
                hash_map[n] = 1
            else:
                hash_map[n] += 1
        for key in hash_map:
            if hash_map[key]>len(nums)//2:
                return key
