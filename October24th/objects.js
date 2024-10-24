class Person {
  constructor(name, age) {
    this.name = name; // 'this' refers to the new object being created
    this.age = age;
  }

  // A method to greet
  greet() {
    console.log(`Hi, I'm ${this.name} and I'm ${this.age} years old.`);
  }
}


let person1 = new Person('Amy', 28);
person1.greet(); // Output: Hi, I'm Amy and I'm 28 years old.



class Car {
  constructor(make, model) {
    this.make = make;
    this.model = model;
  }

  start() {
    console.log(`${this.make} ${this.model} is starting.`);
  }
}

let car1 = new Car('Toyota', 'Corolla');
car1.start(); // Output: Toyota Corolla is starting.



class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    console.log(`${this.name} makes a sound.`);
  }
}

class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks.`);
  }
}

let dog1 = new Dog('Buddy');
dog1.speak(); // Output: Buddy barks.



class Rectangle {
  constructor(width, height) {
    this.width = width;
    this.height = height;
  }

  // Getter for the area
  get area() {
    return this.width * this.height;
  }

  // Setter for changing the width
  set width(newWidth) {
    this._width = newWidth > 0 ? newWidth : 1;
  }

  get width() {
    return this._width;
  }
}

let rect = new Rectangle(10, 5);
console.log(rect.area); // Output: 50
rect.width = -5;
console.log(rect.width); // Output: 1 (since width can't be negative)
