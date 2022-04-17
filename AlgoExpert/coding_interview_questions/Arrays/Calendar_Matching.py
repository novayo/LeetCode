'''
main idea: binary search
time comp: O(nlogn + mlogm)
space comp: O(n + m)
- where n is the length of calendar1 and m is the length of calendar2
'''

import bisect

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
	def time2int(s):
		return int(s.split(':')[0]) * 60 + int(s.split(':')[1])
	
	def int2time(i):
		return f"{i//60}:{i%60:02d}"
	
	len1 = len(dailyBounds1)
	len2 = len(dailyBounds1)
	
	booked = []
	for calendar in [calendar1, calendar2]:
		for a, b in calendar:
			a = time2int(a)
			b = time2int(b)
			idx1 = bisect.bisect_left(booked, a)
			idx2 = bisect.bisect_right(booked, b)

			if (idx1%2 == 0 and idx2%2 == 0):
				booked[idx1: idx2] = [a, b]
			elif (idx1%2 == 0):
				booked[idx1: idx2] = [a]
			elif (idx2%2 == 0):
				booked[idx1: idx2] = [b]
			else:
				booked[idx1: idx2] = []
		
	d1_s, d1_e = time2int(dailyBounds1[0]), time2int(dailyBounds1[1])
	d2_s, d2_e = time2int(dailyBounds2[0]), time2int(dailyBounds2[1])
	bound = []
	if d1_s > d2_s:
		bound.append(d1_s)
	else:
		bound.append(d2_s)
	
	if d1_e > d2_e:
		bound.append(d2_e)
	else:
		bound.append(d1_e)
	
	if not booked:
		return [[int2time(bound[0]), int2time(bound[1])]]
	
	ans = []
	if (bound[0] < booked[0] and booked[0] - bound[0] >= meetingDuration):
		ans.append([int2time(bound[0]), int2time(booked[0])])
	for i in range(len(booked) // 2-1):
		i_start = booked[i*2+1]
		i_end = booked[i*2+2]
		
		if (i_start < bound[0] < i_end):
			i_start = bound[0]
		if (i_start < bound[1] < i_end):
			i_end = bound[1]
		
		if (i_end - i_start >= meetingDuration):
			ans.append([int2time(i_start), int2time(i_end)])
	
	if (booked[-1] < bound[1] and bound[1] - booked[-1] >= meetingDuration):
		ans.append([int2time(booked[-1]), int2time(bound[1])])
	
	return ans

