static void selectSort(int[] rawList) {
	int len = rawList.length;
	for (int i = 0; i < len; i++) {
		int index = 0;
		int minimum = rawList[i];
			for (int j = i; j < len; j++) {
				if (rawList[j] < minimum) {
					minimum = rawList[j];
					index = j;
				}
			int temp = rawList[i];
			rawList[i] = minimum;
			rawList[index] = temp;
			}
	}
	System.out.println(Arrays.toString(rawList));
}