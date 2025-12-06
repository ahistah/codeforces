#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <set>

using namespace std;

const int dx[] = {0, 0, 1, -1};
const int dy[] = {1, -1, 0, 0};

struct DSU {
    vector<int> parent;
    vector<bool> is_sink; 
    int n, m;

    void init(int rows, int cols) {
        n = rows;
        m = cols;
        parent.resize(n * m);
        iota(parent.begin(), parent.end(), 0);
        is_sink.assign(n * m, true);
    }

    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }

    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            // Merge j into i
            parent[root_j] = root_i;
            is_sink[root_i] = is_sink[root_i] && is_sink[root_j];
        }
    }
};

struct Query {
    int r, c, x;
};

void solve() {
    int n, m;
    if (!(cin >> n >> m)) return;

    vector<vector<int>> grid(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> grid[i][j];
        }
    }

    int q;
    cin >> q;
    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].r >> queries[i].c >> queries[i].x;
        queries[i].r--; // 0-indexed
        queries[i].c--;
    }
    {
        DSU initial_dsu;
        initial_dsu.init(n, m);
        
        // Horizontal edges
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m - 1; ++j) {
                if (grid[i][j] == grid[i][j+1]) {
                    initial_dsu.unite(i * m + j, i * m + j + 1);
                }
            }
        }
        // Vertical edges
        for (int i = 0; i < n - 1; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == grid[i+1][j]) {
                    initial_dsu.unite(i * m + j, (i + 1) * m + j);
                }
            }
        }

        // Check sink status
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                int u = r * m + c;
                int root = initial_dsu.find(u);
                if (!initial_dsu.is_sink[root]) continue;

                for (int k = 0; k < 4; ++k) {
                    int nr = r + dx[k];
                    int nc = c + dy[k];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                        if (grid[nr][nc] < grid[r][c]) {
                            initial_dsu.is_sink[root] = false;
                            break;
                        }
                    }
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n * m; ++i) {
            if (initial_dsu.parent[i] == i && initial_dsu.is_sink[i]) {
                ans++;
            }
        }
        cout << ans << "\n";
    }

    // Square Root Decomposition
    // Block size heuristic: sqrt(Q) is approx 450.
    // However, N*M is up to 2e5. O(N*M * Q/B) is dominant.
    // If N*M and Q are both 2e5, B should be around sqrt(N*M) ~ 450.
    int B = 500; 
    
    DSU base_dsu;
    // We reuse memory to avoid allocation overhead
    base_dsu.parent.resize(n * m);
    base_dsu.is_sink.resize(n * m);
    
    // Arrays for micro DSU logic
    vector<int> micro_parent;
    vector<bool> micro_sink;
    vector<int> mapping(n * m, -1); 
    vector<int> active_nodes;

    vector<bool> is_changing(n * m, false);

    for (int b_start = 0; b_start < q; b_start += B) {
        int b_end = min(q, b_start + B);
        
        // 1. Identify changing cells in this block
        vector<int> changing_indices;
        for (int k = b_start; k < b_end; ++k) {
            int idx = queries[k].r * m + queries[k].c;
            if (!is_changing[idx]) {
                is_changing[idx] = true;
                changing_indices.push_back(idx);
            }
        }

        // 2. Build Base DSU (ignoring Changing Cells)
        // Reset base DSU
        iota(base_dsu.parent.begin(), base_dsu.parent.end(), 0);
        fill(base_dsu.is_sink.begin(), base_dsu.is_sink.end(), true);
        base_dsu.n = n; base_dsu.m = m;

        // Unite Fixed neighbors
        auto get_idx = [&](int r, int c) { return r * m + c; };
        
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                int u = get_idx(r, c);
                if (is_changing[u]) continue;

                // Right neighbor
                if (c + 1 < m) {
                    int v = get_idx(r, c + 1);
                    if (!is_changing[v]) {
                        if (grid[r][c] == grid[r][c+1]) base_dsu.unite(u, v);
                    }
                }
                // Down neighbor
                if (r + 1 < n) {
                    int v = get_idx(r + 1, c);
                    if (!is_changing[v]) {
                        if (grid[r][c] == grid[r+1][c]) base_dsu.unite(u, v);
                    }
                }
            }
        }

        // Determine Partial Sink status for Base Components
        // A Base Component is NOT a sink if it has a FIXED neighbor with strictly smaller value.
        // Interactions with Changing Cells are handled in the query loop.
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < m; ++c) {
                int u = get_idx(r, c);
                if (is_changing[u]) continue;
                
                int root = base_dsu.find(u);
                if (!base_dsu.is_sink[root]) continue;

                for (int k = 0; k < 4; ++k) {
                    int nr = r + dx[k];
                    int nc = c + dy[k];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                        int v = get_idx(nr, nc);
                        if (!is_changing[v]) {
                            if (grid[nr][nc] < grid[r][c]) {
                                base_dsu.is_sink[root] = false;
                                break;
                            }
                        }
                    }
                }
            }
        }

        // Calculate Initial Base Sinks count (sum of is_sink for all fixed roots)
        // We will subtract relevant ones and add new ones during queries.
        int total_base_sinks = 0;
        for (int i = 0; i < n * m; ++i) {
            if (!is_changing[i] && base_dsu.parent[i] == i && base_dsu.is_sink[i]) {
                total_base_sinks++;
            }
        }

        // 3. Process Queries
        for (int k = b_start; k < b_end; ++k) {
            int qr = queries[k].r;
            int qc = queries[k].c;
            int qx = queries[k].x;
            int q_idx = get_idx(qr, qc);
            
            grid[qr][qc] -= qx;

            // Build Micro DSU
            active_nodes.clear();
            
            // Add Changing Cells to active set
            for (int idx : changing_indices) {
                if (mapping[idx] == -1) {
                    mapping[idx] = active_nodes.size();
                    active_nodes.push_back(idx);
                }
            }

            // Add adjacent Fixed Component Roots to active set
            // And mark involved fixed roots to subtract from base total
            int fixed_roots_start_idx = active_nodes.size();
            
            for (int idx : changing_indices) {
                int r = idx / m;
                int c = idx % m;
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dx[d];
                    int nc = c + dy[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                        int nidx = get_idx(nr, nc);
                        if (!is_changing[nidx]) {
                            int root = base_dsu.find(nidx);
                            if (mapping[root] == -1) {
                                mapping[root] = active_nodes.size();
                                active_nodes.push_back(root);
                            }
                        }
                    }
                }
            }

            // Init Micro DSU structures
            int micro_size = active_nodes.size();
            micro_parent.resize(micro_size);
            iota(micro_parent.begin(), micro_parent.end(), 0);
            micro_sink.assign(micro_size, true);

            // Initialize properties
            // For Fixed roots: inherit base_sink.
            // For Changing cells: initially true (will check neighbors).
            for (int i = 0; i < micro_size; ++i) {
                int original_idx = active_nodes[i];
                if (is_changing[original_idx]) {
                    micro_sink[i] = true; 
                } else {
                    // Fixed root
                    micro_sink[i] = base_dsu.is_sink[original_idx];
                }
            }

            auto micro_find = [&](int i, auto&& self) -> int {
                if (micro_parent[i] == i) return i;
                return micro_parent[i] = self(micro_parent[i], self);
            };

            auto micro_unite = [&](int i, int j) {
                int ri = micro_find(i, micro_find);
                int rj = micro_find(j, micro_find);
                if (ri != rj) {
                    micro_parent[rj] = ri;
                    micro_sink[ri] = micro_sink[ri] && micro_sink[rj];
                }
            };

            // Process Edges and Drains in Micro Graph
            // 1. Changing <-> Changing
            // 2. Changing <-> Fixed
            
            for (int idx : changing_indices) {
                int u_map = mapping[idx];
                int r = idx / m;
                int c = idx % m;

                for (int d = 0; d < 4; ++d) {
                    int nr = r + dx[d];
                    int nc = c + dy[d];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                        int nidx = get_idx(nr, nc);
                        int v_map = -1;
                        int val_u = grid[r][c];
                        int val_v = grid[nr][nc];

                        if (is_changing[nidx]) {
                            v_map = mapping[nidx];
                        } else {
                            v_map = mapping[base_dsu.find(nidx)];
                        }


                        if (val_v < val_u) {
                            int root_u = micro_find(u_map, micro_find);
                            micro_sink[root_u] = false;
                        } 
                        

                        if (val_v == val_u) {
                            micro_unite(u_map, v_map);
                        }
                    }
                }
            }
            

            int current_ans = total_base_sinks;


            for (int i = fixed_roots_start_idx; i < micro_size; ++i) {
                int original_root = active_nodes[i];
                if (base_dsu.is_sink[original_root]) {
                    current_ans--;
                }
            }


            for (int i = 0; i < micro_size; ++i) {
                if (micro_parent[i] == i && micro_sink[i]) {
                    current_ans++;
                }
            }

            cout << current_ans << "\n";


            for (int node : active_nodes) mapping[node] = -1;
        }

        for (int idx : changing_indices) is_changing[idx] = false;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}