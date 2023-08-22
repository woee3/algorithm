import java.util.Scanner;

public class Baek_2525 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int h = s.nextInt();
        int m = s.nextInt();
        int cook = s.nextInt();
        s.close();

        h += (cook+m) / 60;
        m = (cook+m) % 60;

        if (h >= 24) {
            h -= 24;
        }
        System.out.println(h + " " + m);
    }
}
