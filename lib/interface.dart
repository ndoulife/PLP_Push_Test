// Define an interface
abstract class Drawable {
  void draw();
}

// Implement the interface in a class
class Circle implements Drawable {
  @override
  void draw() {
    print("Drawing a circle");
  }
}
