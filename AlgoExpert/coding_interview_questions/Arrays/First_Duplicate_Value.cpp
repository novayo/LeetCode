/*
main idea: mark index as negtive
time comp: O(n)
space comp: O(1)
*/

#include <vector>
using namespace std;

int firstDuplicateValue(vector<int> array) { 
	int n = array.size();
	int idx = 0;
	while (idx < n){
		int target = abs(array[idx])-1;
		if (array[target] < 0){
			break;
		} else {
			array[target] *= -1;
		}
		idx++;
	}
	
	return idx >= n ? -1 : abs(array[idx]);
}

