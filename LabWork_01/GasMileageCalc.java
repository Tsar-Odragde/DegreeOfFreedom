package org.example;
import java.util.Scanner;

class Odometer {
    float prevMileage, curMileage;
    Scanner myScan = new Scanner(System.in);

    public void setPrevMileage() {
        System.out.println("Enter your previous mileage: ");
        this.prevMileage = myScan.nextFloat();
    }
    public void setCurMileage() {
        System.out.println("Enter your current mileage:");
        this.curMileage = myScan.nextFloat();
    }
}
public class GasMileageCalc extends Odometer {
    float gasFilled;
    public void setGasFilled() {
        System.out.println("Enter how many liters of gas you added to the car: ");
        gasFilled = myScan.nextFloat();
    }
    public void calculateGasMileage(float miles) {
        float gasMileage;
        gasMileage = miles/gasFilled;

        System.out.println("The gas mileage of your car is " + gasMileage + " kilometers/liter");
    }
    public static void main(String[] args) {
        float mileage;
        GasMileageCalc myCalc = new GasMileageCalc();

        myCalc.setPrevMileage();
        myCalc.setCurMileage();
        myCalc.setGasFilled();
        mileage = myCalc.curMileage - myCalc.prevMileage;

        myCalc.calculateGasMileage(mileage);
    }
}
