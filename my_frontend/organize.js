const sample = require("./output.json");

function range(start, end) {
    return Array(end - start + 1).fill().map((_, idx) => start + idx)
};

// const body = document.getElementById("body");
// const context = body.getContext("2d");
// context.fillStyle = "blue";
// context.fillRect(300, 300, 300, 100);

class Component {
    constructor(width, height, document) {
        this.width = width;
        this.height = height;
    };

    getContainer() {
        const container = document.getElementById("container");
        const ctx = container.getContext("2d");
    }

    draw() {
        const rectangle = rect(100, 100, 300, 300);
        
    }
    
 }

var size = Object.keys(sample).length;

let index = 0;
let result = range(0, size - 1);

while (index < result.length) {
    var obj = JSON.stringify(sample[result[index]]["type"]);

    if (obj.includes("class")) {
        console.log("success!");

    } else {
        console.log("function!")
    };
    
    index++;
};