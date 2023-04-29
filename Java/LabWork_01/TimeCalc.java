package org.example;
import java.util.Scanner;

class Place {
    float distance, speed;
    Scanner myScan = new Scanner(System.in);

    public void input() {
        System.out.println("Enter the distance in meters to your house: ");
        this.distance = myScan.nextFloat();

        System.out.println("Enter your speed in meters/minute: ");
        this.speed = myScan.nextFloat();
    }
}
public class TimeCalc extends Place {
    public void calculateTime() {
        float time;
        time = distance/speed;
        System.out.println("It takes you " + time + " minutes to get from the college to your house.");
    }
    public static void main(String[] args) {
        TimeCalc myCalc = new TimeCalc();

        myCalc.input();
        myCalc.calculateTime();
    }
}
