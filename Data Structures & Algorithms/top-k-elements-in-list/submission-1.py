class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={} #hashmap to get the count of each number
        freq= [[]for i in range(len(nums)+1)] # list of values

        for n in nums: #going throught the array nums
            count[n]=1+ count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res




        