class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        biggest_consec = []
        cur_consec = [nums[0]]
        for num in nums:
            if num == cur_consec[-1]:
                continue
            elif num == cur_consec[-1]+1:
                cur_consec.append(num)
            else:
                if len(biggest_consec) < len(cur_consec):
                    biggest_consec = cur_consec
                cur_consec = [num]
        return max([len(biggest_consec),len(cur_consec)])