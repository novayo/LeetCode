/*
main idea: two pointer
time comp: O(nlogn + mlogm)
space comp: O(1)
- where n is the length of the first input array and m is the length of the second input array.
*/

#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
using namespace std;

vector<int> smallestDifference(vector<int> arrayOne, vector<int> arrayTwo) {
  // Write your code here.
	sort(arrayOne.begin(), arrayOne.end());
	sort(arrayTwo.begin(), arrayTwo.end());
	
	vector<int> ans(2, -1);
	int diff = INT_MAX;
	int i=0, j=0;
	while (i < arrayOne.size() && j < arrayTwo.size()){
		// update answer
		int cur_diff = abs(arrayOne[i] - arrayTwo[j]);
		if (cur_diff < diff){
			diff = cur_diff;
			ans[0] = arrayOne[i];
			ans[1] = arrayTwo[j];
		}
		
		// move forward
		if (arrayOne[i] <= arrayTwo[j]){
			i++;
		} else {
			j++;
		}
	}
	
  return ans;
}

