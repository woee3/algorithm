import java.util.Scanner;

public class Beak_2739 {
    public static void main (String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        scan.close();

        for (int i = 1; i < 10; i++) {
            System.out.println(n + " * " + i + " = " + n*i);
        }

    }
}
