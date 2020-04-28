import heapq


class Solution:
    def topKFrequent_1(self, nums, k: int):
        """
        * 桶排序

        时间复杂度 o(n)
        空间复杂度 o(n)

        """
        # 统计元素的频率
        freq_dict = dict()
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = freq_dict[num] + 1
            else:
                freq_dict[num] = 1

        # 桶排序
        # 可能出现 两个数字有一样的频率，所以内部也要用[]包装
        # 注意value就是按照递增的顺序
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in freq_dict.items():
            bucket[value].append(key)

        # 逆序取出前k个元素
        ret = list()
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                ret.extend(bucket[i])
            if len(ret) >= k:
                break
        return ret

    def topKFrequent_2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 统计元素的频率
        freq_dict = dict()
        for num in nums:
            if num in freq_dict:
                freq_dict[num] = freq_dict[num] + 1
            else:
                freq_dict[num] = 1

        # 维护一个大小为k的最小堆，使得堆中的元素即为前k个高频元素
        # 每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
        # 如果是大根堆，就没有办法很快的比较
        pq = []
        for key, value in freq_dict.items():
            if len(pq) < k:
                heapq.heappush(pq, (value, key))
            elif value > pq[0][0]:
                heapq.heapreplace(pq, (value, key))

        # 取出堆中的元素
        ret = []
        while pq:
            ret.append(heapq.heappop(pq)[1])
        return ret


class Heap:
    def __init__(self):
        self.heap = [(0, 0)]  # (num, num出现的次数)
        self.cnt = 0

    def push(self, x):
        self.heap.append(x)
        self.cnt += 1
        ind = self.cnt
        while ind > 1:
            # 比较上一层 大的往上放
            if self.heap[ind][1] > self.heap[ind // 2][1]:
                self.heap[ind // 2], self.heap[ind] = self.heap[ind], self.heap[ind // 2]
                ind = ind // 2
            else:
                break
        print(self.heap)

    def pop(self):
        max_num = self.heap[1][0]
        # 把最后一个放到最前面，删掉最后一个
        ind = self.cnt
        self.heap[1] = self.heap[ind]
        del self.heap[-1]
        self.cnt -= 1
        ind = 1
        # 判断有无下一层 大的往上放
        while ind * 2 <= self.cnt:
            swap_ind = ind
            if self.heap[ind * 2][1] > self.heap[ind][1]:
                swap_ind = ind * 2
            if (ind * 2) + 1 <= self.cnt and self.heap[(ind * 2) + 1][1] > self.heap[swap_ind][1]:
                swap_ind = (ind * 2) + 1

            self.heap[ind], self.heap[swap_ind] = self.heap[swap_ind], self.heap[ind]
            ind = swap_ind

        return max_num


class Solution_1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dict = {}
        heap = Heap()
        res = []
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
        for x in num_dict.items():
            heap.push(x)
        for _ in range(k):
            res.append(heap.pop())
        return res





# 第一种
"""
函数定义：
heapq.heappush(heap, item)
    - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap)
    - Pop and return the smallest item from the heap, maintaining the heap invariant.
    If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
"""
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆

print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]


# 第二种
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]
