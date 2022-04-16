/*
main idea: recursion
time comp: O(n^3)
space comp: O(n^2)
- where n is the length of the input array
*/

#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

vector<vector<int>> ksum(vector<int>& array, int idx, int targetSum, int k);

vector<vector<int>> fourNumberSum(vector<int> array, int targetSum) {
  // Write your code here.
  sort(array.begin(), array.end());
	return ksum(array, 0, targetSum, 4);
}

vector<vector<int>> ksum(vector<int>& array, int idx, int targetSum, int k){
	int n = array.size();
	if (idx >= n || array[idx] * k > targetSum || array.back() * k < targetSum){
		return vector<vector<int>>();
	}
	
	vector<vector<int>> ret;
	
	if (k == 2){
		unordered_set<int> found;
		for (int i=idx; i < n; i++){
			int target = targetSum - array[i];
			if (found.find(target) != found.end()){
				ret.push_back({target, array[i]});
			}
			found.emplace(array[i]);
		}
	} else{
		for (int i = idx; i < n; i++){
			if (i == idx || array[i-1] != array[i]){
				for (auto vec : ksum(array, i+1, targetSum-array[i], k-1)){
					vec.push_back(array[i]);
					ret.push_back(vec);
				}
			}
		}
	}
	
	return ret;
}
