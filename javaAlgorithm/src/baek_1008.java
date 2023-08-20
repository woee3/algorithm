import java.util.Scanner;

public class baek_1008 {
    public static void main (String[] arg) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();
        long b = sc.nextInt();
        sc.close();

        System.out.println(a/b + "." + ((a*1_000_000_000)/b)%1_000_000_000);
    }
}
