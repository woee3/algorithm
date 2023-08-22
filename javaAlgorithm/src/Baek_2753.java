import java.util.Scanner;

public class Baek_2753 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        s.close();
        if (a % 400 == 0) {
            System.out.println("1");
            return;
        }
        if (a % 4 == 0 && a % 100 != 0) {
            System.out.println("1");
            return;
        }
        System.out.println("0");
    }
}
