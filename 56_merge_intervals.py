class Solution:
    def merge(self, intervals):
        """
        *使用排序
        时间复杂度 o(nlogn) 主要是排序的时间 遍历一遍数组是n
        空间复杂度 o(logn)  额外的用时
        """
        intervals.sort(key=lambda x:x[0])
        if len(intervals) <= 1:
            return intervals

        result = []
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])

        return result
