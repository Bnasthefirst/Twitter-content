const dog = {
  name: "Buddy",
  breed: "Golden Retriever",
  describe: function() {
    return `${this.name} is a ${this.breed}.`;
  }
};

console.log(dog.describe());  // Output: "Buddy is a Golden Retriever."

const car = new Object();
car.make = "Toyota";
car.model = "Corolla";
car.describe = function() {
  return `${this.make} ${this.model}`;
};

console.log(car.describe());  // Output: "Toyota Corolla"



console.log(dog.name);       // Dot notation
console.log(dog['breed']);   // Bracket notation

dog.name = "Max";            // Modifying property



const person = {
  firstName: "John",
  lastName: "Doe",
  fullName: function() {
    return `${this.firstName} ${this.lastName}`;
  }
};

console.log(person.fullName());  // Output: "John Doe"



function human(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return `${this.firstName} ${this.lastName}`;
  };
}

const john = new human("John", "Doe");
console.log(john.fullName());  // Output: "John Doe"
