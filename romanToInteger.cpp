#include <iostream>
#include <string>
using namespace std;

int val(char s) {
	if (s == 'I') {
		return 1;
	}
	if (s == 'V') {
		return 5;
	}
	if (s == 'X') {
		return 10;
	}
	if (s == 'L') {
		return 50;
	}
	if (s == 'C') {
		return 100;
	}
	if (s == 'D') {
		return 500;
	}
	if (s == 'M') {
		return 1000;
	}
	return 0;
}
int romanToInt(string s) {
	int result{0};
	for (int i = 0; i < s.length(); i++) {
		int charOne = val(s[i]);
		if (i+1 < s.length()) {
			int charTwo = val(s[i+1]);
			if (charOne < charTwo) {
				result += charTwo - charOne;
				i++;
			}
			else {
				result += charOne;
			}            
		}
		else {
			result += charOne;
		}
	}
	return result;
}

int main() {
	string roman;
	cout << "Input Roman numeral (this will not work for numbers above 3999): ";
	cin >> roman;
	cout << roman << " in decimal is " << romanToInt(roman) << '\n';
	return 0;
}