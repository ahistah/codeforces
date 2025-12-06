/**
 * Problem: C. Annoying Game
 * Logic:
 * 1. If k is even, Bob can neutralize all of Alice's moves. Result is MSS of original 'a'.
 * 2. If k is odd, Alice has 1 net move. She uses it to boost the index 'i' that maximizes the final MSS.
 * We calculate max path through every 'i' using prefix/suffix max sums (Kadane's style).
 */

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

typedef long long ll;
const ll INF = 1e18; // Large enough value to handle constraints

// Function to calculate standard Maximum Subarray Sum (Kadane's Algorithm)
ll get_mss(int n, const vector<ll>& a) {
    ll max_so_far = -INF;
    ll current_max = -INF;
    
    for(ll x : a) {
        // If current_max is negative, starting a new subarray at x is better
        if (current_max < 0) current_max = x;
        else current_max += x;
        
        if (current_max > max_so_far) max_so_far = current_max;
    }
    return max_so_far;
}

void solve() {
    int n;
    ll k;
    if (!(cin >> n >> k)) return;
    
    vector<ll> a(n);
    for(int i = 0; i < n; ++i) cin >> a[i];
    
    vector<ll> b(n);
    for(int i = 0; i < n; ++i) cin >> b[i];

    // Case 1: Even k -> Players cancel out. Return original MSS.
    if (k % 2 == 0) {
        cout << get_mss(n, a) << endl;
    } 
    // Case 2: Odd k -> Alice gets 1 net boost. Find optimal index to boost.
    else {
        // L[i] stores the max subarray sum ending at index i
        vector<ll> L(n);
        ll current = -INF;
        for(int i = 0; i < n; ++i) {
            if (current < 0) current = a[i];
            else current += a[i];
            L[i] = current;
        }

        // R[i] stores the max subarray sum starting at index i
        vector<ll> R(n);
        current = -INF;
        for(int i = n - 1; i >= 0; --i) {
            if (current < 0) current = a[i];
            else current += a[i];
            R[i] = current;
        }
        
        ll original_mss = get_mss(n, a);
        ll max_with_boost = -INF;

        // Check every index i as the candidate for the uncancelled boost
        for(int i = 0; i < n; ++i) {
            // The max sum passing through i is (EndAt[i] + StartAt[i] - a[i])
            // We add b[i] to this sum.
            ll current_boosted_path = L[i] + R[i] - a[i] + b[i];
            if (current_boosted_path > max_with_boost) {
                max_with_boost = current_boosted_path;
            }
        }
        
        // The result is the best of modifying an index vs the original maximum
        // (Though modifying with b_i >= 0 will always be >= original)
        cout << max(original_mss, max_with_boost) << endl;
    }
}

int main() {
    // Fast I/O
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while(t--) {
            solve();
        }
    }
    return 0;
}