static boolean binarySearch(int[] List, int num, int lowBound, int highBound) {
	if (low > high) {
		System.out.println("Not found");
		return false;
	}
	int middle = (lowBound + highBound) / 2;
	
	if (num = List[middle]) {
		System.out.println("found");
		return true;
	}
	else if (num > List[middle]) {
		return binarySearch(List, num, middle + 1, highBound);
	}
	else {
		return binarySarch(List, num, lowBound, middle - 1);
	}
}