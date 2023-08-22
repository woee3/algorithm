import java.util.Scanner;

public class Baek_10807 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i ++) {
            array[i] = s.nextInt();
        }
        int v = s.nextInt();
        s.close();

        int cnt = 0;
        for (int num : array) {
            if (num == v) {
                cnt++;
            }
        }
        System.out.println(cnt);


    }
}
