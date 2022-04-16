/*
main idea: dp
time comp: O(n)
space comp: O(n)
*/

#include <vector>

using namespace std;

vector<int> arrayOfProducts(vector<int> array) {
  // Write your code here.
	int n = array.size();
	vector<int> ans(n, 1);
	vector<int> prefix(n, 1);
	vector<int> suffix(n, 1);
	
	// prefix
	for (int i = 1; i < n; i++){
		prefix[i] = prefix[i-1] * array[i-1];
	}
	
	// suffix
	for (int i = n-2; i >= 0; i--){
		suffix[i] = suffix[i+1] * array[i+1];
	}
	
	// ans
	for (int i = 0; i < n; i++){
		ans[i] = prefix[i] * suffix[i];
	}
	
  return ans;
}

