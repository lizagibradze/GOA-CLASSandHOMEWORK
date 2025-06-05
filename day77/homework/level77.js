
// 1

const el = ["a", "e", "i", "o", "u"];

const spliced = el.splice(1, 3);

console.log(spliced)


const sliced = spliced.slice(1, 2);

console.log(sliced);

sliced.splice(1, 0, "p", "b");

console.log(sliced)




