
let arrToDo = [];
const inp = document.getElementById("inp");
const boxContainer = document.getElementsByClassN("box-container")[0];
const btnAdd = document.getElementById("add");
const btnReset = document .getElementById("reset");

btnAdd.onclick  = () => {
    const value = inp.value;
    arrToDo.push(value);

    boxContainer.innerHTML = "" // reset boxContainer

    arrToDo.forEach((item, index) => { // for each
        const div = document.createElement("div");
        div.textContent = item
        boxContainer.append(div)
    })
}
        






btnReset.onclick  = () => {
    boxContainer.innerHTML = "";

}




