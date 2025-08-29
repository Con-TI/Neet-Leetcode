class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        vals_to_counts = defaultdict(int)
        counts_to_vals = defaultdict(list)
        for num in nums:
            vals_to_counts[num] += 1
        for key in vals_to_counts:
            counts_to_vals[vals_to_counts[key]].append(key)
        res = []
        for key in reversed(sorted(counts_to_vals.keys())):
            print(res)
            if k-len(res) > len(counts_to_vals[key]):
                res += counts_to_vals[key]
            else:
                res += counts_to_vals[key][-(k-len(res)):]
                break
            
        return res