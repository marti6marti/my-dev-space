package CadenaDeCaracteres.SenseEspais;

import java.util.Scanner;

public class SenseEspais {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();

        text = text.replace(" ","");
        System.out.println(text);

    }
}
