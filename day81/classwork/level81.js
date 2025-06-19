

// console.log("ki");

// const counter = document.createElement("strike");
// counter.textContent = "1.6";

// document.body.append(counter)



// 1



// console.log("ki");

// const counter = document.createElement("strike");
// counter.textContent = "goa is best";

// document.body.append(counter)




// ----------------------------------






console.log("ki");

const counter = document.createElement("strike");
const counter1 = document.createElement("p");

counter.textContent = "goa is best";
counter.textContent = "lomi";


document.body.append(counter, counter1);



for (let index = 0; index < 10; index++) {
      const div = document.createElement("p");
      div.textContent = "Goa is best";
      document.body.append(div);
    }


// ----------------------------------




// for (let index = 0; index < 10; index++) {
//       const div = document.createElement("p");
//       div.textContent = "child" + index;
//       document.body.append(div);
//     }


for (let index = 0; index < 10; index++) {
      const div = document.createElement("p");
      div.textContent = `child" ${index}`; 
      document.body.append(div);
    }


console.log('---------------------');


const array = ["el 1", "el 2", 3, 4 , 5]




const arrayMap = array.map((item, index) => {

    return item

});







const arrayFilter = array.filter((el, index) => {
if (el > 4){
    return el
}


});




console.table({
    array: array
});










