
const currentData = new Date()
console.log(currentData)








class Human{
    constructor(name, surname, age){
        this.name = name;
        this.surname = surname;
        this.age = age;

    }



    get talk(){
        console.log(`HI`)
    }


    set someWord(word){
        console.log(word)
    }



}



const newHuman = new Human("liza", "gibradze", -50);

const newHuman1 = new Human("iii", "oo", 500);



newHuman.talk

newHuman1.someWord = "hello bye"

console.log(newHuman)

console.log(newHuman1)





