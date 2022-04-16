/*
main idea: greedy
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
*/

#include <cmath>
using namespace std;e

int longestPeak(vector<int> array) {
  // Write your code here.
	int n = array.size();
	int ans = 0;
	int j = 1;
	
	while (j < n){
		// find the first index which is not decending
		while (j < n && array[j-1] >= array[j]){
			j++;
		}
		
		// find peak now
		int i=j-1;
		
		// acending
		while (j < n && array[j-1] < array[j]){
			j++;
		}
		
		// if not peak
		if (j == n || array[j-1] == array[j]){
			continue;
		}
		
		// decending
		while (j < n && array[j-1] > array[j]){
			j++;
		}
		
		ans = max(ans, j-i);
	}
	
  return ans;
}

