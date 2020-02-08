#include <cstdlib>
#include <iostream>
using namespace std;

// takes in sorted array of integers + its size,
// returns a sorted array of the squares of those integers
// also this whole thing assumes that it will contain both
// negative and positive integers
// might have to refactor later

int* squaring(int * intarr, int size) {
	
	// first we find the element with the smallest square possible
	int* pivot_ptr;
	for (int i = 0; i < size - 1; i++) {
		// if we have 0, that's always going to be the smallest one
		if (intarr[i] <= 0 && intarr[i+1] > 0) {
			if ((0 - intarr[i]) <= intarr[i + 1]) {
				pivot_ptr = &intarr[i];
			} else {
				pivot_ptr = &intarr[i + 1];
			}
			break;
		}
	}
	
	// begin squaring
	int *res_ptr;
	res_ptr = (int*) malloc(size * sizeof(int));
	
	// init the first value
	res_ptr[0] = (*pivot_ptr) * (*pivot_ptr);

	// init the pointers to the back and front
	int * front_ptr = pivot_ptr + 1;
	int * back_ptr = pivot_ptr - 1;
	for (int j = 1; j < size; j++) {
		cout << "Back pointer pointing to " << *back_ptr << " and front pointer pointing to " << *front_ptr << endl;
		
		// if neither have reached the end
		if (back_ptr >= intarr && front_ptr <= intarr + size) {
			if ((0 - (*back_ptr)) < *front_ptr) {
				res_ptr[j] = (*back_ptr) * (*back_ptr);
				back_ptr--;
			} else {
				res_ptr[j] = (*front_ptr) * (*front_ptr);
				front_ptr++;
			}
		// if back_ptr has reached the end but front_ptr hasn't
		} else if (front_ptr <= intarr + size) {
			res_ptr[j] = (*front_ptr) * (*front_ptr);
			front_ptr++;
		// only posibility now is that back_ptr hasn't reached the end
		} else {
			res_ptr[j] = (*back_ptr) * (*back_ptr);
			back_ptr--;
		}
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