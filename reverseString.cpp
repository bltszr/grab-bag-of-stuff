#include <iostream>
#include <vector>
#include <string>
using namespace std;
// recursively reverse a string without a return statement
// note: does not work with whitespace

void reverseString(vector<char>& string_vec) {
	if (string_vec.size() == 1) {
		string_vec = string_vec;
	}
	else {
		char x = string_vec[0];
		string_vec.erase(string_vec.begin());
		reverseString(string_vec);
		string_vec.push_back(x);
	}
}
int main() {
	string in_string;
	vector<char> new_vec;
	cout << "Input string to reverse: ";
	cin >> in_string;
	for (int x = 0; x < in_string.size(); x++) {
		new_vec.push_back(in_string[x]);
	}
	reverseString(new_vec);
	string out_string(new_vec.begin(), new_vec.end());
	cout << "The reverse is: " << out_string << endl;;
	return 0;
}