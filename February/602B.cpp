/*
题意： 求最大值和最小值之差小于等于1的区间长度

思路： 标记每个元素最后出现的位置，然后根据
	   a[i]-2 或者 a[i]+2  找得最前的位置是
	   哪里，记录更新。 

*/

#include<bits/stdc++.h>

using namespace std;
const int maxn = 1e5+20;
int a[maxn],last[maxn];
 
int main(){
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&a[i]);
	}
	int ans = 0;
	int l =0;
	for(int i=1;i<=n;i++){
		int x = -1;
		if(a[i]+2<=100000) x = max(x,last[a[i]+2]);
		if(a[i]-2>=0) x = max(x,last[a[i]-2]);
		l = max(l,x+1);
		ans = max(ans,i-l+1);
		last[a[i]]=i;
	}
	printf("%d\n",ans);
	
}
