/*
main idea: simulate
time comp: O(n)
space comp: O(n)
- where n is the number of elements of the input array
*/

#include <vector>

using namespace std;

enum face { UP_RIGHT, DOWN_LEFT };
int dir[2][2] = { {-1, 1}, {1, -1} };

vector<int> zigzagTraverse(vector<vector<int>> array) {
  // Write your code here.
	int height = array.size();
	int width = array[0].size();
	vector<int> ans;
	
	int face = DOWN_LEFT;
	int x = 0, y = 0;
	while (x != height-1 || y != width-1) {
		ans.push_back(array[x][y]);
		
		int _x = x + dir[face][0];
		int _y = y + dir[face][1];
		
		if (_x >= height) {
			y++;
			face = UP_RIGHT;
		} else if (_y < 0) {
			x++;
			face = UP_RIGHT;
		} else if (_y >= width) {
			x++;
			face = DOWN_LEFT;
		} else if (_x < 0) {
			y++;
			face = DOWN_LEFT;
		} else {
			x = _x;
			y = _y;
		}
	}
	
	ans.push_back(array[x][y]);
	
  return ans;
}

