import java.util.Scanner;

public class Baek_2884 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int h = s.nextInt();
        int m = s.nextInt();
        s.close();

        if (m - 45 < 0) {
            h -= 1;
            m += 15;
        } else m -= 45;
        System.out.println(h + " " + m);
    }
}
