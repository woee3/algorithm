import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {

        ArrayList<String> list = new ArrayList<String>();
        System.out.println(list);

        list.add("사과");
        System.out.println(list);
        list.add("수박");
        System.out.println(list);
        list.add("딸기");
        System.out.println(list);


        // 이런식으로 List의 중간에 데이터를 삽입도 가능하다
        list.add(2, "바나나");
        System.out.println(list);

    }
}