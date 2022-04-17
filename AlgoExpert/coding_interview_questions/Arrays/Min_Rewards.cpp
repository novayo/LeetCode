/*
main idea: dp
time comp: O(n)
space comp: O(n)
- where n is the length of the input array
*/

#include <vector>
#include <cmath>
using namespace std;

int minRewards(vector<int> scores) {
  // Write your code here.
	int n = scores.size();
	vector<int> prefix(n, 0);
	vector<int> suffix(n, 0);
	
	int cur = 0;
	for (int i = n-1; i >= 0; i--) {
		if (i == n-1) {
			continue;
		} else if (scores[i] < scores[i+1]) {
			cur = 0;
		} else {
			cur++;
		}
		prefix[i] = cur;
	}
	
	cur = 0;
	for (int i = 0; i < n; i++) {
		if (i == 0) {
			continue;
		} else if (scores[i-1] > scores[i]) {
			cur = 0;
		} else {
			cur++;
		}
		suffix[i] = cur;
	}
	
	int ans = 0;
	for (int i = 0; i < n; i++) {
		ans += max(prefix[i], suffix[i]) + 1;
	}
	
  return ans;
}

