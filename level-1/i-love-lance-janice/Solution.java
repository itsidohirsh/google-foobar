public class Solution {
    public static String solution(String s) {
        String result = "";

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c >= 'a' && c <= 'z') {
                result += (char) ('a' + 'z' - c);
            } else {
                result += c;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String check;

        check = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!";
        System.out.println(check);
        System.out.println(solution(check));
        System.out.println();

        check = "wrw blf hvv ozhg mrtsg'h vkrhlwv?";
        System.out.println(check);
        System.out.println(solution(check));
        System.out.println();
    }
}