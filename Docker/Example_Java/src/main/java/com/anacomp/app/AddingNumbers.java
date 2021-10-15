import java.util.Scanner;

public class AddingNumbers {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int length = 5;
        int[] inputValues = new int[length];
        System.out.println("Please enter "+ length +" number/s to sum up")

        while (length > 0) {
            length--;
            inputValues[length] = in.nextInt();
        }

        System.out.println("Sum: " + AddingNumbers(inputValues));
    }

    public static int AddNumbers(int[] values) {
        int sum;
        for(int i=0; i<length; i++){
            sum+= i;
        }
        return sum;
    }
}