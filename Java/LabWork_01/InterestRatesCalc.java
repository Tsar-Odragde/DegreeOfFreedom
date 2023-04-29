package org.example;
import java.util.Scanner;
import java.lang.Math;

public class InterestRatesCalc {
    float p, r, t, n;
    Scanner myScan = new Scanner(System.in);
    public void input() {
        System.out.println("Enter the value of principal amount: ");
        p = myScan.nextFloat();
        System.out.println("Enter the annual rate of interest: ");
        r = myScan.nextFloat();
        System.out.println("Enter the years: ");
        t = myScan.nextFloat();
        System.out.println("Enter number of times interest is compounded per year: ");
        n = myScan.nextFloat();
    }
    public void calcSimpleInterestRate() {
        float answer;
        answer = (p*r*t)/100;
        System.out.println("The simple interest rate is: " + answer);
    }
    public void calcCompInterestRate() {
        double answer;
        answer = p*Math.pow((1+(r/n)), (n*t));
        System.out.println("The compound interest rate is: " + answer);
    }
    public static void main(String[] args) {
        InterestRatesCalc myCalc = new InterestRatesCalc();

        myCalc.input();
        myCalc.calcSimpleInterestRate();
        myCalc.calcCompInterestRate();
    }
}
