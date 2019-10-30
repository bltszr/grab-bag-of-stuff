static int[] mergeSort(int[] lst) { // code supplied by Microsoft
	int length = lst.length;
	int[] left;
	int[] right;
	
	if (length % 2 == 0) {
		left = new int[length/2];
		right = new int[length/2];
	}
	else {
		left = new int[length/2];
		right = new int[length/2 + 1];
	}
	
	for (int i = 0; i < length; i++) {
		if (i < length/2) {
			left[i] = lst[i];
		}
		else {
			right[i-length/2] = lst[i];
		}
	}
	
	left = mergeSort(left);
	right = mergeSort(right);
	
	return merge(left, right);
}

static int[] merge(int[] left, int[] right) {
	int[] result = new int[left.length + right.length];
	
	int i = 0;
	int j = 0;
	int index = 0;
	
	while (i < left.length && j < right.length) {
		if (left[i] < right[j]) {
			result[index++] = left[i++];
		}
		else {
			result[index++] = right[j++];
		}
	while (i < left.length) {
		result[index++] = left[i++];
	}
	while (j < right.length) {
		result[index++] = right[j++];
	}
	return result;
}