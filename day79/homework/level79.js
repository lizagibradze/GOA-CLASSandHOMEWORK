
//n 1

// 1

// background gaxda lightblue roca davachiret buttons
const btn1 = document.getElementById("btn1");




btn1.addEventListener("click", () => {


    document.body.style.backgroundColor = "lightblue";


});


// 2


const btn2 = document.getElementById("btn2");
const turngreen = () => {
    document.body.style.backgroundColor = "green"
};


btn2.addEventListener("click", turngreen);




// 3

const btn3 = document.getElementById("btn3");
const colorchange = (color) => () => {
    document.body.style.backgroundColor = color;
}


btn3.addEventListener("click", colorchange ("red"));


// n 2

var div1 = document.getElementById("div1");

var div2 = document.getElementById("div2");




div1.addEventListener("mouseover", function(){
    div1.style.width= "200px";
    div1.style.height= "200px";
})



div1.addEventListener('mouseout', function() {
    div1.style.width = '100px';
    div1.style.height = '100px';
});




div2.addEventListener("mouseover", function(){
    div2.style.width= "200px";
    div2.style.height= "200px";
})



div2.addEventListener('mouseout', function() {
    div2.style.width = '100px';
    div2.style.height = '100px';
});




