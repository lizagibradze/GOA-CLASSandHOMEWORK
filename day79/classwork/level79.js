

// ubralo 


// function hi(name){
//     console.log("hi"+ name)

// }




// arrows dros unda gamoviyenot let an const

let hi = (name, text ) =>  text + name


// 1 ----------------------------------

let ja = (num, num2) =>  num + num2;

console.log(ja(1, 3));

// aq ertze metia magram tu marto erti gaq shegidzlia prchxilebi ar gamoiyeno


// ------------------------------------




const button = document.getElementById("btn")


button.addEventListener("click", () =>{
    alert("hi")

})



// ---






const box = document.getElementById("box1")

box.addEventListener("mouseover" , () => {

    box.style.backgroundColor = "Red"

})


box.addEventListener("mouseout", () =>{

    box.style.backgroundColor = "black"

})




// ------





const bbtn = document.getElementById("bbtn");

bbtn.addEventListener("mousedown", () =>{

bbtn.textContent = "down"
bbtn.style.backgroundColor = "Red"


})

bbtn.addEventListener("mouseup", () =>{

    bbtn.textContent = "up"
    bbtn.style.backgroundColor = "green"

})








       