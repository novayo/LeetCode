/*
main idea: sort
time comp: O(nlogn)
space comp: O(n)
- where n is the length of the input array
*/

#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<vector<int>> mergeOverlappingIntervals(vector<vector<int>> intervals) {
  // Write your code here.
  sort(intervals.begin(), intervals.end());
	
	vector<vector<int>> ans;
	for (auto interval : intervals){
		if (ans.size() == 0 || interval[0] > ans.back()[1]){
			ans.push_back(interval);
		} else {
			ans.back()[1] = max(ans.back()[1], interval[1]);
		}
	}
	
	return ans;
}

