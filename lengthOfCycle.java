import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int num = sc.nextInt();
        sc.close();
		int count = 0;
		int newNum = num;	
		while (true) {
			num = ((num % 10) * 10) + (((num / 10) + (num % 10)) % 10);
			count++;
			if (newNum == num) {
				break;
			}
		}
		System.out.println(count);
	}
}