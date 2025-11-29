#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(2*n);
        for (int &x : a) cin >> x;

        unordered_map<int,int> freq;
        for (int x : a) freq[x]++;

        int E = 0, O = 0;
        for (auto &p : freq) {
            if (p.second % 2 == 0) E++;
            else O++;
        }

        int k = min(E, n);
        cout << (2 * k + O) << "\n";
    }
    return 0;
}
