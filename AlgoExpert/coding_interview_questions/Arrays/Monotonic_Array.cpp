/*
main idea: greedy
time comp: O(n)
space comp: O(1)
- where n is the length of the input array
*/

using namespace std;

bool isMonotonic(vector<int> array) {
  // Write your code here.
	vector<int> ways(2, 0); // [accending, decending]
	
	for (int j=1; j<array.size(); j++){
		if (array[j-1] > array[j]){
			ways[1] = 1;
		} else if (array[j-1] < array[j]){
			ways[0] = 1;
		}
	}
	
  return ways[0] + ways[1] != 2;
}

