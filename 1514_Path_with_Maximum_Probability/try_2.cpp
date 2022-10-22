class Solution {
public:
    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start, int end) {
        // build graph
        unordered_map<int, vector<pair<int, double>>> graph;
        for (int i=0; i<edges.size(); i++) {
            int node1 = edges[i][0], node2 = edges[i][1];
            double prob = succProb[i];
            graph[node1].push_back({node2, prob});
            graph[node2].push_back({node1, prob});
        }
        
        // bfs
        unordered_set<int> found;
        priority_queue<pair<double,int>> pq;

        pq.push({1.0, start});
        while (!pq.empty()) {
            auto [cur_prob, cur_node] = pq.top(); pq.pop();
            
            if (cur_node == end) return cur_prob;
            if (found.find(cur_node) != found.end()) continue;
            found.insert(cur_node);
            
            for (auto& [node, prob] : graph[cur_node]) {
                if (found.find(node) != found.end()) continue;
                pq.push({prob * cur_prob, node});
            }
        }
        
        return 0;
    }
};

