class Solution {
    public int[] next = new int[]{1,0,-1,0,1};
    
    public int maxAreaOfIsland(int[][] grid) {
        int ans = 0;
        
        for (int i=0; i<grid.length; i++){
            for (int j=0; j<grid[i].length; j++){
                if (grid[i][j] == 1){
                    ans = Math.max(ans, bfs(grid, i, j));
                }
            }
        }
        
        return ans;
    }
    
    public int bfs(int[][] grid, int i, int j){
        int ret = 0;
        
        Queue<Pair<Integer,Integer>> q = new LinkedList<Pair<Integer,Integer>>();
        Set<Pair<Integer,Integer>> s = new HashSet<Pair<Integer,Integer>>();
        
        q.offer(new Pair<Integer,Integer>(i, j));
        s.add(new Pair<Integer,Integer>(i, j));
        
        while (q.size() > 0){
            Pair<Integer,Integer> pos = q.poll();
            
            int x = pos.getKey();
            int y = pos.getValue();
            
            grid[x][y] = 0;
            ret += 1;
            
            for (int offset=0; offset<4; offset++){
                int _x = x + next[offset];
                int _y = y + next[offset+1];
                Pair<Integer,Integer> _pos = new Pair<Integer,Integer>(_x, _y);
                
                if (_x < 0 || _x >= grid.length || _y < 0 || _y >= grid[_x].length || 
                    s.contains(_pos) || grid[_x][_y] != 1){
                    continue;
                }
                
                s.add(_pos);
                q.offer(_pos);
            }
        }
        
        return ret;
    }
}
