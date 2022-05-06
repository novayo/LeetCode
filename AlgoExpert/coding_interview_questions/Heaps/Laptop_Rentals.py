'''
main idea: heap
time comp: O(nlogn)
space comp: O(n)
- where n is the length of the input array	
'''
import heapq

def laptopRentals(times):
    # Write your code here.
	times.sort()
	end_time = []
	
	ans = 0
	for s, e in times:
		while end_time and end_time[0] <= s:
			heapq.heappop(end_time)
		
		heapq.heappush(end_time, e)
		ans = max(ans, len(end_time))
		
    return ans

