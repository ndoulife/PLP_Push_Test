// Define a superclass
class Animal {
  void makeSound() {
    print("Animal makes a sound");
  }
}

// Define a subclass that inherits from Animal
class Dog extends Animal {
  @override
  void makeSound() {
    print("Dog barks");
  }
}
