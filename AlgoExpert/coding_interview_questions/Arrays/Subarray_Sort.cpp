/*
main idea: sort
time comp: O(nlogn)
space comp: O(1)
- where n is the length of the input array
*/

#include <vector>
#include <algorithm>
using namespace std;

vector<int> subarraySort(vector<int> array) {
  // Write your code here.
	int n = array.size();
	vector<int> ans(2, -1);
	vector<int> array_ori = array;
	sort(array.begin(), array.end());
	
	int s1=0, s2=0;
	bool flag = true;
	for (int i = 0; i < n; i++){
		s1 += array_ori[i];
		s2 += array[i];
		
		if (flag && s1 != s2){
			ans[0] = i;
			flag = false;
		} else if (!flag && s1 == s2){
			ans[1] = i;
			break;
		}
	}
	
  return ans;
}

