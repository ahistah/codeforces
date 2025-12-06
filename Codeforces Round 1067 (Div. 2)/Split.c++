#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
    int n;
    cin >> n;
    int size = 2 * n;
    vector<int> counts(size + 1, 0);
    
    for (int i = 0; i < size; ++i) {
        int x;
        cin >> x;
        counts[x]++;
    }
    
    int c_odd = 0;
    int c_even = 0;
    
    for (int i = 1; i <= size; ++i) {
        if (counts[i] > 0) {
            if (counts[i] % 2 != 0) {
                c_odd++;
            } else {
                c_even++;
            }
        }
    }
    int ans = c_odd + 2 * c_even;
    if (c_odd == 0) {
        if (c_even % 2 != n % 2) {
            ans -= 2;
        }
    }
    
    cout << ans << endl;
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