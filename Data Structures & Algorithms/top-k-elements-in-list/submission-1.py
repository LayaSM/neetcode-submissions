class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count elements:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # buckets array
        buckets = [[] for i in range (len(nums) +1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []

        for bucket in reversed(buckets):
            for n in bucket:
                res.append(n)

                if len(res) == k:
                    return res

        