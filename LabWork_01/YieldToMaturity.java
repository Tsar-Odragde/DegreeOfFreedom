package org.example;
import java.util.Scanner;
public class YieldToMaturity {
    float c, f, p, n;
    Scanner myScan = new Scanner(System.in);
    public void input() {
        System.out.println("Enter the value of c: ");
        c = myScan.nextFloat();
        System.out.println("Enter the value of f: ");
        f = myScan.nextFloat();
        System.out.println("Enter the value of p: ");
        p = myScan.nextFloat();
        System.out.println("Enter the value of n: ");
        n = myScan.nextFloat();
    }
    public void calcYTM() {
        float answer;
        answer = (c + ((f-p)/n))/((f+p)/2);
        System.out.println("The approx yield to maturity is: " + answer);
    }
    public static void main(String[] args) {
        YieldToMaturity myCalc = new YieldToMaturity();

        myCalc.input();
        myCalc.calcYTM();
    }
}
