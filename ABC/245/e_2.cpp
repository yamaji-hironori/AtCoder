#include <bits/stdc++.h>
using namespace std;
const int CM=2e5+5;

struct Box{
	int H=0,W=0;
};
vector<Box> FChoVec(CM);
vector<Box> FBoxVec(CM);
multiset<int> l_MulSet;

bool cmp(Box AStruA,Box AStruB){
	return AStruA.H>AStruB.H;
}

int main(){
	int l_ChoNum=0,l_BoxNum=0,j=0;
	cin >> l_ChoNum >> l_BoxNum;
	
	for (int i=0;i<l_ChoNum;i++)
		scanf("%d",&FChoVec[i].H);
	for (int i=0;i<l_ChoNum;i++)
		scanf("%d",&FChoVec[i].W);
		
	for (int i=0;i<l_BoxNum;i++)
		scanf("%d",&FBoxVec[i].H);
	for (int i=0;i<l_BoxNum;i++)
		scanf("%d",&FBoxVec[i].W);
		
	sort(FChoVec.begin(),FChoVec.end(),cmp);
	sort(FBoxVec.begin(),FBoxVec.end(),cmp);
	
	for (int i=0;i<l_ChoNum;i++){
		while (j<l_BoxNum and FBoxVec[j].H>=FChoVec[i].H){
			l_MulSet.insert(FBoxVec[j].W);
			j++;
		}
		auto l_Temp=l_MulSet.lower_bound(FChoVec[i].W);
		if (l_Temp==l_MulSet.end()){
			cout << "No";
			return 0;
		}
		l_MulSet.erase(l_Temp);
	}
	cout << "Yes";

    return 0;
}
