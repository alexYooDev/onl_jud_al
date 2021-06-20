import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		int year = Integer.parseInt(str);
		
		System.out.println(year%4==0 && (year%100!=0 || year%400 == 0) ? 1 : 0);
			
	}

}