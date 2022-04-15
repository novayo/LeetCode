/*
main idea: greedy
time comp: O(nlogn)
space comp: O(1)
*/

#include <vector>
#include <algorithm>
using namespace std;

int nonConstructibleChange(vector<int> coins) {
  // Write your code here.
  int ans = 1;
	sort(coins.begin(), coins.end());
	
	for (int i=0; i<coins.size(); i++){
		if (coins[i] > ans){
			break;
		} else {
			ans += coins[i];
		}
	}
	
	return ans;
}

