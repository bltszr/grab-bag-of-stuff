#include <cstdlib>
#include <iostream>
using namespace std;

// takes in sorted array of integers + its size,
// returns a sorted array of the squares of those integers
// also this whole thing assumes that it will contain both
// negative and positive integers
// might have to refactor later

int abs(int i) {
	int j;
	if (i < 0) {
		j = (0 - i);
	} else {
		j = i;
	}
	return j;
}

int* squaring(int* intarr, int size) {
	// init vars
	static int* res_ptr = (int*) malloc(size * sizeof(int));
	int* front_ptr = intarr;
	int* back_ptr = intarr + (size - 1);
	int i = size - 1;
	while (i >= 0)  {
		int back = abs(*back_ptr);
		int front = abs(*front_ptr);
		
		if (back >= front) {
			res_ptr[i] = (back * back);
			back_ptr--;
		} else {
			res_ptr[i] = (front * front);
			front_ptr++;
		}
		i--;
	}
	return res_ptr;

}

int main() {
	
	int size;
	cout << "Input the size of the array: ";
	cin >> size;
	int * arr_ptr = (int*) malloc(size * sizeof(int));
	cout << "Input the numbers: ";
	
	for (int i = 0; i < size; i++) {
		cin >> arr_ptr[i];
	}
	
	int * new_arr = squaring(arr_ptr, size);
	
	for (int j = 0; j < size; j++) {
		cout << new_arr[j] << " ";
	}
	
	return 0;
}