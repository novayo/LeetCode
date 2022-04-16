/*
main idea: mimck
time comp: O(n)
space comp: O(n)
- where n is the number of elements in input array
*/

#include <unordered_set>
#include <string>
using namespace std;

enum FACE {
	UP=0, 
	RIGHT, 
	DOWN, 
	LEFT
};

int dir[4][2] = {
	{-1, 0},
	{0, 1},
	{1, 0},
	{0, -1}
};

vector<int> spiralTraverse(vector<vector<int>> array) {
  // Write your code here.
	int height = array.size();
	int width = array[0].size();
	
	vector<int> ans(height * width, -1);
	int idx = 0;
	int face = RIGHT;
	
	int x=0, y=0, hit_times=0;
	unordered_set<string> found;
	found.emplace(to_string(x) + to_string(y));
	ans[idx++] = array[x][y];
	
	while (hit_times < 4){
		// go next
		int _x = x + dir[face][0];
		int _y = y + dir[face][1];
		string key = to_string(_x) + to_string(_y);
		
		// if hit wall
		if (_x < 0 || _x >= height || _y < 0 || _y >= width || found.find(key) != found.end()){
			face = (face+1) % 4;
			hit_times++;
		} else {
			x = _x; y = _y;
			found.emplace(key);
			hit_times = 0;
			ans[idx++] = array[x][y];
		}
	}
	
  return ans;
}

