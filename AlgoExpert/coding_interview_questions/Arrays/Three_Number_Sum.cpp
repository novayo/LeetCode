/*
main idea: recursion
time comp: O(n^2)
space comp: O(n)
*/

#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

// define
vector<vector<int>> ksum(vector<int>& array, int idx, int targetSum, int k);
bool comp(vector<int> v1, vector<int> v2){
	if (v1[0] < v2[0]){
		return true;
	} else if (v1[0] == v2[0] && v1[1] < v2[1]){
			return true;
	} else {
		return false;
	}
}

// main
vector<vector<int>> threeNumberSum(vector<int> array, int targetSum) {
  // Write your code here.
	sort(array.begin(), array.end());
  return ksum(array, 0, targetSum, 3);
}

vector<vector<int>> ksum(vector<int>& array, int idx, int targetSum, int k){
	int n = array.size() - idx;
	if (idx >= array.size() || array[idx]*k > targetSum || array.back()*k < targetSum){
		return vector<vector<int>>();
	}
	
	vector<vector<int>> ret;
	
	if (k == 2){
		unordered_set<int> uset;
		for (int i=idx; i < array.size(); i++){
			int target = targetSum-array[i];
			if (uset.find(target) != uset.end()){
				ret.push_back({target, array[i]});
			}
			uset.emplace(array[i]);
		}
		sort(ret.begin(), ret.end(), comp);
	} else {
		for (int i=idx; i < array.size(); i++){
			if (i == idx || array[i-1] != array[i]){
				for (auto vec : ksum(array, i+1, targetSum-array[i], k-1)){
					vec.insert(vec.begin(), array[i]);
					ret.push_back(vec);
				}
			}
		}
	}
	
	return ret;
}
