/*
main idea: sliding window
time comp: O(n*k)
space comp: O(k)
- where n is the length of the input blocks and k is the number of requirement.
*/

#include <vector>
#include <unordered_map>
#include <limits>

using namespace std;

bool isAns(unordered_map<string, int> map);

int apartmentHunting(vector<unordered_map<string, bool>> blocks,
                     vector<string> reqs) {
  // Write your code here;
	int ans_i = 0, ans_j = blocks.size();
	
	// init
	unordered_map<string, int> table;
	for (auto str : reqs) {
		table[str] = 0;
	}
	
	// sliding window
	int i = 0;
	for (int j = 0; j < blocks.size(); j++) {
		// get this block
		for (auto& t : blocks[j]) {
			if (table.find(t.first) == table.end()) continue;
			if (t.second) {
				table[t.first]++;
			}
		}
		
		// sliding window
		while (i < j && isAns(table)) {
			// update answer
			if (j-i < ans_j-ans_i) {
				ans_j = j;
				ans_i = i;
			}
			
			for (auto& t : blocks[i]) {
				if (table.find(t.first) == table.end()) continue;
				if (t.second){
					table[t.first]--;
				}
			}
			
			i++;
		}
	}
	
  return (ans_j+ans_i) / 2;
}


bool isAns(unordered_map<string, int> map) {
	for (auto& t : map) {
		if (t.second == 0) {
			return false;
		}
	}
	return true;
}

