import java.util.Scanner;

public class DigitSum {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Input integer: ");
		int digit = input.nextInt();
		System.out.println("Digit sum is : %d", digitSum(digit));
	}
	
	private int digitSum(int digit) {
		int sum = 0;
		int proc = digit;
		while (proc >= 10) {
			sum += proc % 10;
			proc /= 10;
		}
		sum += proc;
		return sum;
	}
}