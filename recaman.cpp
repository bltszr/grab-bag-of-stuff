// Program to compute the nth term of a recaman sequence
#include <iostream>
#include <vector>
using namespace std;

vector<int> recaman(int n) {
	vector<int> recseq;
	recseq.push_back(0);
	for (int i = 1; i < n; i++) {
		int newnum = recseq[i-1] - i;
		int iternum;
		for (iternum = 0; iternum < i; iternum++) {
			if ((recseq[iternum] == newnum) || newnum < 0) {
				newnum = recseq[i-1] + i;
				break;
			}
		}
		
		recseq.push_back(newnum);
	}
	return recseq;
}

int main() {
	int n;
	cout << "Find the values of the recaman sequence until the index of: ";
	cin >> n;
	cout << "\n";
	vector<int> result = recaman(n);
	for (int i = 0; i < n; i++) {
		cout << i+1 << ": " << result[i] << endl;
	}
	return 0;
}