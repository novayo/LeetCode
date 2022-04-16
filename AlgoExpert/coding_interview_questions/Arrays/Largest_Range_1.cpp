/*
main idea: set
time comp: O(n)
space comp: O(n)
*/

#include <vector>
#include <unordered_set>
using namespace std;

vector<int> largestRange(vector<int> array) {
  // Write your code here.
	vector<int> ans(2, array[0]);
	
	unordered_set<int> uset;
	for (auto val : array) {
		uset.emplace(val);
	}
	
	for (int i = 0; i < array.size(); i++) {
		if (uset.find(array[i]-1) != uset.end()) {
			continue;
		} else {
			int val = array[i];
			while (uset.find(val) != uset.end()) {
				uset.erase(val);
				val++;
			}
			
			if (val-1 - array[i] > ans[1]-ans[0]){
				ans = {array[i], val-1};
			}
		}
	}
	
  return ans;
}

