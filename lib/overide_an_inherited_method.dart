import 'dart:convert';
import 'dart:io';

class Person {
  late String name;
  late int age;

  Person(this.name, this.age);

  factory Person.fromJson(Map<String, dynamic> json) {
    return Person(json['name'], json['age']);
  }
}

void main() {
  // Read data from a JSON file
  String jsonString = File('data.json').readAsStringSync();
  Map<String, dynamic> jsonData = json.decode(jsonString);

  // Initialize a Person object with data from the file
  Person person = Person.fromJson(jsonData);

  print('Name: ${person.name}, Age: ${person.age}');
}
