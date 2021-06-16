import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String Tstr = br.readLine();
		int T = Integer.parseInt(Tstr);
		int sum[] = new int[T];

		for (int i = 0; i < T; i++) {
			String[] str = br.readLine().split(" ");
			int A = Integer.parseInt(str[0]);
			int B = Integer.parseInt(str[1]);
			sum[i] = A + B;
			bw.write(sum[i]+"\n");
		}
		bw.flush();
		bw.close();
	}

}