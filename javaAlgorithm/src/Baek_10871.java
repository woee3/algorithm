import java.util.Scanner;

public class Baek_10871 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int x = s.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i ++) {
            array[i] = s.nextInt();
        }
        s.close();

        int cnt = 0;
        for (int num : array) {
            if (num < x) {
                System.out.print(num + " ");
            }
        }
    }
}
