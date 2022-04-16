/*
main idea: find the first non-sorted subarray and find the min / max of this subarray and find the actual index in the input array
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
*/

#include <vector>
#include <limits>
#include <cmath>
using namespace std;

bool isSort(vector<int> array, int idx);

vector<int> subarraySort(vector<int> array) {
  // Write your code here.
	int _min = INT_MAX;
	int _max = INT_MIN;
	
	for (int i = 0; i < array.size(); i++){
		if (!isSort(array, i)){
			_min = min(_min, array[i]);
			_max = max(_max, array[i]);
		}
	}
	cout << _min << " " << _max << endl;
	int l = 0, r = array.size()-1;
	while (l < array.size() && array[l] <= _min){
		l++;
	}
	while (r >= 0 && array[r] >= _max){
		r--;
	}
	
	if (l > r) {
		return vector<int> {-1, -1};
	} else {
	  return vector<int> {l, r};
	}
}

bool isSort(vector<int> array, int idx){
	if (idx == 0){
		return array[idx] < array[idx+1];
	} else if (idx == array.size()-1) {
		return array[idx-1] < array[idx];
	} else {
		return array[idx-1] < array[idx] && array[idx] < array[idx+1];
	}
}
