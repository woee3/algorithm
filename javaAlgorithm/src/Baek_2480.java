import java.util.Scanner;

public class Baek_2480 {
    public static void main(String[] args) {
        int[] array = new int[7];

        Scanner s = new Scanner(System.in);
        for (int i = 0; i < 3; i++){
            array[s.nextInt()] += 1;
        }

        s.close();
        int cnt = 0;
        for (int i = 1; i < 7; i++) {
            if (array[i] == 1) {
                cnt += 1;
            } else if (array[i] == 2) {
                System.out.println(i*100 + 1000);
                return;
            } else if (array[i] == 3) {
                System.out.println(i*1000 + 10000);
                return;
            }
            if (cnt == 3) {
                System.out.println(i*100);
                return;
            }
        }
    }
}
