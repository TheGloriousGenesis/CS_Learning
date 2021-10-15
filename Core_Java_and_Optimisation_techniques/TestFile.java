import java.io.*;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            String value = in.nextLine();
            MyRegex myRegex = new MyRegex();
            boolean isIpAddress = myRegex.isIpAddress(value);
            System.out.println(isIpAddress);
        }

    }

    private static class MyRegex {
        public boolean isIpAddress(String value) {
            final Pattern pattern = Pattern.compile("^([0-9]+(\\.[0-9]+)+)$", Pattern.CASE_INSENSITIVE);
            final Matcher matcher = pattern.matcher(value);
            return matcher.matches();
        }
    }
}