#include <iostream>

using namespace std;

int fibo(int index) {
	if (index == 0) {
		return 0; // the zeroth index will be 0, oneth index 1
	} else {
	int nthNum;		 	   // only count the two numbers prior to the 
	int nMinusOnethNum{0}; // targeted number at the index
	int nMinusTwothNum{1};
	for (int i = 0; i < index; i++) {
		nthNum = nMinusOnethNum + nMinusTwothNum;
		nMinusTwothNum = nMinusOnethNum;
		nMinusOnethNum = nthNum;
	} return nthNum;
	}
}
int main() {
	int n;
	cout << "Find value of the fibonacci sequence at the index of: ";
	cin >> n;
	cout << "The value is " << fibo(n) << endl;
	return 0;
}