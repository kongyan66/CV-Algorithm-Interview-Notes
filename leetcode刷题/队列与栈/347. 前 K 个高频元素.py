# 题目：给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 考点：topk 问题 涉及大小顶堆（不熟悉）
# 思路：1.统计频率（map) 2.对频率进行排序（小顶堆） 3.取出topk 元素
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      # 统计各数字出现的频率
      map_ = {}
      for item in nums:
        map_[item] = map_.get(item, 0) + 1
     #对频率排序
     #定义一个小顶堆，大小为k
      pri_heap = []
      #用固定大小为k的小顶堆，扫面所有频率的数值
      for key, fri in map_.items():
        heapq.heappush(pri_heap, (fri, key)) # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
        if len(pri_heap) > k:
          heapq.heappop(pri_heap)
      #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组 
      result = [0] * k
      for i in range(k-1, -1, -1):  
        result[i] = heapq.heappop(pri_heap)[1]
      
      return result