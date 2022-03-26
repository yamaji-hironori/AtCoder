#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vll = vector<ll>;
using vvll = vector<vll>;

#ifdef _DEBUG
#define debug(x) cout<<#x<<": "<<x<<endl
#define debug_vec(x) cout<<#x<<" ->"<<endl;for(size_t i=0;i<x.size();i++){cout<<x.at(i)<<"; ";}cout<<endl;
#define debug_vecvec(x) cout<<#x<<" ->"<<endl;for(size_t i=0;i<x.size();i++){for(size_t j=0;j<x[i].size();j++){cout<<x.at(i).at(j)<<"; ";}cout<<endl;}cout<<endl;
#else
#define debug(x)
#define debug_vec(x)
#define debug_vecvec(x)
#endif

#define rep(i,n) for(size_t i=0;i<(n);++i)

// 以下に、24時間表記の時計構造体 Clock を定義する

// Clock構造体のメンバ変数を書く
struct Clock {

    int hour;    // 時間を表す (0~23の値をとる)
    int minute;  // 分を表す   (0~59の値をとる)
    int second;  //秒を表す   (0~59の値をとる)

    // メンバ関数 set の定義を書く
    //   関数名: set
    //   引数: int h, int m, int s (それぞれ時、分、秒を表す)
    //   返り値: なし
    //   関数の説明:
    //     時・分・秒を表す3つの引数を受け取り、
    //     それぞれ、メンバ変数 hour, minute, second に代入する
    void set(int set_hour, int set_minute, int set_second) {
        hour = set_hour;
        minute = set_minute;
        second = set_second;
    }

    // メンバ関数 to_str の定義を書く
    //   関数名: to_str
    //   引数: なし
    //   返り値: string型
    //   関数の仕様:
    //     メンバ変数が表す時刻の文字列を返す
    //     時刻の文字列は次のフォーマット
    //     "HH:MM:SS"
    //     HH、MM、SSはそれぞれ時間、分、秒を2桁で表した文字列
    string to_str() {
        string date;
        vector<int> HH_MM_SS = {hour, minute, second};
        for (int i_date: HH_MM_SS) {
            if (i_date < 10) {
                date += "0";
            }
            date += to_string(i_date);
            date += ':';
        }
        date.erase(8);
        return date;
    }

    // メンバ関数 shift の定義を書く
    //   関数名: shift
    //   引数: int diff_second
    //   返り値: なし
    //   関数の仕様:
    //     diff_second 秒だけメンバ変数が表す時刻を変更する(ただし、日付やうるう秒は考えない)
    //     diff_second の値が負の場合、時刻を戻す
    //     diff_second の値が正の場合、時刻を進める
    //     diff_second の値は -86400 ~ 86400 の範囲を取とりうる
    void shift(int diff_second) {
        second += diff_second;
        if (second >= 0) {
            plus_shif();
        } else {
            minus_shif();
        }
    }
    void plus_shif() {
        // second が正
        int n_60s = second / 60;
        int n_60s_not_much = second % 60;
        minute += n_60s;
        int n_60m = minute / 60;
        int n_60m_not_much = minute % 60;
        hour += n_60m;
        int n_24h = hour / 24;
        int n_24h_not_much = hour % 24;
        second = n_60s_not_much;
        minute = n_60m_not_much;
        hour = n_24h_not_much;
    }
    void minus_shif() {
        // second は負
        second = - second;
        int n_60s = second / 60;
        int n_60s_not_much = 60 - (second % 60);
        minute -= (n_60s + 1);
        if (minute < 0) {
            minute = - minute;
            int n_60m = minute / 60;
            int n_60m_not_much = 60 - (minute % 60);
            minute = n_60m_not_much;
            hour -= (n_60m + 1);
        } else {
            int n_60m = minute / 60;
            int n_60m_not_much = minute % 60;
            minute = n_60m_not_much;
            hour += n_60m;
        }
        if (hour < 0) {
            hour = - hour;
            int n_24h = hour / 24;
            int n_24h_not_much = 24 - (hour % 24);
            hour = n_24h_not_much;
        } else {
            int n_24h = hour / 24;
            int n_24h_not_much = hour % 24;
            hour = n_24h_not_much;
        }
        second = n_60s_not_much;
    }
};

// -------------------
// ここから先は変更しない
// -------------------

int main() {
  // 入力を受け取る
  int hour, minute, second;
  cin >> hour >> minute >> second;
  int diff_second;
  cin >> diff_second;

  // Clock構造体のオブジェクトを宣言
  Clock clock;

  // set関数を呼び出して時刻を設定する
  clock.set(hour, minute, second);

  // 時刻を出力
  cout << clock.to_str() << endl;

  // 時計を進める(戻す)
  clock.shift(diff_second);

  // 変更後の時刻を出力
  cout << clock.to_str() << endl;
}
