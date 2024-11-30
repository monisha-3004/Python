import heapq 

class Solution(object):

    def nth_Ugly_Number(self,n):
        ugly_num = 0
        heap = []
        heapq.heappush(heap,1)
        for _ in range(n):
            ugly_num = heapq.heappop(heap)
            if ugly_num % 2 == 0:
                heapq.heappush(heap,ugly_num*2)
            elif ugly_num % 3 ==0:
                heapq.heappush(heap,ugly_num*3)
            else:
                heapq.heappush(heap,ugly_num*2)
                heapq.heappush(heap,ugly_num*3)
                heapq.heappush(heap,ugly_num*5)
        return ugly_num

n=7
s = Solution()
result = s.nth_Ugly_Number(n)
print("7th ugly number:")
print(result)

n=10
result = s.nth_Ugly_Number(n)
print("10th ugly number:")
print(result)

