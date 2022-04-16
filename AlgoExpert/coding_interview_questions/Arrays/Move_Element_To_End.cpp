/*
main idea: two pointer
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
*/

#include <vector>

using namespace std;

void swap(vector<int>& array, int i, int j);
	
vector<int> moveElementToEnd(vector<int> array, int toMove) {
  // Write your code here.
	int n = array.size();
	int i=0, j=n-1;
	
	while (i <= j){
		// find next move
		while (i <= j && array[i] != toMove){
			i++;
		}
		
		// find next location
		while (i <= j && array[j] == toMove){
			j--;
		}
		
		if (i > j){
			break;
		}
		
		// swap
		swap(array, i, j);
		i++;
		j--;
	}
	
  return array;
}

void swap(vector<int>& array, int i, int j){
	int tmp = array[i];
	array[i] = array[j];
	array[j] = tmp;
}
