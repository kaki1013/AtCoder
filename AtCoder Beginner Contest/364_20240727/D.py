# 실패
"""
parametric search
https://atcoder.jp/contests/abc364/editorial/10558

As in this problem, when you are asked to find the “k-th whatever-est something,”
    binary search is often adopted as the first step of the solution.
Indeed, binary search is indeed effective in this problem too.
Specifically, by defining f_j(x)=(the number of points among A_1,A_2,…,A_N such that the distance from B_j is at most x)
    the problem of “finding the k_j-th nearest point to B_j among points A_1,A_2,…,A_N”
        is boiled down to finding the minimum x with f_j(x)≥k_j

Since f_j(x) is obviously monotonic,
    the problem can be solved by binary search that processes the following query O(QlogA) times:
        “evaluate f_j(x) for given j and x.”.

To evaluate f_j(x) for given j and x,
    or to count the number of a in the range between b_j−x and b_j +x (inclusive),
        one can sort a firsthand in order to apply binary search again.

The overall complexity is O(NlogN+QlogA).

Sample Code (C++)
'
#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    while (q--) {
        int b, k;
        cin >> b >> k;
        auto f = [&](int x) -> bool {
            // (# of points in [b-x, b+x]) >= k
            auto lb = lower_bound(a.begin(), a.end(), b - x);
            auto ub = upper_bound(a.begin(), a.end(), b + x);
            return ub - lb >= k;
        };
        int ng = -1, ok = (int) 2e8 + 10;
        while (ok - ng > 1) {
            int mid = (ok + ng) / 2;
            if (f(mid)) ok = mid;
            else ng = mid;
        }
        cout << ok << '\n';
    }
}
'
"""
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
print(*A)
for _ in range(Q):
    b, k = map(int, input().split())

# NlogN + Q(logN+N)