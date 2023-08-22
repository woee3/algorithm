import java.util.Scanner;

public class Baek_10818 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int firstNumber = s.nextInt();
        int min = firstNumber;
        int max = firstNumber;
        for (int i = 1; i < n; i ++) {
            int num = s.nextInt();
            if (min > num) {
                min = num;
            } else if (max < num) {
                max = num;
            }
        }
        s.close();
        System.out.println(min + " " + max);
    }
}
