import java.util.Scanner;
public class Baek_9498 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        s.close();

        if (a >= 90) {
            System.out.println("A");
            return;
        }
        if (a >= 80) {
            System.out.println("B");
            return;
        }
        if (a >= 70) {
            System.out.println("C");
            return;
        }
        if (a >= 60) {
            System.out.println("D");
            return;
        }
        System.out.println("F");

    }
}
