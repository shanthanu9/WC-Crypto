#include <iostream>
using namespace std;

int main() {
	//FILE * file = fopen("key", "r");
	int key = 10;
	//fscanf(file, "%d", &key);

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
