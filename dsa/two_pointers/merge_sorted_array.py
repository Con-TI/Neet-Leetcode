class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1

        # Modifies in place using 3 ptrs starting from the right.
        # Last ptr is used to modify, m and n are used for querying
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
        return

        # Three pointers i for nums1, j for nums2, idx for the answer array
        # O(m+n) time complexity with O(m) space
        nums1_copy = nums1[:m]
        idx = 0
        i = j = 0
        while idx < m+n:
            if j>=n or (i<m and nums1_copy[i] <= nums2[j]):
                nums1[idx] = nums1_copy[i]
                i+=1
            else:
                nums1[idx] = nums2[j]
                j+=1
            idx += 1
        return 

        # Sort method O((m+n)log(m+n)) time complexity
        nums1[m:] = nums2[:n]
        return