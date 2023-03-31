package org.example;

import java.util.Scanner;
public class DegreeOfFreedom {
    public void calculateLittering(float males, float females, float litters, float deposits) {
        float total = males + females;
        float litteringMales, litteringFemales;
        litteringMales = (males/total) * ((litters/total)*100);
        litteringFemales = (females/total) * ((litters/total)*100);
        System.out.println("The total number of littering males is: " + litteringMales);
        System.out.println("The total number of littering females is: " + litteringFemales);
    }
    public static void main(String[] args) {
        float totalMale, totalFemale, totalDeposit, totalLitter;

        Scanner scan = new Scanner(System.in);
        DegreeOfFreedom dof = new DegreeOfFreedom();
        System.out.println("Enter the total of males: ");
        totalMale = scan.nextInt();
        System.out.println("Enter the total of females: ");
        totalFemale = scan.nextInt();
        System.out.println("Enter the total who deposits: ");
        totalDeposit = scan.nextInt();
        System.out.println("Enter the total who litters: ");
        totalLitter = scan.nextInt();

        dof.calculateLittering(totalMale, totalFemale, totalLitter, totalDeposit);
    }
}
