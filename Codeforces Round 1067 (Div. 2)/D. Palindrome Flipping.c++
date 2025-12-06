#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>

using namespace std;

struct Op {
    int l, r;
};

void apply_op(string& s, int l, int r) {
    for (int i = l - 1; i < r; ++i) {
        s[i] = (s[i] == '0' ? '1' : '0');
    }
}

bool is_palindrome(const string& s, int l, int r) {
    int p1 = l - 1;
    int p2 = r - 1;
    while (p1 < p2) {
        if (s[p1] != s[p2]) return false;
        p1++;
        p2--;
    }
    return true;
}

void solve() {
    int n;
    cin >> n;
    string s, t;
    cin >> s >> t;

    if (s == t) {
        cout << "0\n";
        return;
    }
    vector<Op> ops;
    for (int L = 1; L <= n / 2; ++L) {
        int R = n - L + 1;
        bool check_center = (n % 2 != 0 && L == n / 2);
        int m = (n + 1) / 2; // Center index (1-based)
        bool satisfied = (s[L-1] == t[L-1] && s[R-1] == t[R-1]);
        if (check_center) {
            if (s[m-1] != t[m-1]) satisfied = false;
        }

        if (satisfied) continue;
        queue<pair<string, vector<Op>>> q;
        q.push({s, {}});
        
        set<string> visited;
        visited.insert(s);

        bool found = false;
        string solved_s = "";
        while (!q.empty()) {
            auto [curr_s, path] = q.front();
            q.pop();

            // Check correctness
            bool ok = (curr_s[L-1] == t[L-1] && curr_s[R-1] == t[R-1]);
            if (check_center) {
                if (curr_s[m-1] != t[m-1]) ok = false;
            }

            if (ok) {
                s = curr_s;
                for (auto op : path) ops.push_back(op);
                found = true;
                break;
            }
            if (path.size() >= 3) continue; 
            for (int k = L + 1; k <= R; ++k) {
                if (is_palindrome(curr_s, L, k)) {
                    string next_s = curr_s;
                    apply_op(next_s, L, k);
                    if (visited.find(next_s) == visited.end()) {
                        visited.insert(next_s);
                        vector<Op> next_path = path;
                        next_path.push_back({L, k});
                        q.push({next_s, next_path});
                    }
                }
            }
            for (int k = L; k < R; ++k) {
                if (is_palindrome(curr_s, k, R)) {
                    string next_s = curr_s;
                    apply_op(next_s, k, R);
                    if (visited.find(next_s) == visited.end()) {
                        visited.insert(next_s);
                        vector<Op> next_path = path;
                        next_path.push_back({k, R});
                        q.push({next_s, next_path});
                    }
                }
            }
        }

        if (!found) {
            cout << "-1\n";
            return;
        }
    }
    if (s != t) {
        cout << "-1\n";
    } else {
        cout << ops.size() << "\n";
        for (auto op : ops) {
            cout << op.l << " " << op.r << "\n";
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}