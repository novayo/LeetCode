/*
main idea: hash

time comp: O(n)
space comp: O(n)
*/

#include <vector>
#include <unordered_set>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  // Write your code here.
	unordered_set <int> uset;
	for (auto val : array){
		int target = targetSum - val;
		if (uset.find(target) != uset.end()){
			return {target, val};
		} else {
			uset.emplace(val);
		}
	}
	
  return {};
}
