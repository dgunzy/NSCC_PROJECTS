import java.util.Scanner;

public class main {
    public static void main(String[] args ){

        String myName = args[0];
        String myAge = args[1];
        String myHometown = args[2];
        System.out.println("Hello! My name is " + myName + ". I am " + myAge + " years old.  I am from " + myHometown + ".");

        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter your first initial: ");
        String firstInitial = scanner.nextLine();
        System.out.println("Please enter your last initial: ");
        String lastInitial = scanner.nextLine();
        System.out.println("Please enter your age: ");
        String age = scanner.nextLine();
        System.out.println("Please enter your height in centimetres: ");
        String height = scanner.nextLine();
        System.out.println("Please enter your weight in lbs: ");
        String weight = scanner.nextLine();
        System.out.println("Please enter the number of siblings you have: ");
        String siblingnumber = scanner.nextLine();
        System.out.print("There was a person with the initials " + firstInitial.toUpperCase() + lastInitial.toUpperCase() + ". " +  firstInitial.toUpperCase() + lastInitial.toUpperCase());
        System.out.print(" was " + age + " years old, and only " + height + " cm tall!! Wow.  \nThey weighed " + weight + " lbs, about the same as a fully grown warthog. ");
        System.out.print(firstInitial.toUpperCase() + lastInitial.toUpperCase() + " had " + siblingnumber + " warthog siblings too.");
//        Not sure how to use word wrap in Intellij, sorry for the weird formatting.
    }
}
