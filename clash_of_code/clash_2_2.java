import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int M = in.nextInt();
        int S = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        int blocks = 0;
        for (int i = 0; i < N; i++) {
            String row = in.nextLine();
            for(int j = 0; j < M; j++){
                char c = row.charAt(j);
                blocks += c=='o' ? 1 : 0;
            }
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(blocks * S);
    }
}