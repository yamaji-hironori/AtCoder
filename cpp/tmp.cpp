#line 1 "main.cpp"
#include <bits/stdc++.h>
#line 2 "utils/macro.hpp"
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> PINT;
typedef pair<long long, long long> PLL;

#define rep(i,n) for (ll i = 0; i < (ll)(n); ++i)
#define reps(i,s,n) for (ll i = s; i < (ll)(n); ++i)
#define rep1(i,n) for (ll i = 1; i <= (ll)(n); ++i)
#define per(i,n) for (ll i = (ll)(n) - 1; i >= 0; --i)
#define all(c) begin(c),end(c)

template<typename T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }
template<typename T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
void precout(int n = 20) { cout << std::fixed << std::setprecision(n); }
#define print(a) cout << a << endl;
const int INFI = (1 << 30) - 1;
const long long INFLL = (1LL << 62) - 1;
template<typename T> void printv(vector<T>&v) {
    int n = v.size() - 1;
    rep(i, n) cout << v[i] << " ";
    cout << v.back() << endl;
}
template<typename T> void printd(deque<T>&v) {
    int n = v.size() - 1;
    rep(i, n) cout << v[i] << " ";
    cout << v.back() << endl;
}
const int dy[4] = { 0, 1, 0, -1 };
const int dx[4] = { 1, 0, -1, 0 };
const int dx2[4] = { 1, 1, -1, -1 };
const int dy2[4] = { 1, -1, 1, -1 };
const int dy8[8] = { 1, 1, 1, 0, 0, -1, -1, -1 };
const int dx8[8] = { -1, 0, 1, -1, 1, -1, 0, 1 };
double deg2rad(double deg) { return deg * M_PI / 180; }
double rad2deg(double rad) { return rad * 180 / M_PI; }
void yesorno(bool flag) {
    if(flag) print("Yes")
    else print("No");
}
template<typename T> T ceil_int(T A, T B) {
    return (A + (B - T(1))) / B;
}
long long powll(long long a, long long e) {
    if(e == 0) return 1;
    ll res = a;
    rep(i,e-1) res *= a;
    return res;
}
vector<vector<char>> rps_winner_table() {
    vector<vector<char>> t(300, vector<char>(300));

    t['R']['R'] = t['R']['S'] = t['S']['R'] = 'R';
    t['S']['S'] = t['S']['P'] = t['P']['S'] = 'S';
    t['P']['P'] = t['P']['R'] = t['R']['P'] = 'P';

    t['r']['r'] = t['r']['s'] = t['s']['r'] = 'r';
    t['s']['s'] = t['s']['p'] = t['p']['s'] = 's';
    t['p']['p'] = t['p']['r'] = t['r']['P'] = 'p';

    return t;
}
template <class T> vector<vector<T>> makevv(int s1, int s2, T init) {
    return vector<vector<T>>(s1, vector<T>(s2, init));
}
template <class T> vector<vector<vector<T>>> makevvv(int s1, int s2, int s3, T init) {
    return vector<vector<vector<T>>>(s1, vector<vector<T>>(s2, vector<T>(s3, init)));
}
#line 1 "utils/atcoder_debug.hpp"
#include <atcoder/all>

string to_string(atcoder::modint998244353 m) {
    return to_string(m.val());
}

string to_string(atcoder::modint1000000007 m) {
    return to_string(m.val());
}
#line 2 "utils/debug.hpp"
using namespace std;

template <typename A, typename B>
string to_string(pair<A, B> p);

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p);

template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p);

string to_string(const string& s) {
    return '"' + s + '"';
}

string to_string(char c) {
    return {c};
}

template <class _T>
string to_string(complex<_T>& c) {
    return "(" + to_string(c.real()) + "," + to_string(c.imag()) + ")";
}

string to_string(const char* s) {
    return to_string((string) s);
}

string to_string(bool b) {
    return (b ? "true" : "false");
}

string to_string(vector<bool> v) {
    bool first = true;
    string res = "{";
    for (int i = 0; i < static_cast<int>(v.size()); i++) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(v[i]);
    }
    res += "}";
    return res;
}

template <size_t N>
string to_string(bitset<N> v) {
    string res = "";
    for (int i = N - 1; i >= 0; --i) {
        res += static_cast<char>('0' + v[i]);
    }
    return res;
}

template <typename A>
string to_string(A v) {
    if(v.size() >= 200) {
        return "Too big length";
    }

    bool first = true;
    string res = "{";
    for (const auto &x : v) {
        if (!first) {
            res += ", ";
        }
        first = false;
        res += to_string(x);
    }
    res += "}";
    return res;
}

template <typename A, typename B>
string to_string(pair<A, B> p) {
    return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <typename A, typename B, typename C>
string to_string(tuple<A, B, C> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ")";
}

template <typename A, typename B, typename C, typename D>
string to_string(tuple<A, B, C, D> p) {
    return "(" + to_string(get<0>(p)) + ", " + to_string(get<1>(p)) + ", " + to_string(get<2>(p)) + ", " + to_string(get<3>(p)) + ")";
}

void debug_out() { cerr << endl; }

template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
    cerr << " " << to_string(H);
    debug_out(T...);
}

#ifdef LOCAL
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif
#line 6 "main.cpp"
using namespace std;
const long double eps = std::numeric_limits<long double>::epsilon();
using pqt = int;
auto pqcomp = [](pqt a, pqt b) {
    return a < b;
};
std::priority_queue<pqt, std::vector<pqt>, decltype(pqcomp)> que{pqcomp};
// using mint = atcoder::modint1000000007;
// const long long MOD = 1e9+7;
using mint = atcoder::modint998244353;
const long long MOD = 998244353;

int main() {
    std::cin.tie(0);
    std::ios_base::sync_with_stdio(false);

    int a,b; cin >> a >> b;
    yesorno((a+1) == b || (a == 1 && b == 10));
}
