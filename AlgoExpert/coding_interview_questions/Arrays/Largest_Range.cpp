/*
main idea: sort
time comp: O(nlogn)
space comp: O(1)
*/

#include <vector>
#include <algorithm>
using namespace std;

vector<int> largestRange(vector<int> array) {
  // Write your code here.
	sort(array.begin(), array.end());
	vector<int> ans(2, 0);
	
	bool find = false;
	int i = 0;
	for (int j = 0; j < array.size()-1; j++){
		if (array[j] == array[j+1]){
			continue;
		}
		if (!find && array[j] + 1 == array[j+1]){
			i = j;
			find = true;
		} else if (find && array[j] + 1 != array[j+1]) {
			if (j-i > ans[1]-ans[0]){
				ans[0] = i;
				ans[1] = j;
			}
			find = false;
		}
	}
	
	if (find && array.size()-i > ans[1]-ans[0]){
			ans[0] = i;
			ans[1] = array.size()-1;
	}
	
  return {array[ans[0]], array[ans[1]]};
}

