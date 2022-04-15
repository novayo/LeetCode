/*
main idea: two pointer
time comp: O(n)
space comp: O(1)
*/

using namespace std;

bool isValidSubsequence(vector<int> array, vector<int> sequence) {
  // Write your code here.
	if (array.size() < sequence.size()){
		return false;
	}
	
	int idx = 0;
	for (auto target : sequence){
		bool found = false;
		while (idx < array.size()){
			if (array[idx] == target){
				found = true;
				idx++;
				break;
			}
			idx++;
		}
		if (!found){
			return false;
		}
	}
	
  return true;
}

