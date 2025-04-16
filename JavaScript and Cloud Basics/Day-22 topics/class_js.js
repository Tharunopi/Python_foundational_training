class Person{
    constructor(name){
        this.name = name;
    }

    getName(){
        return this.name;
    }

    static greet(){
        return "Hi!" + this.name
    }
}

let p1 = new Person("Tharun");
let name = p1.getName();
console.log(Person.greet("Atithya"))