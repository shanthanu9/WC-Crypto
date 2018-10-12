#include <iostream>
using namespace std;

int main() {
	int key = 10;
	char c;
	while(scanf("%c", &c)){
		if(c == '#')
			break;
		if('a' <= c && c <= 'z')
			c = (c-'a'+key)%26+'a';
		cout<<char(c);
	}
	return 0;
}	
