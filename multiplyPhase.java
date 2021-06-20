import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int A = sc.nextInt();
		int B = sc.nextInt();
		
		int Bdg1 = B%10;
		int Bdg2 = ((B%100)/10);
		int Bdg3 = ((B%1000)/100);

		if(A>0 && A<1000 || B>0 && B<1000) {
			
		System.out.println(Bdg1*A);
		System.out.println(Bdg2*A);
		System.out.println(Bdg3*A);
		System.out.println(B*A);
		}
	}

}