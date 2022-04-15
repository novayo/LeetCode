/*
main idea: two pointer
time comp: O(n)
space comp: O(n)
*/

#include <vector>
using namespace std;

vector<int> sortedSquaredArray(vector<int> array) {
  // Write your code here.
	int n = array.size();
	vector<int> ans(n, -1);
	int idx = n-1;
	
	// two pointer
	int i = 0, j = n-1;
	while (i <= j){
		if (array[i]*array[i] >= array[j]*array[j]){
			ans[idx--] = array[i]*array[i];
			i++;
		} else {
			ans[idx--] = array[j]*array[j];
			j--;
		}
	}
	
  return ans;
}


