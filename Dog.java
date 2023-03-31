package org.example;

class Animal {
    public void reproduce() {
        System.out.println("*reproduces*");
    }
}
class  Mammal extends Animal {
    public void milkProduction() {
        System.out.println("*produces milk*");
    }
}
class  Canid extends Mammal {
    public void growl() {
        System.out.println("grrrr");
    }
}
public class Dog extends Canid {
    public void bark() {
        System.out.println("woof woof");
    }
    public static void main(String[] args) {
        Dog doggy = new Dog();

        doggy.reproduce();
        doggy.milkProduction();
        doggy.growl();
        doggy.bark();
    }
}

