class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp_nums1 = nums1[:m]
        j = 0
        for i in range(m+n):
            if i < m:
                nums1[i] = temp_nums1[i]
            else:            
                nums1[i] = nums2[j]
                j  += 1
        nums1.sort()
        return nums1

        