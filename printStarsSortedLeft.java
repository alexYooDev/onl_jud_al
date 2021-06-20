import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int NMO = N - 1;

		for (int i = 1; i <= N; i++) { 
			for (int j = NMO; j > 0; j--) {	
				System.out.print(" ");	
			}
			for (int k = i; k > 0; k--) {		
				System.out.print("*");			
			}
			System.out.println();				
			NMO--;							
		}

	}
}