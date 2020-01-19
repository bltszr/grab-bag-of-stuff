#include <iostream>
#include <vector>
using namespace std;

// vector_sizewill be the size of the vector
vector<bool> erastothenes(int vector_size) {
	vector<bool> res (vector_size, true);
	res[0] = false;
	res[1] = false;
	for (int i = 2; i < vector_size/ 2; i++) {
		if (res[i]) {
			int multiplier = 2;
			int traverser = i * multiplier;
			while (multiplier <= (vector_size / i)) {
				res[traverser] = false;
				multiplier++;
				traverser = i * multiplier;
			}
		}
	}
	return res;
}

int main() {
	int n;
	cout << "Input the number: ";
	cin >> n;
	vector<bool> prim = erastothenes(n);
	for (int i = 0; i < prim.size(); i++) {
		if (prim[i]) {
			cout << i << ": " << prim[i] << endl;
		}
	}
	return 0;
}