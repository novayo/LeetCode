/*
main idea: counter
time comp: O(n)
space comp: O(k) - where k is the number of teams
*/

#include <vector>
#include <unordered_map>
using namespace std;

string tournamentWinner(vector<vector<string>> competitions,
                        vector<int> results) {
  // Write your code here.
	unordered_map<string, int> umap;
	string ans = "";
	int cur_max = 0;
	
	for (int i=0; i<competitions.size(); i++){
		string winner = competitions[i][results[i] == 0 ? 1 : 0];
		umap[winner] += 3;
		
		if (cur_max < umap[winner]){
			ans = winner;
			cur_max = umap[winner];
		}
	}

  return ans;
}

