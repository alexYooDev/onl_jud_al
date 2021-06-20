import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String str = br.readLine();
		int N = Integer.parseInt(str);
		int num = 0;
		
		for (int i = 0; i < N; i++) {
			num = N-i;
			bw.write(num+"\n");
		}
		bw.flush();
		bw.close();
	}
}