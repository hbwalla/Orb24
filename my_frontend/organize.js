const sample = require("./output.json");

function range(start, end) {
    return Array(end - start + 1).fill().map((_, idx) => start + idx)
};

var size = Object.keys(sample).length;

let index = 0;
let result = range(0, size - 1);

while (index < result.length) {
    var methods = JSON.stringify(sample[result[index]]["methods"]);
    console.log(methods);
    
    index++;
}

// console.log(result)

// firstArg = JSON.stringify(sample[range]);

// console.log(firstArg);