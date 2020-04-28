class Solution:
    def findKthLargest_1(self, nums, k: int) -> int:
        """
        * 暴力 先排序，升序，找倒数第k个

        注意到第 k 个最大元素也就是第 N - k 个最小元素，

        时间复杂度 o(nlogn)  一般默认sort是快排
        空间复杂度 o(1)

        """
        size = len(nums)
        nums.sort()
        return nums[size - k]

    def findKthLargest_2(self, nums, k: int) -> int:
        """
        * 快速选择类似于快排

        注意到第 k 个最大元素也就是第 N - k 个最小元素，

        时间复杂度 o(n)  最坏情况 O(N^2)
        空间复杂度 o(1)

        """
        size = len(nums)
        target = size - k
        left = 0
        right = size - 1
        while True:
            index = self.__partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1
        #  循环不变量：[left + 1, j] < pivot
        #  (j, i) >= pivot

    # 选择一个枢轴，并在线性时间内定义其在排序数组中的位置。
    # 所有小于枢轴的元素都在其左侧，所有大于或等于的元素都在其右侧。
    # 由于知道要找的第 N - k 小的元素在哪部分中，我们不需要对两部分都做处理，这样就将平均时间复杂度下降到O(N)。

    def __partition(self, nums, left, right):
        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def findKthLargest_3(self, nums, k: int) -> int:
        """
         * 堆排序
         创建一个大顶堆，将所有数组中的元素加入堆中，并保持堆的大小 <= k。这样，堆中就保留了前 k 个最大的元素。

         时间复杂度 o(klogn)
         空间复杂度 o(k)    用于存储堆元素。

         """
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_loc = idx
            if left < max_len and nums[max_loc] < nums[left]:
                max_loc = left
            if right < max_len and nums[max_loc] < nums[right]:
                max_loc = right
            if max_loc != idx:
                nums[idx], nums[max_loc] = nums[max_loc], nums[idx]
                adjust_heap(max_loc, max_len)

        # 建堆
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(i, n)
        # print(nums)
        res = None
        for i in range(1, k + 1):
            # print(nums)
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0, n - i)
        return res



