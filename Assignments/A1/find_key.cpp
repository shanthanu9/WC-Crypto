#include <iostream>
using namespace std;

int main() {
	string s;
	int freq[26] = {0}, m = 0;
	while(cin>>s) {
		for(auto c:s) { 
			freq[c-'a']++;
		}
	}	
	for(int i = 1; i < 26; i++) {
		if(freq[m] < freq[i])
			m = i;
	}
	int key = 26 - (m - ('e'-'a'))%26;
	cout<<key;
    for(int i = 0; i < 26; i++) 
		cout<<char('a'+i)<<" : "<<freq[i]<<endl;
	return 0;
}
