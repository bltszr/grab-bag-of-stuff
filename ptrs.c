#include <stdio.h>

// small reminder on why pointers exist

int main() {
	int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};
	int i, *ptr_a, *ptr_b;
	const int arr_size = (sizeof(arr)/sizeof(arr[0]));
	
	ptr_a = &arr[0];
	ptr_b = &arr[arr_size-1];
	
	for (i = arr_size; i > 0; i--) {
		if (ptr_a == ptr_b) {
			printf("Hi! we're both at %x with the value of %d!\n", ptr_a, *ptr_a);
		} else {
			printf("A is at %x with the value of %d!\n", ptr_a, *ptr_a);
			printf("B is at %x with the value of %d!\n", ptr_b, *ptr_b);
		}
		ptr_a++;
		ptr_b--;
	}
}